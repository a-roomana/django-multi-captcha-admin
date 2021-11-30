from __future__ import print_function
from django.conf import settings

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

engines = {
    'simple-captcha': {
        'app': 'captcha',
        'pip': 'django-simple-captcha',
        'url': 'https://github.com/mbi/django-simple-captcha'
    },
    'recaptcha': {
        'app': 'captcha',
        'pip': 'django-recaptcha',
        'url': 'https://github.com/praekelt/django-recaptcha'
    },
    'recaptcha2': {
        'app': 'snowpenguin.django.recaptcha2',
        'pip': 'django-recaptcha2',
        'url': 'https://github.com/kbytesys/django-recaptcha2'
    },
    'recaptcha3': {
        'app': 'snowpenguin.django.recaptcha3',
        'pip': 'django-recaptcha3',
        'url': 'https://github.com/kbytesys/django-recaptcha3'
    },
}

if hasattr(settings, 'MULTI_CAPTCHA_ADMIN'):
    multi_captcha_admin_defaults = settings.MULTI_CAPTCHA_ADMIN
    for item in multi_captcha_admin_defaults.keys():
        if isinstance(multi_captcha_admin_defaults[item], dict):
            MULTI_CAPTCHA_ADMIN[item].update(multi_captcha_admin_defaults[item])
        else:
            MULTI_CAPTCHA_ADMIN[item] = multi_captcha_admin_defaults[item]

setattr(settings, 'MULTI_CAPTCHA_ADMIN', MULTI_CAPTCHA_ADMIN)

engine_name = settings.MULTI_CAPTCHA_ADMIN['engine']
try:
    engine = engines[engine_name]['app']
except KeyError:
    items = '\n'.join(
        [f"\t{item}\t{engines[item]['url']}" for item in engines.keys()]
    )
    error = f'''
please select engine between:
{items}

for example:
    MULTI_CAPTCHA_ADMIN = {{
        "engine": "simple-captcha
    }}"
    '''
    raise Exception(error)

if engine not in settings.INSTALLED_APPS:
    try:
        __import__(engine)
        settings.INSTALLED_APPS.append(engine)
    except ImportError:
        name = engines[engine_name]['pip']
        pip = engines[engine_name]['pip']
        url = engines[engine_name]['url']
        error = f'''
can not import {name}.
you can use "pip install {pip}"
website: {url}
        '''

        raise Exception(error)
