from django.conf.urls import url

from art import views

urlpatterns = [
    url(r'^show/(\d+)/', views.show),
]
