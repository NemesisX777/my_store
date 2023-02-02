from django.contrib import admin

# Register your models here.
from contractors.models import ContractorCategory, Contractor, ContractorsObject


class ContractorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    # list_filter = ['is_active']
    search_fields = ['name']


class ContractorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'category', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'phone', 'address']


class ContractorsObjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'contractor', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'contractor']


admin.site.register(ContractorCategory, ContractorCategoryAdmin)
admin.site.register(Contractor, ContractorAdmin)
admin.site.register(ContractorsObject, ContractorsObjectAdmin)
