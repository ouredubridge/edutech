from django.contrib import admin
from .models import Group, Membership, Post, Comment

# Register your models here.
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Post)
admin.site.register(Comment)