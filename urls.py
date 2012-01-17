from django.conf.urls.defaults import patterns, include, url
from sindeo import views
from sindeo import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sindeo.views.home', name='home'),
    # url(r'^sindeo/', include('sindeo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    	(r'^admin/', include(admin.site.urls)),
	('^$', views.landing_page),
	(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
	(r'^meta/$', views.req_meta),
	(r'^search/$', views.search),
	(r'^subscribe/$', views.subscribe),
	(r'^subscribe/thanks/$', views.thanku),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
