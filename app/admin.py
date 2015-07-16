from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Movies
from app.models import Genre

admin.site.register(Movies)
admin.site.register(Genre)
