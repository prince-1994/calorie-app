from rest_framework import serializers
from .models import FoodCalorie

class FoodCalorieSerializer(serializers.ModelSerializer):
    is_inactive = serializers.BooleanField(required=False)
    class Meta:
        model = FoodCalorie
        exclude = ['user']
    
    def validate_calorie(self, value):
        if value and value < 0:
            raise serializers.ValidationError("This field should not be less than zero.")
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        obj = FoodCalorie.objects.create(**validated_data, user = user)
        return obj



