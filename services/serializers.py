from rest_framework.serializers import ModelSerializer
from .models import Service


class ServiceSerializer(ModelSerializer):

    class Meta:
        model = Service

        fields = ['id', 'first_name', 'last_name', 'phone_number',
                  'service_picture', 'is_favorite'
                  ]
