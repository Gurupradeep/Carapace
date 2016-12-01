import os
import sys
from Carapace.constants import *


def prev(args) :
	with open(HISTORY_PATH,'r') as history_file :
		lines = history_file.readlines()


	#total no of commands in history
	total = len(lines)

	#The command which user wants from
	if len(args) > 0 :
		number = int(args[0])
		#exceeding the no of commands available
		if(number > total) :
			sys.stdout.write("Sorry history doesn't have that many commands\n")
			return SHELL_STATUS_RUN 
		else :
			req = total - number - 1
			for line_no, line in enumerate(lines) :
				if(line_no) == req :
					sys.stdout.write(line)
			sys.stdout.flush()
			return SHELL_STATUS_RUN 

	else :
		#invalid input
		sys.stdout.write("Enter a number(the command you want from last)\n")
		return SHELL_STATUS_RUN
     