from django.contrib import admin
from staticapp.models import table

admin.site.register(table)

class admintable(admin.ModelAdmin):
    list_display = ['Mobile']
    class Meta:
        model=table



