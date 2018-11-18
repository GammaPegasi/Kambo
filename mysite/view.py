from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from blog.models import ProdJSON, Car, Favorite
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mysite.serializers import UserSerializer, GroupSerializer, CarSerializer, ProdJSONSerializer, FavoriteSerializer
from rest_framework import generics
from rest_framework import filters
from django.contrib.auth.decorators import login_required
import os
import pymongo
import re
from django.http import HttpResponseRedirect
from .forms import NameForm, ContactForm, ValidForm
from bson.json_util import dumps
import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# sys.path.insert(0,"/home/kambo/.local/lib/python2.7/site-packages/pymongo")

from django.contrib.auth import authenticate, login, logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/get_name/')

def validForm(request):
    if request.method == 'POST':
        form = ValidForm(request.POST)
        if form.is_valid():
            # userName = form.cleaned_data['username']
            # message = form.cleaned_data['message']
            return render(request, 'submitedData.html', {'formFields' : form.cleaned_data, 'extradata': form.data } )
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ValidForm(initial = { 'username': 'alexa' })

    return render(request, 'validForm.html', {'form': form })

def get_name(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=userName, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'thanks.html', {'formFields' : form.cleaned_data, 'repr' : form.data } )
            else:
                 # Return an 'invalid login' error message.
                return render(request, 'thanks.html', {'formFields' : form.cleaned_data, 'repr' : 'INVALID USER OR PASSWORD'  } )
            # return HttpResponseRedirect('/thanks/' + form.cleaned_data['message'])
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'loginForm.html', {'form': form })


def thanks(request):
  return render(request, 'thanks.html')

def submitedData(request):
  return render(request, 'submitedData.html')

@login_required(login_url='/loginForm/', redirect_field_name='salvattore')
def salvattore(request):
   return render(request, 'salvattore.html')

@login_required(login_url='/loginForm/')
def newspaper(request):
   return render(request, 'newspaper.html')


@login_required(login_url='/loginForm/')
def camera(request ):
   return render(request, 'camera.html')

@login_required(login_url='/loginForm/')
def view_mongo(request, searchKey ):
    client = pymongo.MongoClient('mongodb://hora:hora@ds111798.mlab.com:11798/timestamps')
    db = client.timestamps
    collection = db.items
    query = {"title": re.compile(searchKey, re.IGNORECASE) }
    docs = dumps( collection.find(query).skip(0).limit(5) )
    # return JsonResponse(obj, safe=False)
    logging.info(docs)
    return HttpResponse(docs, content_type='application/json', )


@login_required(login_url='/loginForm/')
def mongo_quick_search(request, searchKey):
    client = pymongo.MongoClient('mongodb://hora:hora@ds111798.mlab.com:11798/timestamps')
    db = client.timestamps
    query = {"title": re.compile(searchKey, re.IGNORECASE) }
    size = db.items.count(query)
    # docs = dumps( db.items.find(query).skip(0).limit(120) )
    docs = dumps( db.vehicles.find(query).skip(0).limit(120) )

    # docs['size'] = size
    # obj = {'size': size, 'data': docs}
    response = HttpResponse(docs, content_type='application/json')
    response['size'] = size
    return response


@login_required(login_url='/loginForm/')
# def mongo_js(request, searchKey):
def mongo_js(request ):
    client = pymongo.MongoClient('mongodb://hora:hora@ds111798.mlab.com:11798/timestamps')
    db = client.timestamps
    collection = db.items
    docs = dumps( collection.find().skip(0).limit(120) )
    return HttpResponse(docs, content_type='application/json')

    # client = pymongo.MongoClient('mongodb://hora:hora@ds111798.mlab.com:11798/timestamps', connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)
    # db = client.get_database('items')
    # json.loads](str( page.fetch()  ))
    # cursor  = db.items.find( { 'price': { '$gt': 5000, '$lt': 5500 } }).skip(0).limit(25)

@login_required(login_url='/loginForm/')
def send_retrieve_favorite(request):
   return render(request, 'send_retrieve_favorite.html', { 'user' : 'alex'} )

# @login_required(login_url='/loginForm/')
# def json_favorites_post(request, id_prod):
#     #alx = User.objects.all()[0]
#     f = Favo.objects.get(user = request.user)
#     o = json.loads(f.json_favorite_ids)
#     o['fav_list'].append(id_prod)
#     f.json_favorite_ids = json.dumps(o)
#     f.save()

    # # return JsonResponse(f.json_favorite_ids, safe=False)
    # return JsonResponse({"id_prod": id_prod }, safe=False)

