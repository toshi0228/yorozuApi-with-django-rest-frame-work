from django.contrib import admin
from .models import MyUser, Plan, Tag

admin.site.register(MyUser)
admin.site.register(Plan)
admin.site.register(Tag)
