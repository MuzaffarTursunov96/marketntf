"""
WSGI config for cars project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
# path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# if path not in sys.path:
#     sys.path.append(path)

# from django.conf import settings

# sys.path.append('.heroku/python/lib/python3.8/site-packages')
# # .heroku/python/lib/python3.8/site-packages

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE']='cars.settings'

application = get_wsgi_application()
