from forms import ValidForm

username = 'John'
message = 'Our best bargains for only 1.99 p'
sender = 'crazydog@yahoo.com'
flag = True

data = { 'username' : username, 'message' : message, 'sender' : sender, 'flag': flag }

f = ValidForm(data)
f.is_valid()

data = { 'username' : username, 'message' : message, 'sender' : 'crazycat.yahoo' , 'flag': flag }
f2 = ValidForm(data)

print(f2.errors)




