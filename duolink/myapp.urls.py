from django.urls import path
from duolink import views

urlpatterns=[
    path('',views.index,name='index'),
    path('',views.trainer,name='trainer'),
    path('',views.why,name='why'),
    path('',views.contact,name='contact')
    ]