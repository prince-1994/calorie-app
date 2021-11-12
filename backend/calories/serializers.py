from rest_framework import serializers
from .models import FoodCalorie

class FoodCalorieSerializer(serializers.ModelSerializer):
    is_inactive = serializers.BooleanField(required=False)
    class Meta:
        model = FoodCalorie
        exclude = ['user']
    
    def create(self, validated_data):
        user = self.context["request"].user
        obj = FoodCalorie.objects.create(**validated_data, user = user)
        return obj



