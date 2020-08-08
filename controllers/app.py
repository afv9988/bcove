#@auth.requires_login()
import shutil
from datetime import datetime



'''## Main function called when enter to the main URL, the can have an argumen
	@args info: filename of file to be analyced
	if the function does't have arguments, the view only will show a button for select a file to upload
'''
def index():
	DATA = request.args(0)
	if not DATA: return dict(status = None, data = None)
	PATH = request.env.web2py_path+'/applications/'+request.application+'/uploads/files.txt'
	DATA, REGISTERS, METRICS, STATUS = analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})

	if STATUS == "OK":
		return dict(data = DATA, metrics = METRICS, registers = REGISTERS, total = len(REGISTERS))
	else:
		return dict(status = STATUS, data = None)
	


def uploadFile():
	file = request.vars.file.file
	PATH = request.env.web2py_path+'/applications/'+request.application+'/uploads/files.txt'
	#now = datetime.now()
	#timestamp = datetime.timestamp(now)
	#filename=request.vars.file.filename

	STATUS = saveFileOnLocal(PATH, file)

	return response.json({'status': STATUS})
	
'''
Args:

Return:
	DATA							Will count the different coincidences arround the log file
	REGISTERS						Save all the registers of the file and asign a index in the same order of has read
	METRICS							Defined for different specific metrics calculated in analysis loop
'''
def analyceLogFile(PATH, DATA, REGISTERS, METRICS):
	file = open(PATH, 'r')
	fieldLine = file.readlines()

	'''
		This loop convert the second line of the log file in the keys of DATA dictionary,
		then, colums will have the fiels name in order to be called with the index in order of aparition
	'''

	if not "#Fields:" in fieldLine[1]:
		return (None, None, None, "NO_VALID_FILE")

	DATA = {item:dict() for item in fieldLine[1][len("#Fields:")+1:].split(" ")}
	colums = list(DATA.keys())

	for nLine, line in enumerate(fieldLine[2:]):
		line = line.replace('\n', '').split("\t")

		if not len(line) == len(colums):
			return (None, None, None, "COLUMS_SIZE_NOT_MATCH")

		for index, item in enumerate(line):
			if item == "-": item = "Undefined"
			REGISTERS[nLine] = line
			if not item in DATA[colums[index]]: DATA[colums[index]][item] = []
			DATA[colums[index]][item].append(nLine)
			if colums[index] == 'x-edge-result-type' and not line[31] == '-':
				if not item in METRICS['HitMisBytes']: METRICS['HitMisBytes'][item] = 0
				METRICS['HitMisBytes'][item] += int(line[31])
			

	METRICS['successFailed'] = {item:len(DATA['sc-status'][item]) for item in DATA['sc-status']}

	METRICS['bytesChange'] = [(REGISTERS[item][1], REGISTERS[item][3], REGISTERS[item][4]) for item in REGISTERS]
	METRICS['bytesChange'].sort(key=lambda x: x[0])

	METRICS['timeTaken'] = [(REGISTERS[item][1], REGISTERS[item][18], REGISTERS[item][4]) for item in REGISTERS]
	METRICS['timeTaken'].sort(key=lambda x: x[0])

	METRICS['ipUse'] = [(item, len(DATA['c-ip'][item])) if len(DATA['c-ip'][item]) > 20 else (0, 0,) for item in DATA['c-ip']]
	METRICS['ipUse'].sort(key=lambda x: x[1])

	METRICS['contentType'] = [(item, len(DATA['sc-content-type'][item])) for item in DATA['sc-content-type']]
	METRICS['contentType'].sort(key=lambda x: x[1])
	METRICS['edgeLocation'] = [(item, len(DATA['x-edge-location'][item])) for item in DATA['x-edge-location']]
	METRICS['edgeLocation'].sort(key=lambda x: x[1])
	METRICS['resultType'] = [(item, len(DATA['x-edge-result-type'][item])) for item in DATA['x-edge-result-type']]
	METRICS['resultType'].sort(key=lambda x: x[1])
	METRICS['csMethod'] = [(item, len(DATA['cs-protocol-version'][item])) for item in DATA['cs-protocol-version']]
	METRICS['csMethod'].sort(key=lambda x: x[1])

	return (DATA, REGISTERS, METRICS, "OK")


def saveFileOnLocal(PATH, file):

	try:
		copyFile = open(PATH,'wb+')
		shutil.copyfileobj(file, copyFile)
		copyFile.close()
	except Exception as e:
		return str(e)

	#session.flash = "File uploaded"
	return "OK"