# @login_required(login_url='/loginForm/')
# def json_favorites(request):
#     # alx = User.objects.all()[0]
#     #f = Favorite.objects.get(user = alx)
#     f = Favo.objects.get(user = request.user)
#     return JsonResponse(f.json_favorite_ids, safe=False)

def list_cars_json(request):  # static html file with javascript
    autos = Car.objects.all().values()[:10]
    car_list = list(autos)
    return JsonResponse(car_list, safe=False)

@login_required(login_url='/loginForm/')
def find_files(request):
   return render(request, 'find_files.html')


@login_required(login_url='/loginForm/')
def mongodb(request):
   return render(request, 'mongodb.html')

@login_required(login_url='/loginForm/')
def response_json_search_files(request, searchKey):
    command = 'find /home/kambo/mysite -name *' + searchKey + '*.*'
    out = os.popen(command).readlines()
    # command =  'grep -rnw \'/home/kambo/mysite\' -e \'import\''
    # out = os.popen(command).readlines()
    # send = []
    # for ln in out:
    #     if (len(ln) < 100):
    #         send.append(ln)
    return JsonResponse(out, safe=False)

@login_required(login_url='/loginForm/')
def response_json_grep(request, grepKey):
    command =  'grep -rn \'/home/kambo/mysite\' -e \''+ grepKey+'\''
    out = os.popen(command).readlines()
    send = []
    for ln in out:
        if (len(ln) < 100):
            send.append(ln)
    return JsonResponse(send, safe=False)

@login_required(login_url='/loginForm/')
def searchAngularJS(request):  # static html file with javascript
   return render(request, 'searchAngularJS.html')


@login_required(login_url='/loginForm/')
def url_index(request):  # static html file with javascript
   return render(request, 'url_index.html')

@login_required(login_url='/loginForm/')
def search_REST_API(request):  # static html file with javascript
   return render_to_response('search_REST_API.html')

# @login_required(login_url='/loginForm/')

def version(request):  # static html file with javascript
   return render(request, 'version.html', {'user': request.user, 'request': request.method} )

@login_required(login_url='/loginForm/')
def popover(request):  # static html file with javascript
   return render_to_response('popover.html')

# ***************************************************************
def loginForm(request):  # static html file with javascript
   return render_to_response('loginForm.html')
# **************************************************************

# import json
@login_required(login_url='/loginForm/')
def render_json_rep_template(request):
    return render(request, 'render_json_rep_template.html')

@login_required(login_url='/loginForm/')
def geolocalization_template(request):
    return render(request, 'geolocalization_template.html')

@login_required(login_url='/loginForm/')
def response_json_rep(request):
    car = Car.objects.filter(brand="Renault")
    json_obj = car[0].json_rep
    return JsonResponse(json_obj, safe=False)

from django.db.models import Q
from django.core.paginator import Paginator #, EmptyPage, PageNotAnInteger


@login_required(login_url='/loginForm/')
def simpleSearch(request):

    req_param = ''
    try:
        req_param = request.GET['brand']
        cars = Car.objects.filter( Q(brand__icontains = req_param) | Q(model__icontains = req_param) )
    except:
        cars = Car.objects.all()

    paginator = Paginator(cars, 10) # Show 25 contacts per page
    page = request.GET.get('page')

    if page == None:
        page = 1

    setCars = paginator.page(page)
    return render(request,"simpleSearch.html",{'req': request, 'host': request.get_host(), 'params': request.content_params, 'setCars': setCars , 'pagina': page, 'req_param':req_param } )


@login_required(login_url='/loginForm/')
def form(request):  # static html file with javascript
   return render(request, 'form.html', {})


@login_required(login_url='/loginForm/')
def message(request):  # static html file with javascript
   return render_to_response('message.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    login_required = True
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    login_required = True
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
"""
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # login_required = True
    # permission_classes = [IsAccountAdminOrReadOnly]
    # def get_queryset(self):
    #     return Car.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^brand', '^model')
    lookup_field = 'brand'

class ProdJSONListView(viewsets.ViewSet, generics.ListAPIView):
    login_required = True
    queryset = ProdJSON.objects.all()
    serializer_class = ProdJSONSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('json_full_info', 'json_basic_info', 'url', 'created_at', 'deleted_at', 'active', 'searchable_words')
    lookup_field = 'json_full_info'


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# class FavoriteListView(viewsets.ViewSet, generics.ListAPIView):
class FavoriteListView(viewsets.ModelViewSet):
# class FavoriteListView(APIView):

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('^username',)  # ************  THIS COMA IS MANDATORY!!!! ************
    # lookup_field = 'username'

