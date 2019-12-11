# from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


class Seller(models.Model):
        name =      models.CharField(max_length=20, blank=True)
        phone =     models.CharField(max_length=20, blank=True)
        location =  models.CharField(max_length=200, blank = True)

        def __unicode__(self):
            return self.name

        def __str__(self):
            return self.name

class ProdJSON(models.Model):
        json_full_info =    models.TextField(blank=True)
        json_basic_info =   models.TextField(blank=True)
        url =               models.URLField(blank=True)
        created_at =        models.DateTimeField(auto_now_add=True)
        deleted_at =        models.DateTimeField(auto_now_add=True)
        active =            models.BooleanField(default=True)
        searchable_words =  models.TextField(blank=True)

class Car(models.Model):
        brand =         models.CharField(max_length=50)        #Subaru
        model =         models.CharField(max_length=50,blank=True)        # Legacy
        generation =    models.CharField(max_length=50,blank=True)   # Legacy V Station Wagon
        url =           models.URLField(blank=True)
        phone =         models.CharField(max_length=20, blank=True)
        engineDisplacement =    models.CharField(max_length=5,blank=True) # 2.2
        created_at =            models.DateTimeField(auto_now_add=True)
        updated_at =            models.DateTimeField(auto_now=True)
        fuel_type =             models.CharField(max_length=10, blank=True)
        seler_description =     models.TextField(blank=True)
        version =               models.CharField(max_length=60,blank=True)  # hatchback pack full
        doors =      models.PositiveIntegerField(null=True)
        power =      models.PositiveIntegerField(null=True)                         # 125 HP
        price =      models.PositiveIntegerField()
        year =       models.PositiveIntegerField(null=True)
        milleageKM = models.PositiveIntegerField(null=True)
        seller =      models.ForeignKey(Seller, blank=True, null = True,  on_delete=models.CASCADE)

        json_rep =  models.TextField(blank=True)

        def __str__(self):
            return self.brand + " " + self.model + " $" + str(self.price) + "-" + str(self.milleageKM) + "KM"

class Favorite(models.Model):
        id_prod =   models.CharField(max_length=50)
        # owner =     models.ForeignKey(User, blank=True, null = True)
        username =   models.CharField(max_length=20, blank=True)

        def __str__(self):
            return self.id_prod + ' ' + self.username

class Product(models.Model):

        # product_id = models.CharField(max_length=50)
        name =        models.CharField(max_length=50)
        description = models.CharField(max_length=50,blank=True)
        # price =    models.PositiveIntegerField()
        # discounted_price = models.PositiveIntegerField()
        # display = models.BooleanField(default=True)
        # image = models.URLField(blank=True)
        photo = models.ImageField(upload_to='cars', default = 'foto.jpg')

        # def show_photo(self):
        #     return format_html('<img src={} style="height:100px;">', self.url)

        # def __str__(self):
        #     return self.name + " " + self.description + " $" + str(self.price) + "-" + str(self.image) + "KM"

        def __str__(self):
            return self.name + " " + self.description

