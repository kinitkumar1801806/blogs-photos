
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.index,name="index"),
    path('blogview/',views.blogview,name="blogview"),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
    path('defence_blogpost/<int:id>', views.defence_blogpost, name='defence_blogpost'),
    path('software_blogpost/<int:id>', views.software_blogpost, name='software_blogpost'),
    path('contact/',views.contact,name='ContactUs'),
    path('Imageview/<int:myid>',views.Imageview,name="Imageview"),
    path('animals_Imageview/<int:myid>',views.animals_Imageview,name="animals_Imageview"),
    path('accessories_Imageview/<int:myid>',views.accessories_Imageview,name="accessories_Imageview"),
    path('nature_Imageview/<int:myid>',views.nature_Imageview,name="nature_Imageview"),
    path('heritage_Imageview/<int:myid>',views.heritage_Imageview,name="heritage_Imageview"),
    path('monuments_Imageview/<int:myid>',views.monuments_Imageview,name="monuments_Imageview"),
    path('holyplaces_Imageview/<int:myid>',views.holyplaces_Imageview,name="holyplaces_Imageview"),
    path('vehicles_Imageview/<int:myid>',views.vehicles_Imageview,name="vehicles_Imageview"),
    path('search/', views.search, name='Search'),
    path('defenceblog/', views.defenceblog,name="defenceblog"),
    path('softwareblog/',views.softwareblog,name="softwareblog"),
    path('animals_photo/', views.animals_photo, name='animals_photo'),
    path('accessories_photo/',views.accessories_photo,name='accessories_photo'),
    path('nature_photo/',views.nature_photo,name="nature_photo"),
    path('heritage_photo/', views.heritage_photo, name='heritage_photo'),
    path('monuments_photo/',views.monuments_photo,name='monuments_photo'),
    path('holyplaces_photo/',views.holyplaces_photo,name="holyplaces_photo"),
    path('vehicles_photo/', views.vehicles_photo, name='vehicles_photo'),
]
