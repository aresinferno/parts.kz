from .models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import F

def home_page(request):
    brand = request.GET.get("brand")
    model = request.GET.get("model")
    part_type = request.GET.get('part_type')
    year = request.GET.get("year")

    context = {}

    # 1. Если ничего не выбрано — показываем марки
    if not brand:
        context["brands"] = PartBrand.objects.all()

    # 2. Если выбрали бренд — показываем модели
    elif brand and not model:
        context["models"] = PartSeries.objects.filter(brand__slug=brand)

    elif brand and model and not part_type:
        context["part_types"] = (
            Part.objects
            .filter(brand__slug=brand, car_series__slug=model)
            .values_list("part_type__slug", "part_type__name").distinct()
        )

    elif brand and model and part_type and not year:
        context["years"] = (
            Part.objects
            .filter(brand__slug=brand, car_series__slug=model, part_type__slug=part_type)
            .values_list("year", flat=True)
            .distinct()
        )

    # 4. Если выбрано всё — показываем запчасти
    else:
        context["parts"] = Part.objects.filter(
            brand__slug=brand,
            car_series__slug=model,
            part_type__slug=part_type,
            year=year
        )

    return render(request, "part_templates/home_page.html", context)






