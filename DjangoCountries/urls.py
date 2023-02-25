from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('countries-list', views.get_countries_list, name='countries'),
    path('country/<str:country_name>', views.get_country, name='country'),
    path('languages', views.get_languages, name='lang'),
    path('language/<str:language_name>', views.get_language, name='lang-info'),
    path('countries-that-start-with/<str:letter>', views.same_fletter_countries, name='letter')
]
