from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer, Service, Product, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'organization', 'phone_number')
    list_filter = ('cust_name', 'organization')
    search_fields = ('cust_name',)
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ('cust_name', 'service_category', 'setup_time')
    list_filter = ('cust_name', 'setup_time')
    search_fields = ('cust_name',)
    ordering = ['cust_name']


class ProductList(admin.ModelAdmin):
    list_display = ('cust_name', 'product', 'pickup_time')
    list_filter = ('cust_name', 'pickup_time')
    search_fields = ('cust_name',)
    ordering = ['cust_name']


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'department', 'employee_cell_phone', 'is_staff', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Product, ProductList)

# Register your models here.
