from .models import Countries, Cities, Cc
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .controller import glosowanie
import random


def index(request):
    return render(request, 'game/index.html', {})


def country_pyt(request):
    global pyt_a_city, count_odp_a
    count_odp_a = Countries.objects.order_by('?').first()
    pyt_a_city = count_odp_a.cities
    odp_b = Countries.objects.order_by('?').first()
    odp_c = Countries.objects.order_by('?').first()
    lista_odp = [count_odp_a, odp_b, odp_c]
    random.shuffle(lista_odp)

    # request.session['odpowiedz'] = odp_a.cities

    return render(request, "game/countries_pyt.html", {
        'pyt_a_city': pyt_a_city,
        'lista_odp': lista_odp,
    })

def country_odp(request):
    return render(request, "game/countries_odp.html", {
        'pyt_a_city': pyt_a_city,
        'count_odp_a': count_odp_a,
        # 'odpowiedz': odpowiedz,
    })


def city_pyt(request):
    global pyt_a_country, city_odp_a
    city_odp_a = Cities.objects.order_by('?').first()
    pyt_a_country = city_odp_a.countries
    odp_b = Cities.objects.order_by('?').first()
    odp_c = Cities.objects.order_by('?').first()
    lista_odp = [city_odp_a, odp_b, odp_c]
    random.shuffle(lista_odp)

    # request.session['odpowiedz'] = odp_a.cities

    return render(request, "game/cities_pyt.html", {
        'pyt_a_country': pyt_a_country,
        'lista_odp': lista_odp,
    })

def city_odp(request):
    return render(request, "game/cities_odp.html", {
        'pyt_a_country': pyt_a_country,
        'city_odp_a': city_odp_a,
        # 'odpowiedz': odpowiedz,
    })

def cc_pyt(request):
    query = Cc.objects.values_list('country', 'city').order_by('?').first()

    global cc_city_pyt, cc_odp_a
    cc_city_pyt = query[1]
    cc_odp_a = query[0]
    odp_b = Cc.objects.values_list('country', 'city').order_by('?').first()[0]
    odp_c = Cc.objects.values_list('country', 'city').order_by('?').first()[0]

    lista_odp = [cc_odp_a, odp_b, odp_c]
    random.shuffle(lista_odp)

    return render(request, "game/cc_pyt.html", {
        'cc_city_pyt': cc_city_pyt,
        'lista_odp': lista_odp,
    })


def cc_odp(request):
    return render(request, "game/cc_odp.html", {
        'cc_city_pyt': cc_city_pyt,
        'cc_odp_a': cc_odp_a,
    })



# Powiązanie dwoch tabel Cities i Countries - zrobione w shellu

# for ci in Cities:
#     city = Cities.objects.create(nazwa=f"City {ci}")
#     country = Countries.objects.create(nazwa=f"Country {ci}")
#     city.country = country
#     city.save()

# stworzenie połączenia pomiedzy dwoma istniejacymi modelami (tabelami)
# w ktorych sa juz wprowadzone dane
# def relation_creation():
#     for ci in Cities.objects.all():
#         ci.countries_id = ci.id
#         ci.save()




# def pokaz_pierwsze_pyt(request):
#     q: Questions = Questions.objects.get(pk=1)
#     return HttpResponse(q.question_text)
#
# def pokaz_drugie_pyt(request):
#     q: Questions = Questions.objects.get(pk=2)
#     return HttpResponse(q.question_text)
#
# def pytanie(request, question_id):
#     q: Questions = Questions.objects.get(pk=question_id)
#     return HttpResponse(q.question_text)

# def pokaz_pierwsze_pyt_i_odp(request):
#     pytanie: Questions = Questions.objects.get(pk=1)
#     odpowiedzi_na_pytanie = pytanie.choice_set.all()
#
#     ladna_odpowiedz_do_przegladarki = f'Pytanie: {pytanie.question_text} <br/>'
#     for odp in odpowiedzi_na_pytanie:
#         ladna_odpowiedz_do_przegladarki += f' - {odp.choice_text} - liczba glosow: {odp.votes} <br/>'
#
#     return HttpResponse(ladna_odpowiedz_do_przegladarki)


# def pyt_i_odp(request, question_id):
#     try:
#         pytanie: Questions = Questions.objects.get(pk=question_id)
#     except Questions.DoesNotExist:
#         return HttpResponse('Nie ma takiego pytania ')
#     odpowiedzi_na_pytanie = pytanie.choice_set.all()
#
#     odpowiedzi_sformatowane = ''
#     for odp in odpowiedzi_na_pytanie:
#         odpowiedzi_sformatowane += f'<li> {odp.choice_text} - liczba glosow: {odp.votes} </li>'
#
#
#     ladna_odpowiedz_do_przegladarki = f"""
#     <b>Pytanie:</b> {pytanie.question_text}
# <ul>
#     {odpowiedzi_sformatowane}
#  </ul>
#
#     """
#     return HttpResponse(ladna_odpowiedz_do_przegladarki)


# def pyt_i_odp_template(request, question_id):
#     template = loader.get_template("game/countries_pyt.html")
#     pytanie = Questions.objects.get(pk=question_id)
#     context = {
#         'pytanie': pytanie,
#         'lista_odpowiedzi': pytanie.choice_set.all()
#     }
#     return HttpResponse(template.render(context, request))


# def pyt_i_odp_template2(request, question_id):
#     try:
#         return render(request, "game/cities_pyt.html", {
#             'pytanie': Questions.objects.get(pk=question_id),
#         })
#     except Questions.DoesNotExist:
#         return HttpResponse('Nie ma takiego pytania')

# def pokaz_pierwsze_pyt_innym_stylu(request):
#     return HttpResponse("trzeba zaimplementowac pokaz pierwsze pytanie w innym stylu")

# def oddano_glos(request):
#     return HttpResponse('Wlasnie oddales glos')


# def ankieta(request, question_id):
#     if request.method == "POST":
#         nr_odp = request.POST.get("nr_odp")
#         return glosowanie(request, nr_odp)
#     try:
#         return render(request, "game/ankieta.html", {
#             'pytanie': Questions.objects.get(pk=question_id),
#         })
#     except Questions.DoesNotExist:
#         return HttpResponse('Nie ma takiego pytania')

