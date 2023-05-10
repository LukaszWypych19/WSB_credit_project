from django.urls import path

from . import views, controller

# app_name = 'game'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.pytanie, name="detail"),
    path("game/<int:question_id>", views.pyt_i_odp, name="game"),
    path("pyt_i_odp_template/<int:question_id>", views.pyt_i_odp_template, name="pyt_i_odp_template"),
    path("pyt_i_odp_template2/<int:question_id>", views.pyt_i_odp_template2, name="pyt_i_odp_template2"),
    path("pokaz_pierwsze_pyt", views.pokaz_pierwsze_pyt, name="pokaz_pierwsze_pyt"),
    path("pokaz_drugie_pyt", views.pokaz_drugie_pyt, name="pokaz_drugie_pyt"),
    path("pokaz_pierwsze_pyt_i_odp", views.pokaz_pierwsze_pyt_i_odp, name="pokaz_pierwsze_pyt_i_odp"),
    path("pokaz_pierwsze_pyt_innym_stylu", views.pokaz_pierwsze_pyt_innym_stylu, name="pokaz_pierwsze_pyt_innym_stylu"),

    path("oddano_glos", views.oddano_glos, name='oddano_glos'),
    path("ankieta/<int:question_id>", views.ankieta, name='ankieta'),
    path("glosowanie/<int:wybor_id>", controller.glosowanie, name='glosowanie'),

]