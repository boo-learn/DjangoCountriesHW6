from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list', views.get_countries_list),
    path('country/<str:country_name>', views.get_country),
    path('languages', views.get_languages),
    path('language/<str:language_name>', views.get_language)
]
