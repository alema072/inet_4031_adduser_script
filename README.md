# INET4031 Add Users Script and User List

## Program Description
 
In this program, it is able to automate the creation of users. The way it is able to do this is by taking in a file, in this case, 'create-users.input' and it will create the users based on the data in that file.  Normally to add a user, the command 'sudo adduser user01' would be used to add the user, with a list of information that would need inputting by the user. But this program will relpace the manual need of that. Instead with the files in this program, using 'sudo ./create-users.py < create-users.input' will create the users based on the users and its information in the input file. The Python file is able to store commands that would be used to execute in the command line to create the user itself, rather than the user having to input it.

## Program User Description


### Input File Format

There is a input file that is used to hold data about the users and will be used to create them in the Python file. It is a text file that has to have this format: user##:pass##:Last##:First##:group##. Each field represents the data of the user; username, password, first name, last name, and the group to be assigned. If a line should be skipped, make sure to put a '#' at the start of that line to comment it out and skip to the next line. The last part, which is the group, is optional and can be replaced with a '-' to represent no group assignment for that user.

### Command Execution

In order to run the code, use this in the command line, './create-users.py < create-users.input' The reason this works is because '<' redirects the contents of 'create-users.input' into the program’s standard input, and './create-users.py' reads those lines using 'sys.stdin.'

### Dry-Run

If a user chooses to do a dry-run, then all the 'os.system(cmd)' lines will be commented out and only print statements will run to see a simulation of the users that would be cretaed. It is more a like a test run to see if things are working correctly before the execution is actually done.


