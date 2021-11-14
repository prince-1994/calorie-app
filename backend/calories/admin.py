from django.contrib import admin
from .models import FoodCalorie
from django.utils import timezone
from datetime import timedelta

class FoodCalorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'consumed_at', 'calorie', 'user', 'created_at')

    def changelist_view(self, request, extra_context={}):
        now = timezone.now()
        delta = timedelta(days=7)
        extra_context['no_of_entry_last_7_days'] = FoodCalorie.get_no_entries(now-delta, now)
        extra_context['no_of_entry_last_to_last_7_days'] = FoodCalorie.get_no_entries(now-2*delta, now-delta)
        extra_context['avg_calories_per_user_last_7_day'] = FoodCalorie.get_avg_calorie_per_user(now-delta, now)
        print(extra_context)
        return super().changelist_view(request, extra_context=extra_context)
    

admin.site.register(FoodCalorie, FoodCalorieAdmin)
