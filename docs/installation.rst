.. _installation:

============
Installation
============

* To install django-user-accounts (no releases have been yet)::

    pip install django-user-accounts

* Add ``account`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # ...
        "account",
        # ...
    )

* See the list of :ref:`settings` to modify the default behavior of
  django-user-accounts and make adjustments for your website.

* Add ``account.urls`` to your URLs definition::

    urlpatterns = patterns("",
        ...
        url(r"^account/", include("account.urls")),
        ...
    )

* Add ``"account.context_processors.account"`` to ``TEMPLATE_CONTEXT_PROCESSORS``::

    TEMPLATE_CONTEXT_PROCESSORS = [
        ...
        "account.context_processors.account",
        ...
    ]

.. _dependencies:

Dependencies
============

``django.contrib.auth``
-----------------------

This is bundled with Django. It is enabled by default with all new Django
projects, but if you adding django-user-accounts to an existing project you
need to make sure ``django.contrib.auth`` is installed.

django-appconf_
---------------

We use django-appconf for app settings. It is listed in ``install_requires``
and will be installed when pip installs.

.. _django-appconf: https://github.com/jezdez/django-appconf