from django.contrib.auth.models import User, Group
from blog.models import Car, ProdJSON, Favorite, Product

from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'url', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('pk', 'brand', 'model', 'generation', 'updated_at', 'price', 'year', 'json_rep')
        # , 'generation', 'url', 'phone', 'engineDisplacement', 'created_at', 'modified_at', 'price', 'year' )

class ProdJSONSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProdJSON
        fields = ('json_full_info', 'json_basic_info', 'url', 'created_at', 'deleted_at', 'active', 'searchable_words')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'username', 'id_prod')
        read_only_fields = ['id',]


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'photo')

