from django.contrib import admin

from alerts.models import ProductAlert, ProductAlertResult


class ProductAlertAdmin(admin.ModelAdmin):
    list_display = ("user", "product_search_phrase", "alert_frequency", "website", "created_at")

class ProductAlertResultAdmin(admin.ModelAdmin):
    list_display = ("product_alert", "created_at")

admin.site.register(ProductAlertResult, ProductAlertResultAdmin)
admin.site.register(ProductAlert, ProductAlertAdmin)
