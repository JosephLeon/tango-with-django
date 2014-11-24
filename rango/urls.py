from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from rango import views
# from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^restricted/$', views.restricted, name='restircted'),
    url(r'^logout/$', views.user_logout, name='logout'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
