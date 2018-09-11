#!/usr/bin/env python

import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import templater
import log


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

	def __init__(self, to, fromm, subject, template):
		self.to = to
		self.fromm = fromm
		self.subject = subject
		self.template = template
		
	
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
	
	
template = ""
def theTemplate(temp):

	global template

	template = temp
	

def createMessage():
	
	mail = email(recipient, sender, subject, template)	
		
	msg = MIMEMultipart()
	
	msg['To'] = mail.to
	msg['From'] = mail.fromm
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = mail.subject
	
	
	msg.attach(MIMEText(template, 'html'))
	
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
		log.logSent(recipient, subject)
	except:
		print "Could not connect to server"
		log.logFailed(recipient, subject)

	

	
	
	
	
	
	