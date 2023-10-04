from django.conf.urls import url
from terms.views import TermsAndConditions

urlpatterns = [
    url(r'^$', TermsAndConditions , name='home'),
]