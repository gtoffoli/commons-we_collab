import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(__file__)

HAS_SAML2 = False # supports the SSO interface provided by the Up2U project (www.up2uiversity.eu) ?
HAS_LRS = True # supports xAPI?
HAS_EARMASTER = False # supports import and processing of the data exported from the EarMaster application ?

from commons.settings import *

CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS + ['http://www.we-collab.eu', 'https://www.we-collab.eu',]

# PRIMARY_DOMAIN = 'we-collab.commonspaces.eu'
PRIMARY_DOMAIN = 'www.we-collab.eu'
SECONDARY_DOMAIN = None
TEST_DOMAIN = None

SITE_ID = 5
IS_SITE_PRIVATE = True
IS_SITE_ERASMUS = True
SITE_NAME = 'WE-COLLAB'
SITE_ROOT = 'we-collab' # slug of the root community
HAS_CALENDAR = True
ALLOW_REDUCED_PROFILE = True

WSGI_APPLICATION = 'we_collab.wsgi.application'

# see: https://github.com/django/channels/issues/1039
# see: https://channels.readthedocs.io/en/latest/topics/consumers.html?highlight=inmemorychannellayer#websocketconsumer
ASGI_APPLICATION = 'we_collab.asgi.application'
if not 'channels' in INSTALLED_APPS:
    INSTALLED_APPS = ['channels'] + INSTALLED_APPS
if not 'feedback' in INSTALLED_APPS:
    INSTALLED_APPS = ['feedback'] + INSTALLED_APPS

ROOT_URLCONF = 'we_collab.urls'

PROJECT_TITLE = 'WE-COLLAB - Erasmus+'
PROJECT_NAME = 'we_collab'
LOGIN_REDIRECT_URL = 'we_collab.home'

LANGUAGES = (
    (u'en', u'English'),
    (u'da', u'Dansk'),
    (u'el', u'Ελληνικά'),
    (u'es', u'Español'),
    (u'hr', u'Hrvatski'),
    (u'it', u'Italiano'),
    (u'lt', u'Lietuvių'),
)

for code, name in LANGUAGES:
    if not code in LANGUAGE_MAPPING:
        LANGUAGE_MAPPING[code] = name

