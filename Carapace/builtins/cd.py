import os
from Carapace.constants import *

def cd(args) :
	#changes the current working directory of the calling process
	#to the directory specified in the path
	os.chdir(args[0])

	return SHELL_STATUS_RUN

