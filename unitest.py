from controllers import app

PATH = 'uploads/SampleFile-1.txt'

DATA, REGISTERS, METRICS = app.analyceLogFile(PATH, {}, {}, {'HitMisBytes': {}})

assert 6185 == len(REGISTERS)
