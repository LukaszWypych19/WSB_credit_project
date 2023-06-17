from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path("", views.index, name="index"),
    path("country_pyt", views.country_pyt, name="country_pyt"),
    path("country_odp", views.country_odp, name="country_odp"),
    path("city_pyt", views.city_pyt, name="city_pyt"),
    path("city_odp", views.city_odp, name="city_odp"),
    path("save_history", views.save_history, name="save_history"),
    # path("zla_odp", views.zla_odp, name="zla_odp"),

    ]