from django.contrib import admin

from .models import Thread, Comment

admin.site.register(Thread)
admin.site.register(Comment)
