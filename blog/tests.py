from django.test import TestCase

from blog.models import Favorite

from django.test import Client


from django.contrib.auth.models import User



print('\nTEST UNIT django.test ****\n ')

class FavoriteTestCase2(TestCase):

    def setUp(self):
       # f1 = Favorite.objects.create(id_prod="123", username="johnny")
       # f2 = Favorite.objects.create(id_prod="124", username="juan")
       self.user = User.objects.create(username="johnny", password='secret'   )
       # f1.save()
       # f2.save()
     
    def test_log_in(self):
        print("test_log_in")
        """User created and logged in !!! """
        c = Client()
        response = c.post('/loginForm/', {'username': 'johnny', 'password': 'secret'})
        # response = c.get('/find_files/')
        # print('RESPONSE ********* ', response.content.__str__())
        self.assertEqual('<!DOCTYPE html>' in response.content.__str__(), True)
           
  
    def test_versions(self):
        """ Test versions """
        print("\ntest_versions")
        c = Client()
        
        # response = c.post('/loginForm/', {'username': self.user.username, 'password': 'JOHNNY_123johnny'})

        c.login(username='johnny', password='secret')

        response = c.get('/version/')
        # response = c.get('/loginForm/')

        print('RESPONSE version ********* ', response.content.__str__())
        print('RESPONSE get ********* ', response.get)
        
        # self.assertEqual('3.6.0' in response.content.__str__(), True)



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'johnny',
            'password': 'secret'}
        u = User.objects.create_user(**self.credentials)
        u.save()
    
    # def test_login(self):
    #     # send login data
    #     # response = self.client.post('/admin/login/?next=/admin/', self.credentials, follow=True)
    #     response = self.client.post('/admin/', self.credentials, follow=True)
    #     # response = self.client.post('/loginForm/', self.credentials, follow=True)
    #     # should be logged in now
    #     self.assertTrue(response.context['user'].is_active)




        
