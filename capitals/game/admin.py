from django.contrib import admin

from .models import Countries, Cities

# ...
admin.site.register(Countries)
admin.site.register(Cities)
