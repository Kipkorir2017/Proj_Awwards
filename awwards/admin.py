from django.contrib import admin
from awwards.models import Profile,Rates,Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Rates)