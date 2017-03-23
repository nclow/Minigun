# Minigun

### Setup

`cd minigun`

`virtualenv .`

`source bin/activate`

`pip install cerberus django mongoengine pyyaml`

`python manage.py runserver`

or

`python manage.py runserver 0.0.0.0:8000` to make it public

### Issue Requests

curl -XPOST 127.0.0.1:8000/minigun/email/ -d '{"to":"nathan.clow@gmail.com","subject":"sub","body":"bod"}'

### What's in the sauce?

* Mongodb
* Django
* Mongoengine
* Cerberus

### To Do

GET route
Requirements file (dist)
Queueing
Description