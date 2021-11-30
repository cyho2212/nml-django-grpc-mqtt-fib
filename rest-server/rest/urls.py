from django.urls import path, re_path

from .views import FibView, LogView

urlpatterns = [
    path('fibonacci', FibView.as_view()),
    path('logs', LogView.as_view())
]
