from rest_framework import serializers
from .models import *


class ManografiaSerializer(serializers.ModelSerializer):
        class Meta:
                model = Manografia_models
                fields = '__all__'