import os

'grep -r -i -n "return self.title" ./'

search_key = "url"
# command = 'find ./home/kambo/mysite/ -name *' + search_key + '*.*'
command = 'find . -name *' + search_key + '*.*'

command = 'grep -r -i -n "car.brand =" ./'

out = os.popen(command).readlines()

for elem in out:
    print(elem)

# print()
print(out)
