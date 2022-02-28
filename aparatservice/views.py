from django.shortcuts import render
from .froms import InterfaceForm
from .models import Interface
from django.contrib import messages
import aparatsr.settings as settings
import json
import urllib
from django.contrib.auth import login , authenticate

# Create your views here.

def index(request):
    form = InterfaceForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                form.save()
                messages.success(request, 'درخواست شما با موفقیت ثبت شد و تا 24 ساعت آینده واریز خواهد شد.اگر فالوور ها واریز نشدند با استفاده از دکمه پشتیبانی پیگیر باشید.')
            else:
                messages.error(request, 'لطفا تیک من ربات نیستم را بزنید . اگر مشکلی دیگری بود با پشتیبانی از طریق دکمه پشتیبانی در تماس باشید.')

    return render(request , "aparatservice/index.html" , {"form" : form})