from django.contrib import admin
from django.urls import path
from apps.schedule.views import dashboard_grade # Importe a view que acabamos de criar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grade/', dashboard_grade, name='dashboard-grade'), # Nossa nova tela!
]