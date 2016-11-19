import os
import re

def processAnnLines(lines):
	t=[]
	allowed=['Process','Task','Material']
	for line in lines:
		words=line.strip().split()
		if words[1] not in allowed:continue
		s=''
		for w in words[4:]:
			s+=w+' '
		s=s.strip()
		t.append((words[0],words[1],words[2],words[3],s))
	return t

def createEvaluationFiles(out_lines,txt_line,ann,name):
	key_phrases=[]
	words_indices=[(m.group(0), (m.start(), m.end()-1)) for m in re.finditer(r'\S+', txt_line)]
	words,indices=zip(*words_indices)
	# if name=="S0010938X13003818":print words_indices
	key_phrase=''
	key_phrase_started=False
	key_phrase_start_index=None
	for i in range(len(words)):
		output_splitted=out_lines[i].strip().split()
		if len(output_splitted)==0:continue
		if output_splitted[-1]=='1':
			key_phrase+=' '+words[i]
			if key_phrase_start_index is None:key_phrase_start_index=indices[i][0]
			key_phrase_started=True
			if words[i][-1]=='.' or words[i][-1]==',' or words[i][-1]==')':
				key_phrase=key_phrase[:-1]
				key_phrases.append((key_phrase.strip(),(key_phrase_start_index,indices[i][1])))
				key_phrase_started=False
				key_phrase_start_index=None
				key_phrase=''
			elif words[i][0]=='(':
				key_phrase=key_phrase[:len(' '+words[i])]
				key_phrases.append((key_phrase.strip(),(key_phrase_start_index,indices[i][1])))
				key_phrase_started=False
				key_phrase_start_index=None
				key_phrase=''
		else:
			if key_phrase_started==True:
				key_phrases.append((key_phrase.strip(),(key_phrase_start_index,indices[i-1][1])))
			key_phrase_started=False
			key_phrase_start_index=None
			key_phrase=''
	if key_phrase_started:key_phrases.append((key_phrase.strip(),(key_phrase_start_index,indices[-1][1])))
	for i in range(len(key_phrases)):
		kp=key_phrases[i]
		index=None
		for t in ann:
			if kp[0].strip()==t[4].strip():
				index=(int(t[2]),int(t[3]))
		if index is not None:
			key_phrases[i]=(kp[0],index)
	f=open(name+'.ann','w')
	for kp in key_phrases:
		line='-\t- '+str(kp[1][0])+' '+str(kp[1][1])+'\t'+kp[0]
		if kp[0][-1]=='.' or kp[0][-1]==',':
			line='-\t- '+str(kp[1][0])+' '+str(kp[1][1])+'\t'+kp[0][:-1]
		line=line.strip()+'\n'
		f.write(line)
	f.close()

os.chdir('Test_Out_Boundary')
files=os.listdir('.')
filenames=set()
for name in files:
	filenames.add(name[:name.index('.')])
for name in filenames:
	f=open(name+'.out','r')
	out_lines=f.readlines()
	f.close()
	f=open('..\\scienceie2017_dev\\dev\\'+name+'.ann','r')
	ann_lines=f.readlines()
	f.close()
	ann=processAnnLines(ann_lines)
	f=open('..\\scienceie2017_dev\\dev\\'+name+'.txt','r')
	txt_line=f.readlines()[0]
	f.close()
	createEvaluationFiles(out_lines,txt_line,ann,name)
	print 'Done with',name