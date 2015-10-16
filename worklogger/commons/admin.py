from django.contrib import admin
from commons.models import *


class UserAdmin(admin.ModelAdmin):
    fields = ['name']


class ProjectAdmin(admin.ModelAdmin):
    fields = ['name']


class PostAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Post_To_Tag)
# Register your models here.
