import os

KOFA_TELEGRAM_BOT_ENV = os.environ.get('KOFA_TELEGRAM_BOT_ENV')

try:
    if KOFA_TELEGRAM_BOT_ENV == 'production':
        from settings.production import *
    else:
        from settings.development import *
        from settings.production import TELEGRAM_TOKEN
except ImportError:
    from settings.development import *
