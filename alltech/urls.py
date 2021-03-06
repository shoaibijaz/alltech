from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^', include("web.public.urls")),
                       )

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
                        )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)