# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from minigunapp.models import Email
from django.core.mail import send_mail

@shared_task
def send_email(id):
    email = Email.objects.get(id=id)

    try:
        send_mail(
            email.subject,
            email.body,
            email.from_,
            [email.to],
            fail_silently=False,
        )
        email.status = 'sent'
        print("Sent email {0}".format(email.id))
    except Exception as ex:
        print("Failed to send email {0} ({1})".format(email.id, email.retries))
        email.status = 'error'
        email.error_message = str(ex)
        if(email.retries < 3):
            print("Queueing email {0} for retry".format(email.id))
            email.retries += 1
            email.save()
            send_email.apply_async([str(email.id)], countdown=600)
        return False

    email.save()

    return True