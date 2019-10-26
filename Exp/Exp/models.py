from django.db import models




class expendtitureDetails(models.Model):
	item = models.CharField(max_length=10, blank=False, null=False)
	quantity = models.IntegerField(blank=False, null=False)
	price = models.FloatField(blank=False, null=False, default=0)
	Date = models.DateField(blank=False, null=False)


class Enrolled(models.Model):
	name = models.CharField(max_length=10,null=False, blank=False)
	phone_no=models.IntegerField(max_length=10,blank=False,null=False)
	email=models.CharField(max_length=20,null=False,blank=False)
	amoount_paid=models.FloatField()
	date_enrolled=models.DateField(blank=False,null=False)


