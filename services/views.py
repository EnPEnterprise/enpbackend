from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Service
from .serializers import ServiceSerializer
from rest_framework import permissions


class ServiceList(ListCreateAPIView):

    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)


class ServiceDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Service.objects.filter(owner=self.request.user)
