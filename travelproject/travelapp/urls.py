from . import views
from django.urls import path

urlpatterns = [
    path('',views.demofn,name='demofn' ),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
