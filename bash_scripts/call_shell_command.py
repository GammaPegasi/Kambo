import os

searchKey = 'view'
# command = 'find /home/kambo/mysite -name *' +  + '*.*'

command =  'grep -rnw \'/home/kambo/mysite\' -e \'import\''

out = os.popen(command).readlines()
for ln in out:

    if (len(ln) < 100):
        print(ln)