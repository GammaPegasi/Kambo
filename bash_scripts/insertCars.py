import random
from blog.models import Car

for x in range(0, 10):

    rans =  str(round (random.random(), 5))
    car = Car()
    # car.brand = "Brand" + rans
    # car.model = "Model"+rans
    car.brand = "BMW"
    car.model = "320"
    car.generation = "80" +rans
    car.year = 2011
    # car.milleageKM = 120500
    car.url = "www.cartromba.com"
    car.phone = "598 987 456 321"
    car.doors = 5
    car.power = 136
    car.engineDisplacement =  "2.2"
    car.price =  10500

    car.save()

    # brand = models.CharField(max_length=50)        #Subaru
    # model = models.CharField(max_length=50)        # Legacy
    # generation = models.CharField(max_length=50)   # Legacy V Station Wagon
    # year = models.PositiveSmallIntegerField()
    # milleageKM = models.PositiveIntegerField()
    # url = models.URLField()
    # phone = models.CharField(max_length=20)
    # doors = models.IntegerField()
    # power = models.IntegerField()                         # 125 HP
    # engineDisplacement = models.CharField(max_length=5) # 2.2
    # datePost = models.DateField(auto_now_add=True)

    print(car.brand, car.model)

