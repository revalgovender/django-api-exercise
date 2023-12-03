from django.contrib import admin
from django.urls import path

from exercise import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/payout/', views.payout, name='payout'),
]
