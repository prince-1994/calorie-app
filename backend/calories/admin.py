from django.contrib import admin
from .models import FoodCalorie
from django.utils import timezone
from datetime import timedelta

class FoodCalorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'consumed_at', 'calorie', 'user', 'created_at')

    def changelist_view(self, request, extra_context={}):
        date_format = "%d %b, %Y"
        delta_1 = timedelta(days=1)
        delta_7 = timedelta(days=7)
        date_1 = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        date_2 = date_1 - delta_7 + delta_1
        date_3 = date_1 - delta_7
        date_4 = date_1 - 2*delta_7 + delta_1
        extra_context['date_1'] = date_1.strftime(date_format)
        extra_context['date_2'] = date_2.strftime(date_format)
        extra_context['date_3'] = date_3.strftime(date_format)
        extra_context['date_4'] = date_4.strftime(date_format)
        extra_context['no_of_entry_date_2_to_date_1'] = FoodCalorie.get_no_entries(date_2, date_1 + delta_1)
        extra_context['no_of_entry_date_4_to_date_3'] = FoodCalorie.get_no_entries(date_4, date_3)
        extra_context['avg_calories_per_user_date_2_to_date_1'] = FoodCalorie.get_avg_calorie_per_user(date_2, date_1 + delta_1)
        print(extra_context)
        return super().changelist_view(request, extra_context=extra_context)
    

admin.site.register(FoodCalorie, FoodCalorieAdmin)
