from django.shortcuts import render, redirect, get_object_or_404
from . import models

def ads_view(request, slug=None):
    ads = models.Ads.objects.all()

    if slug:
        city_values = [c[0] for c in models.IRAN_CITIES]

        if slug in city_values:
            ads = ads.filter(city=slug)
        else:
            ads = ads.filter(category__name=slug)

    return render(request, 'Ads/Ads.html', {'ads': ads})


def delete_view(request, slug=None):
    ad = get_object_or_404(models.Ads, id=slug)
    ad.delete()
    return redirect('ads_list')

