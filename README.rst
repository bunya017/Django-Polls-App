================
Django Polls App
================

``Django Polls App`` is an implementation of tutorials in the official django docs. Padded with new features, you can group ``Categories`` under a ``Ballot Box``


Requirements
------------

* Python 2.7 or 3.4+(not tested)
* Django 1.11+


Configuration
-------------

1. Create a virtual environment, for python 2.7 run::

    python virtualenv --your_env-- or virtualenv --your_env--

2. Activate virtual environment and install dependencies::

    pip install -r requirements.txt

3. Make migrations and make database tables by running::

    python manage.py makemigrations
    python manage.py migrate


Usage
-----

After configuration, run ``python manage.py runserver`` 
and open ``http://localhost:8000/`` on your browser.