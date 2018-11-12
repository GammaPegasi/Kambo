from django.conf.urls import url, include

from mysite.view import response_json_grep

urlpatterns = [
    # url(r'^foo/', include('mysite.urls')),
    url(r'^', include('mysite.urls')),
    # url(r'^response_json_grep/', response_json_grep),
    url(r'^response_json_grep/(?P<grepKey>\w{0,50})/$', response_json_grep),

]



