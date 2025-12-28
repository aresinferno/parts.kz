from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='home', permanent=False)),
    path('home/', views.home_page, name='home')
]