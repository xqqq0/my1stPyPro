from django.conf.urls import url
from . import views as bv

urlpatterns = [
    url(r'^index/$', bv.index),
    url(r'^article/(?P<article_id>[0-9]+)$', bv.article_page,name="article_page"),
    url(r'^edit/$', bv.edit_page,name="edit_page"),
    url(r'^edit/action/$', bv.edit_action,name="edit_action"),
]