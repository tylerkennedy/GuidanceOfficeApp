#!/usr/bin/env python

#import pg
import mailer
import templater

class task:
	
	def __init__(self, eaddress, name, subject, level, accountType, templatePath, link):	
		self.eaddress = eaddress
		self.name = name
		self.subject = subject
		self.level = level
		self.accountType = accountType
		self.templatePath = templatePath
		self.link = link

def getTasks():
	#Query through database
	#Create a table of all emails('tasks') that need to be sent today
	#For each row in temporary table create a new task object, fill in the attributes
	#List of objects with attributes of: email address, name, subject, level, account type, template path, link

	tasks = []
	
	tasks = [task("kennedytyler25@icloud.com", "Tyler", "Test Email Sent from Python", 1, "Tyler's Mac", "/Users/tylerkennedy/Documents/GitHub/GuidanceOfficeApp/guidanceTest.txt", "None")]
	return tasks
	
	
###################################################################################################################################	
	
	
""" Get input for the server object"""
def getServerAddress():
	#Encrypted text file
	address = ""

	return address


def getServerPort():	
	#Encrypted text file
	port = 0

	return port

count = 1
def getServerUsername():	
	#Encrypted text file
	global count
	
	username = ""
	count = count + 1
	
	return username


def getServerPassword():	
	#Encrypted text file
	password = ""

	return password
	
	
"""Get input for template method"""

""" Get input for the email object """
	
""" Call this function every time new server input is needed"""
def serverInput():
	mailer.theServerAddress(getServerAddress())
	mailer.theServerPort(getServerPort())
	mailer.theServerUsername(getServerUsername())
	mailer.theServerPassword(getServerPassword())

""" Call this function every time new template input is needed"""	
def templateInput(templatePath, name, link):
	templater.getTemplatePath(templatePath)
	templater.makeTemplateDictionary(name, link)
	
""" Call this function every time new email input is needed"""
def emailInput(eaddress, accountType, subject):
	mailer.theRecipient(eaddress)
	mailer.theSender(accountType)
	mailer.theSubject(subject)
	mailer.theTemplate(templater.makeTemplate())
		
		
