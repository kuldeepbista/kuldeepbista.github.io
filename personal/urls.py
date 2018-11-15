from django.conf.urls import url
from django.urls import path
from . import views


'''urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact')
]
'''

urlpatterns = [
	path('', views.index, name='index'),
	path('contact/', views.contact, name='contact')
]