from django.test import TestCase

from blog.models import Favorite


print('\n Favorite TEST  UNIT \n ')

class FavoriteTestCase2(TestCase):
    def setUp(self):
       Favorite.objects.create(id_prod="123", username="johnny")
       Favorite.objects.create(id_prod="124", username="juan")
       
    def test_animals_can_speak2(self):
        """Animals that can speak are correctly identified !!! """
        johnny = Favorite.objects.get(username="johnny")
        juan = Favorite.objects.get(username="juan")
        print('Animals	 TEST ')
        self.assertEqual(johnny.__str__(), '123 johnny22******')
        self.assertEqual(juan.__str__(), '124 juan')


