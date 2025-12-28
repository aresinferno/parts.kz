from django.shortcuts import render
from .models import *

def home_page(request):
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    year = request.GET.get('year')

    context = {}

    if not brand:
        context['brands'] = PartBrand.objects.all()

    elif brand and not model:
        context['models'] = PartSeries.objects.filter(brand__slug=brand)

    elif brand and model and not year:
        context['years'] = Part.objects.filter(brand__slug=brand, car_series__slug=model).values_list('year', flat=True).distinct()

    else:
        context['parts'] = Part.objects.filter(brand__slug=brand, car_series__slug=model, year=year)


    return render(request,
        'part_templates/home_page.html',
                context)


