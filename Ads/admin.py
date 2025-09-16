from django.contrib import admin

from Ads import models


@admin.register(models.RealEstateAd)
class RealEstateAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'price', 'price_per_meter', 'date')

    search_fields = ('title', 'description', 'content')

    list_filter = ('city', 'category', 'has_elevator', 'has_parking', 'has_storage')

    readonly_fields = ('date',)


@admin.register(models.CarAd)
class CarAdAdmin(admin.ModelAdmin):
    list_display = ('title','city','category', 'price','mileage', 'production_year', 'color', 'brand', 'model', 'trim', 'insurance_expiry', 'gearbox',
                    'fuel_type')
    search_fields = ('brand','gearbox','fuel_type','base_price')
    list_filter = ('city', 'category','price')


@admin.register(models.DigitalProductAd)
class DigitalProductAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'model_name', 'condition', 'price', 'warranty')

    search_fields = ('title', 'brand', 'model_name')

    list_filter = ('brand', 'condition', 'warranty')

@admin.register(models.HomeKitchenAd)
class HomeKitchenAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_type', 'brand', 'material', 'condition', 'price')

    search_fields = ('title', 'product_type', 'brand', 'material')

    list_filter = ('brand', 'condition', 'material')

@admin.register(models.ServiceAd)
class ServiceAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'experience_years', 'is_remote', 'price')
    search_fields = ('title', 'service_type')
    list_filter = ('is_remote', 'service_type')


@admin.register(models.PersonalItemAd)
class PersonalItemAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'brand', 'condition', 'price')
    search_fields = ('title', 'item_type', 'brand')
    list_filter = ('condition', 'brand', 'material')


@admin.register(models.EntertainmentAd)
class EntertainmentAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'entertainment_type', 'condition', 'brand', 'price')
    search_fields = ('title', 'brand', 'genre')
    list_filter = ('entertainment_type', 'condition', 'brand')


@admin.register(models.IndustrialEquipmentAd)
class IndustrialEquipmentAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'equipment_type', 'brand', 'condition', 'price')
    search_fields = ('title', 'equipment_type', 'brand')
    list_filter = ('equipment_type', 'condition', 'brand')


@admin.register(models.JobListingAd)
class JobListingAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'company', 'employment_type', 'salary')
    search_fields = ('title', 'position', 'company')
    list_filter = ('employment_type', 'company')


class AdImageInline(admin.TabularInline):
    model = models.AdImage
    extra = 1

@admin.register(models.Ads)
class AdsAdmin(admin.ModelAdmin):
    inlines = [AdImageInline]
    list_display = ('title', 'city', 'category', 'price', 'date')


admin.site.register(models.Category)
