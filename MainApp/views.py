from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist

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
        'languages': Language.objects.all()
    }
    return render(request, 'languages.html', context)

def get_language(request, language_name):
    try:
        language = Language.objects.get(name=language_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Language: {language_name} not found.")
    countries2 = Country.objects.filter(language__name=language_name)
    context = {
        'language': language,
        'countries': countries2
    }
    return render(request, 'language_info.html', context)