from django.urls import path

from .views import StatsAPIView, MutationAPIView


urlpatterns = [
    path('stats/', StatsAPIView.as_view()),
    path('mutation/', MutationAPIView.as_view()),
]