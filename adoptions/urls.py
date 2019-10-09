from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
]