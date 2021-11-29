from django.urls import path
from agregator.views import index

urlpatterns = [
	path('', index, name='index')
]
