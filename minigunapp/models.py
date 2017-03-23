from django.db import models
import json
# Create your models here.

from mongoengine import *

class Email(Document):
    to = StringField(max_length=254)
    from_ = StringField(max_length=254)
    subject = StringField(max_length=9999)
    body = StringField(max_length=99999)
    status = StringField(default='pending')
    error_message = StringField(max_length=9999)

    def __str__(self):
        return self.to_json()

    # def __iter__(self):
    #     for field_name in Email._meta.get_field("to"):
    #         value = getattr(self, field_name, None)
    #         yield (field_name, value)