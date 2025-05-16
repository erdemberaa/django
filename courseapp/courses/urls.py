from django.urls import path
from . import views

# http://127.0.0.1:8000/client          => anasayfa
# http://127.0.0.1:8008/client/home     => anasayfa
# http://127.0.0.1:8000/client/products  => kurslar



urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('kurslar', views.kurslar),
    path('urunler', views.urunler),
    path('<kurs_adi>', views.hakkında),
    path('kategori/<int:category_name>', views.getCoursesByCategory),
    path('kategori/<str:category_id>', views.getCoursesByCategory),
]
