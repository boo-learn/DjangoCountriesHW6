from django.contrib import admin
from django.urls import path
from MainApp import views

# TODO: настройки IDE(.idea) не должны быть частью репозиторию
urlpatterns = [
    # TODO: используйте именованные url'ы
    # TODO: используйте наследование шаблонов
    path('', views.home),
    # TODO: а как попасть на страницу со списком стран обычному пользователю сайта?
    path('countries-list', views.get_countries_list),
    path('country/<str:country_name>', views.get_country),
    path('languages', views.get_languages),
    path('language/<str:language_name>', views.get_language),
    # TODO: артикли никогда не используются в именовании функций и переменных
    path('countries-that-start-with/<str:letter>', views.the_same_fletter_countries)
]
