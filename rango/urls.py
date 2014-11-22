from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
