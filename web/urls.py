from django.conf.urls.defaults import patterns, include, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from app.resources import ParticipantResource, EventResource, GroupResource, ExpenseTypeResource, WeightResource
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^participants/$',          ListOrCreateModelView.as_view(resource=ParticipantResource), name='model-resource-root'),
    url(r'^participant/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=ParticipantResource)),
    url(r'^events/$',          ListOrCreateModelView.as_view(resource=EventResource), name='model-resource-root'),
    url(r'^event/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=EventResource)),
    url(r'^groups/$',          ListOrCreateModelView.as_view(resource=GroupResource), name='model-resource-root'),
    url(r'^group/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=GroupResource)),
    url(r'^types/$',          ListOrCreateModelView.as_view(resource=ExpenseTypeResource), name='model-resource-root'),
    url(r'^type/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=ExpenseTypeResource)),
    url(r'^weights/$',          ListOrCreateModelView.as_view(resource=WeightResource), name='model-resource-root'),
    url(r'^weight/(?P<pk>[0-9]+)/$', InstanceModelView.as_view(resource=WeightResource)),
)
