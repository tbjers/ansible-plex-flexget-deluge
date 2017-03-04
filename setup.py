"""
This script takes the user and host and runs an Ansible playbook.
"""

import argparse
import os
import subprocess
import re

if __name__ == "__main__":
    if not os.path.isfile("main.yml"):
        print "This must be run from the playbook root directory."
        exit(1)

    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("login", help="user@host to run on")

    ARGS = PARSER.parse_args()
    USER, HOST = re.match("(.+)@(.+)", ARGS.login).groups()

    with open("inventory", "w") as f:
        f.write(HOST)

    CMD = "ansible-playbook -u {user} -i inventory " + \
            "--ask-vault-pass --ask-sudo-pass main.yml"
    CMD = CMD.format(user=USER)
    try:
        subprocess.call(CMD.split())
    except KeyboardInterrupt:
        pass

    os.remove("inventory")
