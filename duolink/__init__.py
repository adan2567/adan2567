from django.urls import path
from duolink import views

urlpatterns=[
    path('',views.trainer,name='trainer'),
    path('',views.contact,name='contact'),
    path('',views.index,name='index'),
    path('', views.why,name='why')
]