from django.conf.urls.defaults import *

from microblog.models import Note

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)',admin.site.root),
    (r'',include('microblog.urls')),
    #(r'^list/$',object_list,dict(queryset=Note.objects.all().order_by('-id'),paginate_by=5)),
    #(r'^add/$',create_object,dict(model=Note,post_save_redirect='/list/')),
    # Example:
    # (r'^manoush/', include('manoush.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)

if setteings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
