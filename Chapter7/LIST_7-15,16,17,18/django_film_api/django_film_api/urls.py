"""URLルーティング定義."""
from django.conf.urls import url, include

from rest_framework import routers

from film import views

router = routers.DefaultRouter()

# /films のURLに views.FilmViewSet を紐付ける
router.register(r'films', views.FilmViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
