from django.contrib import admin

from insights.models import UserInsightRecord


class UserInsightRecordAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'description', 'created_at')

admin.site.register(UserInsightRecord, UserInsightRecordAdmin)
