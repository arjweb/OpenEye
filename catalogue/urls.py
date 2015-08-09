from django.conf.urls import url

# The dot operator means import from same package the current module is in
# ie views from catalogue
from . import views

urlpatterns = [
    # Pattern means ^ start $ end with nothing in between
    url(r'^$', 'catalogue.views.home', name='home'),
]
