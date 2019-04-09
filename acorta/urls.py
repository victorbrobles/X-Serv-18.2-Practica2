from django.urls import path
from . import views

urlpatterns = [
	path ('', views.bar),
	path ('<int:numero>', views.comprobar_url),
	path ('<str:cadena>', views.error),
]
