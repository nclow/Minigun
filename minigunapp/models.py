from django.db import models
import json

from mongoengine import *


class Email(Document):
    to = StringField(max_length=254)
    from_ = StringField(max_length=254)
    subject = StringField(max_length=9999)
    body = StringField(max_length=99999)
    status = StringField(default='pending')
    error_message = StringField(max_length=9999)
    retries = IntField(default=0)

    def __str__(self):
        return self.to_json()
