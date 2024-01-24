from django.contrib import admin
from .models import Product,Variation ,ReviewRating ,ABC ,Cde
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','stock','price','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}



class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable =('is_active',)
    list_filter= ('product','variation_category','variation_value')


admin.site.register(Product , ProductAdmin)
admin.site.register(Variation ,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ABC)
admin.site.register(Cde)