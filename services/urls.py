from django.urls import path
from .views import ServiceList, ServiceDetailView


urlpatterns = [
    path('', ServiceList.as_view()),
    path('<int:id>', ServiceDetailView.as_view()),
]
