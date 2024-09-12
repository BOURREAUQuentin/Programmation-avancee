from django.contrib import admin
from .models import Product, ProductItem, ProductAttribute, ProductAttributeValue

class ProductItemAdmin(admin.TabularInline):
    model = ProductItem
    filter_vertical = ("attributes",)

class ProductFilter(admin.SimpleListFilter):
    title = 'filtre produit'
    parameter_name = 'custom_status'
    
    def lookups(self, request, model_admin) :
        return (
            ('online', 'En ligne'),
            ('offline', 'Hors ligne'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'online':
            return queryset.filter(status=1)
        if self.value() == 'offline':
            return queryset.filter(status=0)

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductItemAdmin,]
    list_display = ('id', 'name', 'date_creation', 'status')
    list_editable = ['name']
    radio_fields = {"status": admin.VERTICAL}
    search_fields = ('name',)
    list_filter = (ProductFilter,)
    date_hierarchy = 'date_creation'

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)