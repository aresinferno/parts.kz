from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='home', permanent=False)),
    path('home/', views.home_page, name='home'),
    path('search_parts', views.search_parts, name='search_parts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)