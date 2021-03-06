import sys
import shlex
import os
#import constants
from Carapace.constants import *

# Import all built-in function references
from Carapace.builtins import *


# Hash map to store built-in function name and reference as key and value
bulit_in_cmds = {}

# Register a built-in function to built-in command hash map
def register_command(name,func) :
	bulit_in_cmds[name] = func

# Register all built-in commands here
def init() :
	register_command("cd",cd)
	register_command("exit", exit)
	register_command("history",history)
	register_command("prev",prev)

def shell_loop() :
	status = SHELL_STATUS_RUN

	flag = 1
	while status == SHELL_STATUS_RUN :
		#For Displaying the command prompt
		if flag == 1 :
			sys.stdout.write("Welcome to Carapace!\n Type prev <line_num> to view the line_num th previous command.\n All standard unix commands are available.\n")
			flag =0

		sys.stdout.write('>')
		sys.stdout.flush()

		#Read the command input
		cmd = sys.stdin.readline()



		#Tokenise the command input
		cmd_tokens = tokenize(cmd)

		#Execute the command and get status
		status = execute(cmd_tokens)

def main() :
	init()
	shell_loop()

def tokenize(string) :
	return shlex.split(string)


def execute(cmd_tokens):
	#To write the history into a file
	with open(HISTORY_PATH, 'a') as history_file :
		history_file.write(' '.join(cmd_tokens) + os.linesep)
	#Extract the command name and arguments from the tokens
	cmd_name = cmd_tokens[0]
	cmd_args = cmd_tokens[1:]

	#If the command is bulit in command invoke it with its arguments
	if cmd_name in bulit_in_cmds:
		return bulit_in_cmds[cmd_name](cmd_args)

	#Fork a child shell process
	#Child process pid will be set to 0
	#Otherwise the current process is parent and it's pid is
	#the process of id of it's child
	pid = os.fork()

	if pid ==0 :
		#child process
		#replace the child shell process with the program called with exec
		os.execvp(cmd_tokens[0],cmd_tokens)

	elif pid > 0 :
		#parent process
		while True :
		#wait for the response status of it's child process
		#It returns the id and status of waiting process
			wpid,status = os.waitpid(pid,0)

			#finish waiting if the child process exits nomally or
			#terminated by signal
			if os.WIFEXITED(status) or os.WIFISIGNALED(status) :
				break

	#Return status indicating to wait for next command in shell_loop
	return SHELL_STATUS_RUN

if __name__ == "__main__" :
	main()

