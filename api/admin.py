from django.contrib import admin
from api.models import  Company, Review

admin.site.register(Company)

admin.site.register(Review)

# admin.site.register(TaskList)

#
# @admin.register(Company)
# class CompanyListAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'bio',)
#
# @admin.register(Review)
# class ReviewListAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'rating', 'summary', 'ip_address', 'submissionDate', 'company',)