import os

# os.chdir(r'scienceie2017_dev\dev')

files=os.listdir(r'scienceie2017_dev\dev')
filenames=set()
for name in files:
	filenames.add(name[:name.index('.')])

for name in filenames:
	os.system('"CRF++-0.58\\crf_test.exe" -m model_boundary.crf scienceie2017_dev\\dev\\'+name+'.ffb > Test_Out_Boundary\\'+name+'.out')
	# os.system('cp scienceie2017_dev\\dev\\'+name+'.ff Test_Out')
	print 'Done with',name