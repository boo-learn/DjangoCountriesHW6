from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

with open("countries.json", "r") as f:
    countries_json = f.read()
countries = json.loads(countries_json)
lang_set = set()

for country in countries:
    for language in country['languages']:
        lang_set.add(language)

lang_lst = sorted(list(lang_set))

def home(request):
    context = {
        "name": "Игорь",
        "email": "email@test.ru"
    }
    return render(request, 'index.html', context)

def get_countries_list(request):
    context = {
        'countries': countries
    }
    return render(request, 'countries_list.html', context)

def get_country(request, country_name):
    for country in countries:
        if country['country'] == country_name:
            context = {
                'country': country
            }
            return render(request, 'country_info.html', context)
    return HttpResponseNotFound(f'Country "{country_name}" is not found.')

def get_languages(request):
    context = {
        'languages': lang_lst
    }
    return render(request, 'languages.html', context)