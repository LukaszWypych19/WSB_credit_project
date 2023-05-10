from django.contrib import admin

from .models import Choice, Questions

# ...
admin.site.register(Choice)
admin.site.register(Questions)
