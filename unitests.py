from controllers import app
import os.path

'''
	Sample of error file, the Field data starts in line 0 instead of 1
'''

PATH = 'uploads/ErrorSampleFile-1.txt'
DATA, REGISTERS, METRICS, STATUS = app.analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})
assert "NO_VALID_FILE" == STATUS 
assert None == DATA 
assert None == REGISTERS 
assert None == METRICS 


'''
	Verification of existing file with analysis and comparation of metrics
'''

PATH = 'uploads/SampleFile-1.txt'
DATA, REGISTERS, METRICS, STATUS = app.analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})


assert "OK" == STATUS 
assert 6185 == len(REGISTERS)
assert 33 	== len(DATA)
assert 'successFailed' 	in METRICS
assert 'bytesChange' 	in METRICS
assert 'contentType' 	in METRICS
assert 'timeTaken' 		in METRICS
assert 'ipUse' 			in METRICS
assert len(REGISTERS)-1 in REGISTERS


'''
	Simulation of complete proccess, uploading a log file and making an analysis
'''

PATH = 'uploads/SampleUpload-1.txt'

file = open("uploads/TMP-1.txt", "w")
file.write("#Version: 1.0\n")
file.write("#Fields: date time x-edge-location sc-bytes c-ip cs-method cs(Host) cs-uri-stem sc-status cs(Referer) cs(User-Agent) cs-uri-query cs(Cookie) x-edge-result-type x-edge-request-id x-host-header cs-protocol cs-bytes time-taken x-forwarded-for ssl-protocol ssl-cipher x-edge-response-result-type cs-protocol-version fle-status fle-encrypted-fields c-port time-to-first-byte x-edge-detailed-result-type sc-content-type sc-content-len sc-range-start sc-range-end\n")
file.write("020-06-14	23:02:59	LAX50-C1	51988	189.165.30.205	GET	dummy.cloudfront.net	/FnY3kxaDE68pEaZq4dWeEFYC5pPMWnh5/1/dash/1_audio_1_1_1056.mp4	200	-	com.dla.android/548v1%20(Linux;Android%207.1.2)%20ExoPlayerLib/2.10.6	m=1547524403	-	Hit	UXQNaz0czh0zs-pu1XRN6UbJHTjyIHYJu5MEh7dx6xBuAn_ua6YgQA==	sample.bc.com	https	286	0.029	-	TLSv1.2	ECDHE-RSA-AES128-GCM-SHA256	Hit	HTTP/1.1	-	-	42422	0.029	Hit	-	51400	-	-\n")
file.close()

file = open("uploads/TMP-1.txt", "rb")
STATUS = app.saveFileOnLocal(PATH, file)
assert "OK" == STATUS 

DATA, REGISTERS, METRICS, STATUS = app.analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})

assert "OK" == STATUS 
assert 1 == len(REGISTERS)
assert 33 	== len(DATA)
assert 'successFailed' 	in METRICS
assert 'bytesChange' 	in METRICS
assert 'contentType' 	in METRICS
assert 'timeTaken' 		in METRICS
assert 'ipUse' 			in METRICS
assert len(REGISTERS)-1 in REGISTERS


'''
	Adding a wrong line to existing log file and detecting the status error
'''


file = open(PATH, "a")
file.write("2020-06-14	LAX50-C1	51988	189.165.30.205	GET	dummy.cloudfront.net	/FnY3kxaDE68pEaZq4dWeEFYC5pPMWnh5/1/dash/1_audio_1_1_1056.mp4	200	-	com.dla.android/548v1%20(Linux;Android%207.1.2)%20ExoPlayerLib/2.10.6	m=1547524403	-	Hit	UXQNaz0czh0zs-pu1XRN6UbJHTjyIHYJu5MEh7dx6xBuAn_ua6YgQA==	sample.bc.com	https	286	0.029	-	TLSv1.2	ECDHE-RSA-AES128-GCM-SHA256	Hit	HTTP/1.1	-	-	42422	0.029	Hit	-	51400	-	-\n")
file.close()

DATA, REGISTERS, METRICS, STATUS = app.analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})

assert "COLUMS_SIZE_NOT_MATCH" == STATUS

#if os.path.exists(PATH): os.remove(PATH)
#if os.path.exists('uploads/TMP-1.txt'): os.remove(PATH)