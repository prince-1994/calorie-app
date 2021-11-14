from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodCalorieSerializer
from .models import FoodCalorie

class FoodCalorieViewSet(viewsets.ModelViewSet):
    serializer_class = FoodCalorieSerializer
    permission_classes = (IsAuthenticated,)
    ordering_fields = ('consumed_at',)
    filterset_fields = {
        'consumed_at' : ['gte', 'lte', 'gt', 'lt']
    }
    
    def get_queryset(self):
        return FoodCalorie.objects.filter(user = self.request.user)
