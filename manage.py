###
# SETTINGS ::..
##
import sys
import os
from django.conf import settings


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# unclutter the main project directory
#sys.path.append(os.path.join(BASE_DIR, 'apps'))
DEBUG = True 
settings.configure(
	DEBUG = DEBUG,		#DEBUG=True,
	DEBUG_TOOLBAR = DEBUG,
	TEMPLATE_DEBUG = DEBUG,
        SECRET_KEY='hehehe!@#$', 
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.staticfiles',
        ),
        TEMPLATE_DIRS=(
            os.path.join(BASE_DIR, 'templates'),
        ),
        STATICFILES_DIRS=(
            os.path.join(BASE_DIR, 'static'),
			os.path.join(BASE_DIR, 'src'),
        ),
	DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'dev.db'),
        }
	},
	STATIC_URL ='/static/',
	STATIC_ROOT =os.path.join(BASE_DIR, 'static_root'), 
	ADMINS = (
    		('lean-website:admin', 'admin@admin.com'),
	),
    	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend',
)



###
# VIEWS ::..
##
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

###
# URLS ::..
##
from django.conf.urls import url

urlpatterns = (#'',
        url(r'^$', index, name="homepage"),
)



###
# tests
##
def test_hello_world():
    assert "hello_world" == "hello_world"

###
# MANAGE ::..
##
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

