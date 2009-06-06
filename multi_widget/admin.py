from django.contrib import admin
from models import DemoModel
from forms import FeetInchesModelForm

class DemoModelAdmin(admin.ModelAdmin):
    form = FeetInchesModelForm

admin.site.register(DemoModel,DemoModelAdmin)