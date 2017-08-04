###############################
Django Invisible Recaptcha Admin
###############################

###############################
How do I get set up?
###############################

Instale usando PyPI:

    pip install django_invisible_recaptcha_admin

Add the app ``django_invisible_recaptcha_admin`` to ``settings.py``



    INSTALLED_APPS = (
        'django_invisible_recaptcha_admin',
        
        'nocaptcha_recaptcha',

        ...
    )


Add to ``urls.py`` from:

    from django_invisible_recaptcha_admin.admin import my_admin

    urlpatterns = [
        #url(r'^admin/', include(admin.site.urls)),
        
        url(r'^admin/', include(my_admin.urls)),
    ]


###############################
To Do
###############################

* Create tests
* Organize the code according to the `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_

