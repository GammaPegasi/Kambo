"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# djangorestframework in /home/kambo/.local/lib/python2.7/site-packages
# Requirement already satisfied (use --upgrade to upgrade): django-filter in /home/kambo/.local/lib/python2.7/site-packages

from django.conf.urls import url, include
from rest_framework import routers
from mysite import view
from django.contrib import admin
# , json_favorites, json_favorites_post

from mysite.view import list_cars_json, search_REST_API, simpleSearch, message, popover, version, send_retrieve_favorite, \
searchAngularJS, loginForm, render_json_rep_template, response_json_rep, geolocalization_template, url_index, find_files, \
response_json_search_files, mongodb, mongo_js, view_mongo, mongo_quick_search, camera,newspaper, salvattore, get_name, thanks, logout_view, \
validForm, submitedData

router = routers.DefaultRouter()
router.register(r'users', view.UserViewSet)
# router.register(r'groups', view.GroupViewSet)
router.register(r'carSet', view.CarViewSet)
# router.register(r'carList', view.CarListFilter)
router.register(r'prod_json', view.ProdJSONListView)
router.register(r'favorite', view.FavoriteListView)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'

urlpatterns = [

    # url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

    url(r'^validForm/', validForm),
    url(r'^submitedData/', submitedData),

    url(r'^get_name/', get_name),
    url(r'^thanks/', thanks),

    url(r'^logout_view/', logout_view),

    url(r'^newspaper/', newspaper),
    url(r'^salvattore/', salvattore),

    url(r'^camera/', camera),

    url(r'^mongodb/', mongodb),


    url(r'^mongo_js/', mongo_js),

    url(r'^view_mongo/(?P<searchKey>\w{0,50})/$', view_mongo),

    url(r'^mongo_quick_search/(?P<searchKey>\w{0,50})/$', mongo_quick_search),


    url(r'^admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),

    url(r'^simpleSearch/', simpleSearch),
    url(r'^search_REST_API/', search_REST_API),
    url(r'^searchAngularJS/', searchAngularJS),
    url(r'^loginForm/', loginForm),
    url(r'^render_json_rep_template/', render_json_rep_template),
    url(r'^geolocalization_template/', geolocalization_template),
    url(r'^find_files/', find_files),
    url(r'^send_retrieve_favorite/', send_retrieve_favorite),

    # url(r'^json_favorites/', json_favorites),
    # url(r'^json_favorites_post/(?P<id_prod>\w{0,50})/$', json_favorites_post),

    url(r'^response_json_search_files/(?P<searchKey>\w{0,50})/$', response_json_search_files),

    url(r'^response_json_rep/', response_json_rep),
    url(r'^url_index/', url_index),

    # url(r'^form/', form),


    url(r'^list_cars_json/', list_cars_json),

    url(r'^message/', message),
    url(r'^popover/', popover),
    url(r'^version/', version),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'car_view', view.CarListView.as_view())
    # url('^car_view/(?P<brand>.+)/$', view.CarListView.as_view()),

]
# Boostrap and AnjularJS
# file:///C:/Users/hvillarrea/Desktop/DEV/Bootstrap/layoutit2/src/index.html