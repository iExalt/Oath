import sys
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

command = 'ansible-playbook -e "host_key_checking=False ansible_python_interpreter=/usr/bin/python3 ansible_ssh_common_args=\'-o StrictHostKeyChecking=no\'"  dev_env.yaml -i "{0}," -u {1} --ask-become-pass'

if (len(sys.argv) < 2):
    print("Not enough arguments!")
    sys.exit(1)

for i in range(2, len(sys.argv)):
    print(command.format(sys.argv[i], sys.argv[1]))
    os.system(command.format(sys.argv[i], sys.argv[1]))
    #os.system(command.replace("$REPLACE", sys.argv[i]))
