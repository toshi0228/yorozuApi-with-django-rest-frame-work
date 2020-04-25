from django.contrib import admin
from .models import MyUser, Profile, Plan, Tag


admin.site.register(MyUser)
admin.site.register(Profile)
admin.site.register(Plan)
admin.site.register(Tag)
