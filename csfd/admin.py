from django.contrib import admin
from django.utils.html import format_html
from .models import Filmy, Tvurci, Idecka

# Register your models here.

# admin.site.register(Filmy)

@admin.register(Filmy)
class FilmyAdmin(admin.ModelAdmin):
    list_display = ['nazev', 'rok', '_url', 'hodnoceni']
    search_fields = ['nazev']

    def _url(self, obj):
        return format_html('<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url))

@admin.register(Tvurci)
class TvurciAdmin(admin.ModelAdmin):
    list_display = ['jmeno', 'id_tvurce']
    search_fields = ['jmeno', 'id_tvurce']


@admin.register(Idecka)
class TvurciAdmin(admin.ModelAdmin):
    list_display = ['id_tvurce', 'id_filmu']
    search_fields = ['id_tvurce', 'id_filmu']
