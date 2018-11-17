from django.test import Client
import urllib

c = Client()

print('TEST UNIT ')
response = c.post('/admin/', {'username': 'jane', 'password': 'janejane'})


# response = c.post('/login/', {'username': 'john', 'password': 'smith'})
# response = c.post('/list_cars_json')

# response = c.get('/loginForm/', secure=True)
# print (response.status_code )
# print(response.content)
# print()

# response = c.get('/list_cars_json/', secure=True)
# print (response.status_code )
# print(response.content)
# print()

# response = c.get('/popover/', secure=True)
# print (response.status_code )
# print(response.content)
# print()


