from django.urls import path
from .views import *


urlpatterns = [
    path('', paided, name='paided'),
    path('list/', list_ac_pa, name='list_ac_pa'),
]