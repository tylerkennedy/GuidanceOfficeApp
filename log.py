#!/usr/bin/env python

import datetime
import time

def logSent(emailaddress, subject):
	date = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
	logs = open("/Users/tylerkennedy/Documents/GitHub/GuidanceOfficeApp/logs.txt", "a")
	logs.write("Mail SUCCESSFULLY sent to " + " (" + emailaddress + "), at " + date + " with (" + subject + ")\n")
	logs.close()


def logFailed(emailaddress, subject):
	date = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
	logs = open("/Users/tylerkennedy/Documents/GitHub/GuidanceOfficeApp/logs.txt", "a")
	logs.write("Mail UNSUCCESSFULLY sent to " + " (" + emailaddress + "), at " + date + " with (" + subject + ")\n")
	logs.close()
	
	