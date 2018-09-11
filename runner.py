#!/usr/bin/env python

import input
import templater
import mailer
import time
import log


def main():
	for task in input.getTasks():
		input.serverInput()
		input.templateInput(task.templatePath, task.name, task.link)
		input.emailInput(task.eaddress, task.accountType, task.subject)
		mailer.mailIt()
		#output.updateTime()
		

main()	

