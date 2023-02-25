from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

def home(request):
    context = {
        "name": "Игорь",
        "email": "email@test.ru"
    }
    return render(request, 'index.html', context)

def get_countries_list(request):
    countries1 = Country.objects.all()
    paginator = Paginator(countries1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'countries_list.html', context)

def get_country(request, country_name):
    try:
        country = Country.objects.get(name=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Country with name: {country_name} not found")
    context = {
        'country': country,
        'country_languages': country.language.all
    }
    return render(request, 'country_info.html', context)

def get_languages(request):
    languages = Language.objects.all()
    paginator = Paginator(languages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
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

def same_fletter_countries(request, letter):
    countries = Country.objects.filter(name__startswith=f"{letter}")
    if not countries:
        return HttpResponseNotFound(f"There are no countries that start with the letter: {letter}.")
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'countries_list.html', context)