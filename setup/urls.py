from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('grade/', views.grade_visual, name='grade_visual'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
