import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

EXCLUDE_FROM_PACKAGES = ['.vscode']

setup(
    name='django_invisible_recaptcha_admin',
    version='0.1.1-alpha',
    url='https://github.com/ricardochaves/django_invisible_recaptcha_admin',
    author='Ricardo Baltazar Chaves',
    author_email='ricardobchaves6@gmail.com',
    description='Invisible captcha in administrative login.',
    license='BSD',
    keywords=['django', 'recaptcha', 'field'],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    long_description=README,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Portuguese (Brazilian)',
    ],
    install_requires=[
          'django-nocaptcha-recaptcha-inv',
      ],
    zip_safe=False
)
