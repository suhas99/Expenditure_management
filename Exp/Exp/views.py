from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.context_processors import csrf
from .models import payment_stats, expendtitureDetails, Enrolled
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import matplotlib as plt
import json





def expendtiture(request,daysV=30):
	fdate = datetime.today().date() - timedelta(daysV)
	ldte=datetime.today().date()
	tests=expendtitureDetails.objects.filter(Date__gte=fdate, Date__lte = ldte)
	l=[]
	for i in tests:
		l.append(i.price)
	price1=sum(l)

	tests2=Enrolled.objects.filter(date_enrolled__gte=fdate, date_enrolled__lte = ldte)
	l2=[]
	for i in tests2:
		l2.append(i.amoount_paid)
	price2=sum(l2)
	if price2 > price1:
		var="profit"
		value=price2-price1
	elif price2 ==price1:
		var="Neutral"
		value=price2
	else:
		var="loss"
		value=price1-price2



	return render(request, 'abc.html', {'tests':tests,
										'var': var,
										'value':value,
										'Data':tests})
