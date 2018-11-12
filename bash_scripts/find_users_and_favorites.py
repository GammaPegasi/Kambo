# from django.contrib.auth.models import User
from blog.models import Favorite
# import json

# alx = User.objects.all()[0]

# f_list = Favorite.objects.all()

newFav = Favorite(username = 'alex', id_prod ='TOYOTA_2345')
newFav.save()


fl = Favorite.objects.filter(username = 'alex', id_prod ='TOYOTA_2345')
for f in fl:
    print(' {} {}'.format( f.username, f.id_prod ) )

# fl = Favorite.objects.filter(username = 'alex')
#     print(' {} {}'.format( f.username, f.id_prod ) )


# print(' {} {}'.format( fl.username, fl.id_prod ) )
# f = Favorite.objects.all()[0]
# f = Favorite.objects.get()

# print(alx.username)
# print(f.user, f.json_favorite_ids)

# o = json.loads(f.json_favorite_ids)
# str = json.dumps(o)
# jo = json.loads(str)

# # fl = FavoriteList()
# # fl.user = alx
# # fl.save()

# fl = Favorite.objects.get(user = alx)
# fn = Favorite(lst = fl)
# fn.item = "ASA34"
# # fn.save()

# # fn = FavoriteList.objects.get(user = alx)
# f_list = Favorite.objects.all()


# nodes = FavoriteNode.objects.all()
# for n in nodes:
#     print(n)

# o['fav_list'].append("asdf")
# f.json_favorite_ids = str(o)
# f.save()

# print( '{}    {} '.format( o['fav_list'][0], o['fav_list'][1] ))


