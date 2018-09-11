#!/usr/bin/env python


templatePath = ""
def getTemplatePath(tp):

	global templatePath

	templatePath = tp
	
	
templateDictionary = {}
def makeTemplateDictionary(n, l):

	global templateDictionary
	
	templateDictionary = {'name': n, 'link': l}


def makeTemplate():


	with open(templatePath) as f:
		lines = f.readlines()

	template = ""
	
	
	keys = templateDictionary
	for line in lines:
		
		for key in keys:
			
			if line.find("{" + key + "}") != -1:
				#print ' Replace' + line
			
			
				line = line.format(**keys)
				#print line
				
		template = template + line
	
	#print template	
	return template
	
	






