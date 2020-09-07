from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "review_count"]
    search_fields = ['brand', "model"]
    list_filter = ("model", "brand")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["car", "title"]
    list_filter = ("car__brand", "title")
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
