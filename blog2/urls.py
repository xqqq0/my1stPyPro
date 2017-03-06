from django.conf.urls import url
from . import  views as v
urlpatterns = [
    url(r'^index2/$', v.index)
]



