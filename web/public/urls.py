from django.conf.urls import patterns, url
from web.public.views import *

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^about/', AboutView.as_view(), name='about'),
                       url(r'^contact/', ContactView.as_view(), name='contact'),
                       url(r'^hosting/', HostingView.as_view(), name='hosting'),
                       url(r'^cloud/', CloudView.as_view(), name='cloud'),
                       url(r'^services/', ServicesView.as_view(), name='services'),
                       url(r'^portfolio/', PortfolioView.as_view(), name='portfolio'),
)