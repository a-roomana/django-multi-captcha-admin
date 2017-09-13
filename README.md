[![PyPi Version](https://img.shields.io/pypi/v/django-multi-captcha-admin.svg)](https://pypi.python.org/pypi/django-multi-captcha-admin)
[![GitHub stars](https://img.shields.io/github/stars/a-roomana/django-multi-captcha-admin.svg?style=social)](https://github.com/a-roomana/django-multi-captcha-admin)
# django-multi-captcha-admin

easy added captcha to login page of django admin

----------
**DEPENDENCY**

To use this module you need to install django and one of engine captcha. which you can install it with easy_install or pip

----------
**INSTALL**

    pip install django-multi-captcha-admin   

----------
**USAGE**

settings.py
```python
INSTALLED_APPS = [
	'multi_captcha_admin',
	'django.contrib.admin',
	
	'other_apps',
]

# defaults
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}
```

command
```bash
pip install [django-simple-captcha | django-recaptcha | django-recaptcha2]
```
----------
**ENGINES**

We use the famous engines for render CAPTCHA. You need to install one of them, then according document add the name to the settings.

 - [simple-captcha](https://github.com/mbi/django-simple-captcha)
 - [recaptcha](https://github.com/praekelt/django-recaptcha)
 - [recaptcha2](https://github.com/kbytesys/django-recaptcha2)

For more information, please go to the engine site.

----------
**EXAMPLE**

command
```bash
pip install django-mulit-captcha django-recaptcha2
```
settings.py
```python
INSTALLED_APPS = [
	'multi_captcha_admin',
	'django.contrib.admin',
	
	'other_apps',
]

MULTI_CAPTCHA_ADMIN = {
    'engine': 'recaptcha2',
}

# recaptcha2
RECAPTCHA_PUBLIC_KEY = 'public key'
RECAPTCHA_PRIVATE_KEY = 'private key'
```

----------
**RESULTS**

[recaptcha2](https://github.com/kbytesys/django-recaptcha2)

![captcha of recaptcha2](http://bayanbox.ir/view/2417903076718397977/reCaptcha2.png)


[recaptcha](https://github.com/praekelt/django-recaptcha)

![captcha of recaptcha](http://bayanbox.ir/view/2014387201108001651/reCaptcha.png)


[simple captcha](https://github.com/mbi/django-simple-captcha)

![captcha of recaptcha](http://bayanbox.ir/view/721684099022571779/simple-captcha.png)
