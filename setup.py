#!/usr/bin/env python
import codecs
from setuptools import setup, find_packages

try:
    from pypandoc import convert


    def read_me(filename):
        return convert(filename, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")


    def read_me(filename):
        return codecs.open(filename, encoding='utf-8').read()

setup(
    name='django-multi-captcha-admin',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    description=(
        'easy added captcha to login page of django admin'
    ),
    url='http://github.com/a-roomana/django-multi-captcha-admin',
    download_url='https://pypi.python.org/pypi/django-multi-captcha-admin/',
    author='Arman Roomana',
    author_email='roomana.arman@gmail.com',
    keywords="django captcha recaptcha recaptcha2 simple-captcha admin",
    license='MIT',
    platforms=['any'],
    install_requires=[
        "django",
    ],
    long_description=read_me('README.md'),
    use_2to3=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
