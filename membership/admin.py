from django.contrib import admin

from .models import Thread, Comment, StudentWork


admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(StudentWork)
