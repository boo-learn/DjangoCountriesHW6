from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country
from django.core.exceptions import ObjectDoesNotExist

countries = Country.objects.all()
lang_set = set()

for country in countries:
    for language in country.languages.split():
        lang_set.add(language)

lang_lst = sorted(list(lang_set))

def home(request):
    context = {
        "name": "Игорь",
        "email": "email@test.ru"
    }
    return render(request, 'index.html', context)

def get_countries_list(request):
    countries1 = Country.objects.all()
    context = {
        'countries': countries1
    }
    return render(request, 'countries_list.html', context)

def get_country(request, country_name):
    try:
        country = Country.objects.get(name=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country with name: {country_name} not found")
    context = {
        'country': country,
        'country_languages': country.languages.split()
    }
    return render(request, 'country_info.html', context)

def get_languages(request):
    context = {
        'languages': lang_lst
    }
    return render(request, 'languages.html', context)