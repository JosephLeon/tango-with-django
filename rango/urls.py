from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
