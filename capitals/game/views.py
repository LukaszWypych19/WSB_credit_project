from .models import Countries, Cities, Cc, History, AuthUser
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .controller import glosowanie
import random
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'game/index.html', {})


def country_pyt(request):

    total_nr_of_id = Cc.objects.count()
    random_id = random.randint(0, total_nr_of_id - 1)
    query = Cc.objects.values_list('country', 'city')[random_id]
    # alternatywna metoda losowania odp a
    # query = Cc.objects.values_list('country', 'city').order_by('?').first()

    city_for_country_pyt = query[1]
    country_odp_a = query[0]    # prawidlowa odpowiedz

    random_id = random.randint(0, total_nr_of_id - 1)
    country_odp_b = Cc.objects.values_list('country', 'city')[random_id][0]
    # alternatywna metoda losowania odp b
    # country_odp_b = Cc.objects.values_list('country', 'city').order_by('?').first()[0]

    random_id = random.randint(0, total_nr_of_id - 1)
    country_odp_c = Cc.objects.values_list('country', 'city')[random_id][0]
    # alternatywna metoda losowania odp c
    # country_odp_c = Cc.objects.values_list('country', 'city').order_by('?').first()[0]

    user_id = request.user.id

    lista_country_odp = [country_odp_a, country_odp_b, country_odp_c]
    random.shuffle(lista_country_odp)

    return render(request, "game/countries_pyt.html", {
        'city_for_country_pyt': city_for_country_pyt,
        'lista_country_odp': lista_country_odp,
        'user_id': user_id,
        'country_odp_a': country_odp_a,
    })

def country_odp(request):
    if request.method == 'POST':
        country_odp_a = request.POST.get('country_odp_a')
        city_for_country_pyt = request.POST.get('city_for_country_pyt')
        user_id = request.POST.get('user_id')

    return render(request, "game/countries_odp.html", {
        'city_for_country_pyt': city_for_country_pyt,
        'country_odp_a': country_odp_a,
        'user_id': user_id,
    })


def city_pyt(request):
    total_no_of_id = Cc.objects.count()
    random_id = random.randint(0, total_no_of_id - 1)
    query = Cc.objects.values_list('country', 'city')[random_id]

    # alternatywna metoda losowania odp a
    # query = Cc.objects.values_list('country', 'city').order_by('?').first()

    country_for_city_pyt = query[0]
    city_odp_a = query[1]    # prawidlowa odpowiedz


    random_id = random.randint(0, total_no_of_id - 1)
    city_odp_b = Cc.objects.values_list('country', 'city')[random_id][1]
    # alternatywna metoda losowania odp b
    # city_odp_b = Cc.objects.values_list('country', 'city').order_by('?').first()[1]


    random_id = random.randint(0, total_no_of_id - 1)
    city_odp_c = Cc.objects.values_list('country', 'city')[random_id][1]
    # alternatywna metoda losowania odp c
    # city_odp_c = Cc.objects.values_list('country', 'city').order_by('?').first()[1]

    user_id = request.user.id

    lista_city_odp = [city_odp_a, city_odp_b, city_odp_c]
    random.shuffle(lista_city_odp)

    return render(request, "game/cities_pyt.html", {
        'country_for_city_pyt': country_for_city_pyt,
        'lista_city_odp': lista_city_odp,
        'user_id': user_id,
        'city_odp_a': city_odp_a,
    })


def city_odp(request):
    if request.method == 'POST':
        city_odp_a = request.POST.get('city_odp_a')
        country_for_city_pyt = request.POST.get('country_for_city_pyt')
        user_id = request.POST.get('user_id')
    return render(request, "game/cities_odp.html", {
        'country_for_city_pyt': country_for_city_pyt,
        'city_odp_a': city_odp_a,
        'user_id': user_id,
    })


@login_required
def save_history(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        correct_ans = request.POST.get('correct_ans')

        user_id = request.user.id
        # zapisanie wynikow do bazy danych
        history = History(question=question, correct_ans=correct_ans, username_id_id=user_id)
        history.save()
        # wyswietlanie ostatnich (10) pytanie + odpowiedz + uzytkownik
        last_items = History.objects.order_by('-id')[:10]

        return render(request, 'save_history.html', {
            'question': question,
            'correct_ans': correct_ans,
            'user_id': user_id,
            'last_items': last_items,
        })




# def get_last_five_history_items(request, user):
#     last_five_items = History.objects.filter(username_id_id=user).order_by('-timestamp')[:5]
#     return render(request, 'save_history.html', {
#         # 'question': question,
#         # 'correct_ans': correct_ans,
#         # 'user_id': user_id,
#         # 'last_hist': last_hist,
#         'last_five_items': last_five_items,
#     })

    # return last_five_items


# def zla_odp(request):
#     return HttpResponse('To nie jest poprawna odpowiedź! Spróbuj ponownie!')



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




