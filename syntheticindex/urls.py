"""
Syntheticindex URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views as app_views

router = routers.DefaultRouter()
#################
##  VIEWSETS   ##
#################
router.register(r'price', app_views.PriceViewSet)
router.register(r'store-prices', app_views.StorePrices, 'Prices')
router.register(r'synthetic_index',app_views.SyntheticIndex)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
