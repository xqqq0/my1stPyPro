from django.conf.urls import url
from . import views as bv

urlpatterns = [
    url(r'^index/',bv.index),
]