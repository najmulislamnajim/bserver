from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import DonorViewSet,DonationRequestViewSet


router=DefaultRouter()
router.register('list',DonorViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('donation-request/',DonationRequestViewSet.as_view(),name='donation-request')
]

