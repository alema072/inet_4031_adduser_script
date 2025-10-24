#!/usr/bin/python3

# INET4031
# Matthew Alemayehu
# 10/24/2025
# 10/24/2025

# import os allows running commands in the code.
# import re allows for text searching.
# import sys allows for reading input.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTOR'S COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():

    ans = input("Would you like to run the code in dry-run mode? (Y/N): ")

    if ans == "N":
        for line in sys.stdin:

        # This is scanning through the text to find a hashtag to see if its a comment. It is looking for a hashtag to discard creating them as a user.
        match = re.match("^#", line)

        # Split will create an array and split each string that has a colon in front of it and store that string as an element in the array. The array will be stored in the fields variable.
        fields = line.strip().split(':')

        # The IF statement is checking for two things to be true.
        # 1. That match has a value, which would be "#".
        # 2. Or IF the length of the array is not 5.
        # If either of the two is true, then it will hit the continue line, and skip this iteration.
        # If neither is true, then it is a valid input line and will create the user.
        if match or len(fields) != 5:
            continue

        # Stores the first and seconds element of fields array into username and password. This will store the full and last name.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        # This will split strings from the commas and store those strings as elements in an array stored by groups.
        groups = fields[4].split(',')

        # The print statement shows the creation of the user and that it is working.
        print("==> Creating account for %s..." % (username))

        # This will store the command that will be used to add a user.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # It should be commnted out the first time to dry-run the code.
        # Runs command to create the user
        os.system(cmd)

        # Print message about setting the user password
        print("==> Setting the password for %s..." % (username))

        # Stores Linux command to create user password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # The first time should be commneted out.
        # Command would set the password.
        os.system(cmd)

        for group in groups:
            # Checks if the current string being checked is not a dash.
            # If it does, then it is empty and it will skip.
            # If this does not have a dash, then there are groups for users to be added to.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print cmd
                os.system(cmd)

    elif ans == "Y":
        for line in sys.stdin:

        # This is scanning through the text to find a hashtag to see if its a comment. It is looking for a hashtag to discard creating them as a user.
        match = re.match("^#", line)
        print(match)

        # Split will create an array and split each string that has a colon in front of it and store that string as an element in the array. The array will be stored in the fields variable.
        fields = line.strip().split(':')
        print(fields)

        # The IF statement is checking for two things to be true.
        # 1. That match has a value, which would be "#".
        # 2. Or IF the length of the array is not 5.
        # If either of the two is true, then it will hit the continue line, and skip this iteration.
        # If neither is true, then it is a valid input line and will create the user.
        if match or len(fields) != 5:
            continue

        # Stores the first and seconds element of fields array into username and password. This will store the full and last name.
        username = fields[0]
        password = fields[1]
        print(username, " ", password)
        gecos = "%s %s,,," % (fields[3], fields[2])
        print(gecos)

        # This will split strings from the commas and store those strings as elements in an array stored by groups.
        groups = fields[4].split(',')
        print(groups)

        # The print statement shows the creation of the user and that it is working.
        print("==> Creating account for %s..." % (username))

        # This will store the command that will be used to add a user.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # It should be commnted out the first time to dry-run the code.
        # Runs command to create the user
        #os.system(cmd)

        # Print message about setting the user password
        print("==> Setting the password for %s..." % (username))

        # Stores Linux command to create user password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # The first time should be commneted out.
        # Command would set the password.
        #os.system(cmd)

        for group in groups:
            # Checks if the current string being checked is not a dash.
            # If it does, then it is empty and it will skip.
            # If this does not have a dash, then there are groups for users to be added to.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print cmd
                #os.system(cmd)

    print()
    print()
if __name__ == '__main__':
    main()
