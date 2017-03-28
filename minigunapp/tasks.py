import logging 

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
        logging.info("Sent email {0}".format(email.id))
    except Exception as ex:
        logging.error("Failed to send email {0} ({1}): {2}".format(email.id, email.retries. str(ex)))
        email.status = 'error'
        email.error_message = str(ex)
        if(email.retries < 3):
            logging.info("Queueing email {0} for retry".format(email.id))
            email.retries += 1
            email.save()
            send_email.apply_async([str(email.id)], countdown=600)
        return False

    email.save()

    return True
