from django.contrib import admin
from .models import  expendtitureDetails,Enrolled
from datetime import datetime, timedelta





class expendtitureDetailsAdmin(admin.ModelAdmin):
	list_display = ('item', 'quantity', 'Date','price')


class enrolledAdmin(admin.ModelAdmin):
	list_display = ('name','phone_no','email','amoount_paid','date_enrolled')







admin.site.register(expendtitureDetails , expendtitureDetailsAdmin)
admin.site.register(Enrolled,enrolledAdmin)
