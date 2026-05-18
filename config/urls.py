from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from dashboard.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('workflow/', include('workflow.urls')),
]
