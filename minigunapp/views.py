from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.db import models
from django.core.mail import send_mail
import json
import yaml
from cerberus import Validator
from minigunapp.models import Email

v = Validator()
schema = yaml.load(open('minigunapp/schemas/email.yaml'))

def email(request):
    if request.method in ['GET', 'POST']:
        return globals()[request.method.lower() + '_email'](request) # WTB a real router
    raise Http404("Not found")

def get_email(request):
    emails = [json.loads(str(email)) for email in Email.objects.all()]
    return JsonResponse(emails, safe=False)

def post_email(request):
    
    body = json.loads(request.body.decode("utf-8"))
    valid = v.validate(body, schema)
    if(not valid):
        return JsonResponse(v.errors, status=400)

    email = Email(**body)
    email.from_ = 'nathan.clow@gmail.com'

    try:
        sent = send_mail(
            email.subject,
            email.body,
            email.from_,
            [email.to],
            fail_silently=False,
        )
        email.status = 'ok'
    except Exception as ex:
        email.status = 'error'
        email.error_message = str(ex)
    
    email.save()

    return HttpResponse(str(email))