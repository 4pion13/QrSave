from django.contrib import admin
from .models import InformationAboutBoxes

# Register your models here.
@admin.register(InformationAboutBoxes)
class BoxInfo(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


