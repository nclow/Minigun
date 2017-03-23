# Minigun

An example email-sending program using django, mongo, celery, redis

### Setup

`cd minigun`

`virtualenv .`

`source bin/activate`

`pip install cerberus django mongoengine pyyaml celery[redis]`

`python manage.py runserver`

or

`python manage.py runserver 0.0.0.0:8000` to make it public

`celery -A minigun worker -l info` to run the celery worker

### Issue Requests

`GET /minigun/email`

```curl -XPOST 127.0.0.1:8000/minigun/email/ -d '{"to":"nathan.clow@gmail.com","subject":"Subject goes here","body":"Body goes here"}'```

### What's in the sauce?

* Mongodb
* Django
* Mongoengine
* Cerberus
* Celery
* Redis

### Where's the meat of it?

https://github.com/nclow/minigun/blob/master/minigunapp/views.py
https://github.com/nclow/minigun/blob/master/minigunapp/tasks.py

### To Do

* Requirements file (dist)
