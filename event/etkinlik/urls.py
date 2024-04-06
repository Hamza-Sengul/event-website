from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('category/<int:category_id>/', views.category_events, name='category_events'),
    path('hesabim/', views.hesabim, name='hesabim'),
    path('slider-ekle/', views.slider_item_ekle, name='slider_ekle'),
    path('etkinlik-ekle/', views.event_ekle, name='etkinlik_ekle'),
    path('kategori-ekle/', views.category_ekle, name='kategori_ekle'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)