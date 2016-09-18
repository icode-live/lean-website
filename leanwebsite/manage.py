###
# SETTINGS ::..
##
from settings import *


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


urlpatterns = (  # '',
        url(r'^$', index, name="homepage"),
)


###
# tests
##
def test_hello_world():
    assert "hello_world" == "hello_world"

###
# WSGI ::..
##

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()

if __name__ == "__main__":
    import sys

    from django.core.management import execute_from_command_line


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    execute_from_command_line(sys.argv)
