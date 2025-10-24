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
            # This checks if the line starts with a '#' to skip comment lines.
            match = re.match("^#", line)

            # Split line into fields using ':' as the delimiter.
            fields = line.strip().split(':')

            # If it's a comment line or the line doesn't have 5 fields, skip it.
            if match or len(fields) != 5:
                continue

            # Extract user info from fields.
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])

            # Split groups into a list.
            groups = fields[4].split(',')

            # Show account creation message.
            print(f"==> Creating account for {username}...")

            # Build and run adduser command.
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            os.system(cmd)

            # Show password message and set password.
            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            os.system(cmd)

            # Add user to groups if not '-'.
            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"
                    os.system(cmd)

    elif ans == "Y":
        for line in sys.stdin:
            # Dry-run mode: print what would be done instead of executing it.
            match = re.match("^#", line)
            print(match)

            fields = line.strip().split(':')
            print(fields)

            if match or len(fields) != 5:
                continue

            username = fields[0]
            password = fields[1]
            print(username, " ", password)
            gecos = "%s %s,,," % (fields[3], fields[2])
            print(gecos)

            groups = fields[4].split(',')
            print(groups)

            print(f"==> Creating account for {username}...")
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            # os.system(cmd)  # Commented out for dry-run

            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            # os.system(cmd)  # Commented out for dry-run

            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"
                    # os.system(cmd)

    print()
    print()
if __name__ == '__main__':
    main()
