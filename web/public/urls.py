from django.conf.urls import patterns, url
from web.public.views import *

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^home2', Home2View.as_view(), name='home2'),
                       url(r'^about/', AboutView.as_view(), name='about'),
                       url(r'^contact/', ContactView.as_view(), name='contact'),
                       url(r'^projects/', ProjectView.as_view(), name='projects'),
                       url(r'^projects2/', Project2ColView.as_view(), name='projects2'),
                       url(r'^project_single/', ProjectSingleView.as_view(), name='single_project'),

                       url(r'^construction/', ConstructionView.as_view(), name='construction'),
                       url(r'^services/', ServicesView.as_view(), name='services'),
                       url(r'^building/', BuildingView.as_view(), name='building'),
                       url(r'^isolation/', IsolationView.as_view(), name='isolation'),
                       url(r'^painting/', PaintingView.as_view(), name='painting'),
                       url(r'^electricy/', ElectricyView.as_view(), name='electricy'),
                       url(r'^projecting/', ProjectingView.as_view(), name='projecting'),

                       url(r'^blog/', BlogView.as_view(), name='blog'),
                       url(r'^single_post/', SinglePostView.as_view(), name='single_post'),
                       url(r'^404_error/', ErrorView.as_view(), name='404_error'),
)