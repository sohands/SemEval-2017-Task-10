import os

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

def createEvaluationFiles(lines,ann,name):
	i=0
	new_ann=[]
	correct=0
	total=0
	classified_count=0
	for t in ann:
		words=t[4].split()
		votes={}
		for w in words:
			line=lines[i].strip()
			if len(line.strip())<=0:continue
			line_split=line.split()
			if line_split[2]!=w:print line_split;continue
			tag=line_split[-1]
			if tag not in votes:
				votes[tag]=0
			votes[tag]+=1
			i+=1
		max_vote_tag=None
		for tag in votes:
			if max_vote_tag==None or votes[tag]>votes[max_vote_tag]:
				max_vote_tag=tag
		total+=1
		if max_vote_tag==None:continue
		if max_vote_tag==t[1]:correct+=1
		classified_count+=1
		new_ann.append((t[0],max_vote_tag,t[2],t[3],t[4]))
	f=open(name+'.ann','w')
	for t in new_ann:
		print t
		line=str(t[0])+'\t'+str(t[1])+' '+str(t[2])+' '+str(t[3])+'\t'+t[4]+'\n'
		f.write(line)
	f.close()
	return correct,total,classified_count

os.chdir('Test_Out')
files=os.listdir('.')
filenames=set()
for name in files:
	filenames.add(name[:name.index('.')])
total_p_n=0
total_p_d=0
total_r_d=0
for name in filenames:
	f=open(name+'.out','r')
	out_lines=f.readlines()
	f.close()
	if name[-1]=='b':continue
	f=open('..\\scienceie2017_dev\\dev\\'+name+'.ann','r')
	ann_lines=f.readlines()
	f.close()
	ann=processAnnLines(ann_lines)
	p_n,r_d,p_d=createEvaluationFiles(out_lines,ann,name)
	total_p_n+=p_n
	total_p_d+=p_d
	total_r_d+=r_d
	# print 'Done with',name,'Precision:',float(p_n)/p_d,'Recall:',float(p_n)/r_d
# print 'Precision:',float(total_p_n)/total_p_d,'Recall:',float(total_p_n)/total_r_d