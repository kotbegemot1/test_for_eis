from django.contrib import admin
from .models import Accrual, Payment
# Register your models here.
@admin.register(Accrual)
class AcrualAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'date', 'month']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["__str__", 'date', 'month']
