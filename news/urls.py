from rest_framework.routers import DefaultRouter 
from django.urls import path,include
from .views import NewsViewSet

router=DefaultRouter()
router.register('',NewsViewSet)
urlpatterns = [
    path('',include(router.urls))
]