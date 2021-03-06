
import re

from word import doc2text

def procResume (f):

	text = doc2text.process(f)

	'''
	with open('demofile.txt','r') as f:
		content = f.read().lower().replace('\n',' ')
		'''

	sections =['address','professional experience', 'experience summary','education', 
				'certificate','major projects','award','training', 'technical skills']

	content =text.lower().replace('\n',' ')

	for sec in sections:
		rstr='\n'+sec
		content = content.replace(sec,rstr,1)
		


	dictPtrn = { 'name':r'Tushar\s\w+', 
				 'phone':r'\+\d+.\d+', 
				 'email':r'\w+@\w+\.\w+',
				 'address':r'address:.*',
				 'experience summary':r'experience summary.*',
				 'professional experience':r'professional experience.*',
				 'education':r'education.*',
				 'award':r'award.*',
				 'skills':r'skills.*',
				 'training':r'training.*',
				 'major projects':'major projects.*'

				 }

	dictData ={}

			
	for key, value in dictPtrn.items() :

		srtPat=value

		pattern = re.compile(srtPat, re.IGNORECASE)

		matches = pattern.finditer(content)

		lMatch=[]

		s=''

		for match in matches:
			m=match[0]
			if(m not in lMatch) :
				m=m.replace(key,'')
				lMatch.append(m)
				s=s+m+', '

		s=s[:-1]				

		dictData[key]=s

	return dictData




def handle_uploaded_file(f):
	print(f)
	with open('resume.docx', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)



 
            
