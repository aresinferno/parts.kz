from django.contrib import admin
from .models import *
from django.urls import path
from django.http import JsonResponse


@admin.register(PartBrand)
class PartBrandAdmin(admin.ModelAdmin):
    pass

@admin.register(PartType)
class PartTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(PartSeries)
class PartSeriesAdmin(admin.ModelAdmin):
    pass

@admin.register(Part)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('part_type', 'brand', 'car_series')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("get-series/", self.admin_site.admin_view(self.get_series), name="get_series"),
        ]
        return custom_urls + urls

    def get_series(self, request):
        brand_id = request.GET.get("brand_id")
        series = PartSeries.objects.filter(brand_id=brand_id).values("id", "name")

        return JsonResponse(list(series), safe=False)

    class Media:
        js = ("admin/js/dependent_dropdown.js",)

@admin.register(PartPlace)
class PartPlaceAdmin(admin.ModelAdmin):
    pass