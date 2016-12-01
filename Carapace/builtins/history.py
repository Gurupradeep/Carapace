import os
import sys
from Carapace.constants import *


def history(args) :
	with open(HISTORY_PATH,'r') as history_file :
		lines = history_file.readlines()


	#set default limit as whole file
	limit = len(lines)

	#setting user given limit
	if len(args) > 0 :
		limit = int(args[0])

	#get the starting line for output	
	start = len(lines) - limit

	for line_no, line in enumerate(lines) :
		if(line_no) >= start :
			sys.stdout.write('%d %s' %(line_no + 1, line))
	sys.stdout.flush()

	return SHELL_STATUS_RUN 