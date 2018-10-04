import cgitb
import cgi
cgitb.enable()

import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate






print "Content-Type: text/html"  
print 

print "<TITLE>CGI script output</TITLE>"
print "<H1>This is my first CGI script</H1>"
print "Hello, world!"


##########################################################################################


""" Define email class and methods to get input"""
class server:
	
	def __init__(self, address, port, username, password):	
		self.address = address
		self.port = port
		self.username = username
		self.password = password
		
serverAddress = ""
def theServerAddress(sa):
	
	global serverAddress
	
	serverAddress = sa
	
serverPort = 0
def theServerPort(sp):	
	
	global serverPort
	
	serverPort = sp


serverUsername = ""
def theServerUsername(su):

	global serverUsername
	
	serverUsername = su
	

serverPassword = ""
def theServerPassword(sp):
	
	global serverPassword
	
	serverPassword = sp


""" Define email class and methods to get input"""	
class email:

	def __init__(self, to, fromm, subject):
		self.to = to
		self.fromm = fromm
		self.subject = subject
		
		
	
recipient = ""
def theRecipient(rec):
	
	global recipient
	
	recipient = rec
	

sender = ""
def theSender(sen):
	

	global sender
	sender = sen
	sender = sender + ' ' + '<' + serverUsername + '>'
	return sender		

subject = ""	
def theSubject(sub):

	global subject
	
	subject = sub
	
	

	

def createMessage():
	
	mail = email(recipient, sender, subject)	
		
	msg = MIMEMultipart()
	
	msg['To'] = mail.to
	msg['From'] = mail.fromm
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = mail.subject
	
	
	
	
	return msg.as_string()
	
		
def mailIt():
	#global s
	
	
	try:
		s = server(serverAddress, serverPort, serverUsername, serverPassword)
		myserver = smtplib.SMTP_SSL(s.address, s.port)
		myserver.connect(s.address, s.port)
		myserver.ehlo()
		myserver.login(s.username, s.password)
	
		myserver.sendmail(serverUsername, recipient, createMessage())

		myserver.quit()


		print "Mail sent"
		
	except:
		print "Could not connect to server"
		

	

	
	
##########################################################################################

	
	
	
	
	
##########################################################################################


class task:
	
	def __init__(self, eaddress, name, subject, level, accountType, link):	
		self.eaddress = eaddress
		self.name = name
		self.subject = subject
		self.level = level
		self.accountType = accountType
		
		self.link = link

def getTasks():
	#Query through database
	#Create a table of all emails('tasks') that need to be sent today
	#For each row in temporary table create a new task object, fill in the attributes
	#List of objects with attributes of: email address, name, subject, level, account type, template path, link
	
	form = cgi.FieldStorage()
	
	name = "Appointment for " + form["firstname"].value + " " + form["lastname"].value
		
	tasks = []
	
	tasks = [task("kennedytyler25@icloud.com", "Tyler", name, 1, "Tyler's Mac", "None")]
	return tasks
	
	
	
	
""" Get input for the server object"""
def getServerAddress():
	#Encrypted text file
	address = "smtpout.secureserver.net"

	return address


def getServerPort():	
	#Encrypted text file
	port = 465

	return port

count = 1
def getServerUsername():	
	#Encrypted text file
	global count
	
	username = "tyler@kennedy-csg.com"
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
	theServerAddress(getServerAddress())
	theServerPort(getServerPort())
	theServerUsername(getServerUsername())
	theServerPassword(getServerPassword())

""" Call this function every time new template input is needed"""	

	
""" Call this function every time new email input is needed"""
def emailInput(eaddress, accountType, subject):
	theRecipient(eaddress)
	theSender(accountType)
	theSubject(subject)
	
		
		
##########################################################################################


def main():
	for task in getTasks():
		serverInput()
		emailInput(task.eaddress, task.accountType, task.subject)
		mailIt()
		print "*We are trying to send mail as of right now*"
		

main()	


