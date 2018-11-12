"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()


# import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)

# logging.debug('This message should go to the log file')
# logging.info(application)
# # logging.warning('And this, too')
