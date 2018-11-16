# from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Entry(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     slug = models.SlugField(editable=False)

#     def __unicode__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.title)
#         super(Entry, self).save(*args, **kwargs)

# new comment to show in github

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

        # def fill_basic_info(key_array):
        #     p = {}
        #     for k in key_array:
        #         p[k] = self.json_full_info[k]

        #     self.json_basic_info = p


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

        # def __unicode__(self):
        #     return self.brand + " " + self.model + " $ " + self.price + " " + self.milleageKM + " KM"

        def __str__(self):
            return self.brand + " " + self.model + " $" + str(self.price) + "-" + str(self.milleageKM) + "KM"

class Favorite(models.Model):
        id_prod =   models.CharField(max_length=50)
        # owner =     models.ForeignKey(User, blank=True, null = True)
        username =   models.CharField(max_length=20, blank=True)

        def __str__(self):
            return self.id_prod + ' ' + self.username

