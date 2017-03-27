# Minigun

An example email-sending program using django, mongo, celery, redis

### Setup

`cd minigun`

`virtualenv .`

`source bin/activate`

`pip install -r requirements.txt`

`python manage.py runserver`

or

`python manage.py runserver 0.0.0.0:8000` to make it public

`celery -A minigun worker -l info` to run the celery worker

Setup postfix or another MTA however you want and change the `EMAIL_` settings in `settings.py` to point to it

Example: https://www.digitalocean.com/community/tutorials/how-to-install-and-setup-postfix-on-ubuntu-14-04

### Issue Requests

`GET /minigun/email`

```curl -XPOST 127.0.0.1:8000/minigun/email/ -d '{"to":"username@localhost.localdomain","subject":"Subject goes here","body":"Body goes here"}'```

### What's in the sauce?

* Mongodb
* Django
* Django Rest Framework
* Mongoengine
* Cerberus
* Celery
* Redis

### Where's the meat of it?

* https://github.com/nclow/minigun/blob/master/minigunapp/views.py
* https://github.com/nclow/minigun/blob/master/minigunapp/tasks.py
