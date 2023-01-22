from django.urls import path

from .views import (
    ApiKeyListApiView,
)

urlpatterns = [
    path('api', ApiKeyListApiView.as_view()),
]
