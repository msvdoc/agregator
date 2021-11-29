from django.contrib import admin
from agregator.models import ShoesData, ShoesPrice


class ShoesAdmin(admin.ModelAdmin):
	list_display = ('name', 'magazineName', 'description', 'sezon')
	list_display_links = ('name', 'description')
	search_fields = ('name', 'magazineName')

class ShoesAdminPrice(admin.ModelAdmin):
	list_display = ('name', 'timeScan', 'priceShoes')

# Register your models here.
admin.site.register(ShoesData, ShoesAdmin)
admin.site.register(ShoesPrice, ShoesAdminPrice)
