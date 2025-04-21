from django.contrib import admin

from stb_database_app.models import Races, InnateAbilities, Stones, Aedra, Daedra

# Register your models here.
admin.site.register(Races)
admin.site.register(InnateAbilities)
admin.site.register(Stones)
admin.site.register(Aedra)
admin.site.register(Daedra)