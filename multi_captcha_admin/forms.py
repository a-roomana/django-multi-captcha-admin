from django.conf import settings
from django.contrib.admin.forms import AdminAuthenticationForm


def get_captcha_field():
    engine = settings.MULTI_CAPTCHA_ADMIN['engine']

    if engine == 'simple-captcha':
        from captcha.fields import CaptchaField
        return CaptchaField()

    elif engine == 'recaptcha':
        from captcha.fields import ReCaptchaField
        return ReCaptchaField()

    elif engine == 'recaptcha2':
        from snowpenguin.django.recaptcha2.fields import ReCaptchaField
        from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

        return ReCaptchaField(widget=ReCaptchaWidget())
    
    elif engine == 'recaptcha3':
        from snowpenguin.django.recaptcha3.fields import ReCaptchaField
        from snowpenguin.django.recaptcha3.widgets import ReCaptchaHiddenInput
        
        return ReCaptchaField(widget=ReCaptchaHiddenInput())

class MultiCaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MultiCaptchaAdminAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = get_captcha_field()
