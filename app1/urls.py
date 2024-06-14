from django.urls import path
from .views import home,home2,home3,home4,home5
urlpatterns = [
      path('',home,name='home1'),
      path('home2/',home2,name='home2'),
      path('home3/',home3,name='home3'),
      path('home4/',home4,name='home4'),
      path('home5/',home5,name='home5'),
]