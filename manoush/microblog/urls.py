from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object

from microblog.models import Note

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from forms import NoteForm
#from views import post_note, user_home

urlpatterns = patterns('',
    (r'^list/$',object_list,dict(queryset=Note.objects.all().order_by('-id'),paginate_by=5)),
    (r'^add/$',create_object,dict(model=Note,post_save_redirect='/list/')),
    #url(r'/$', post_note, name='post_note'),
    #url(r'profile/(?P<username>\w+)/$', user_home, name='user_home'),
    #(r'$', object_list, dict(queryset=Note.objects.all().order_by('-id').select_related(depth=1),
    #paginate_by=20, extra_context=dict(form=NoteForm())), 'microblog_home'),
)
