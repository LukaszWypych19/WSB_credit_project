from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("question/", include("question.urls")),
    path("admin/", admin.site.urls),
]