from django.contrib import admin
from groups import models

admin.site.register(models.Group)

# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember