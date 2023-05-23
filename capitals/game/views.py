from .models import Countries, Cities, Cc
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .controller import glosowanie
import random


def index(request):
    return render(request, 'game/index.html', {})


# def country(request):
#     cou = Countries.objects.all()
#     return HttpResponse(cou)


def country(request):
    city_list1 = Cities.objects.order_by('?').first()
    city_list2 = Cities.objects.order_by('?').first()
    city_list3 = Cities.objects.order_by('?').first()

    return render(request, "game/countries_pyt.html", {
        'city_list1': city_list1,
        'city_list2': city_list2,
        'city_list3': city_list3,
    })


def city(request):
    country_list1 = Countries.objects.order_by('?').first()
    country_list2 = Countries.objects.order_by('?').first()
    country_list3 = Countries.objects.order_by('?').first()
    return render(request, "game/cities_pyt.html", {
        'country_list1': country_list1,
        'country_list2': country_list2,
        'country_list3': country_list3,
    })


def country_and_city(request):
    query = Cc.objects.values_list('country', 'city').order_by('?').first()

    global city, odp_a
    city = query[1]
    odp_a = query[0]
    odp_b = Cc.objects.values_list('country', 'city').order_by('?').first()[0]
    odp_c = Cc.objects.values_list('country', 'city').order_by('?').first()[0]

    lista_odp = [odp_a, odp_b, odp_c]
    random.shuffle(lista_odp)

    return city, render(request, "game/cc.html", {
        'city': city,
        'lista_odp': lista_odp,
    })


def cc_odp(request):
    return render(request, "game/cc_odp.html", {
        'city': city,
        'odp_a': odp_a,
    })

# def country_and_city(request):
#     cc = Cc.objects.all()
#     return HttpResponse(cc)


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

