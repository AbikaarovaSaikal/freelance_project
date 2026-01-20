from django.contrib import admin
from freelance.models import Job, Category, Tag, Comment
# Register your models here.

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)