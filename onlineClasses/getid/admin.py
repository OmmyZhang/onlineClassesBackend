from django.contrib import admin

from .models import SessionRecord,AppInfo

admin.site.register(SessionRecord)
admin.site.register(AppInfo)

