from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Homework
# Register your models here.
admin.site.site_header = "Adminitrador de tareas"
admin.site.unregister(Group)
admin.site.register(Homework)