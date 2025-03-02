from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'student_id', 'approved')
    list_filter = ('approved', 'teacher_name')
    search_fields = ('teacher_name', 'student_id', 'review_text')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Mark selected reviews as approved"

admin.site.register(Review, ReviewAdmin)
