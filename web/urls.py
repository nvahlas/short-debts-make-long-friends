from django.conf.urls.defaults import patterns, include, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from app.resources import ParticipantResource, EventResource, GroupResource
from app.resources import ExpenseTypeResource, WeightResource
from app.resources import AuthenticationView, ExpenseResource
from app.views import IndexView, LoginView, EventsView, CalculatorView
from app.views import BalanceView, EventParticipantsView, EventExpenseTypesView
from app.views import ExpenseAddView

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^rest/participants/$',                 ListOrCreateModelView.as_view(resource=ParticipantResource), name='model-resource-root'),
    url(r'^rest/participant/(?P<pk>[0-9]+)/$',   InstanceModelView.as_view(resource=ParticipantResource)),
    url(r'^rest/events/$',                       ListOrCreateModelView.as_view(resource=EventResource), name='model-resource-root'),
    url(r'^rest/event/(?P<pk>[0-9]+)/$',         InstanceModelView.as_view(resource=EventResource)),
    url(r'^rest/groups/$',                       ListOrCreateModelView.as_view(resource=GroupResource), name='model-resource-root'),
    url(r'^rest/group/(?P<pk>[0-9]+)/$',         InstanceModelView.as_view(resource=GroupResource)),
    url(r'^rest/types/$',                        ListOrCreateModelView.as_view(resource=ExpenseTypeResource), name='model-resource-root'),
    url(r'^rest/type/(?P<pk>[0-9]+)/$',          InstanceModelView.as_view(resource=ExpenseTypeResource)),
    url(r'^rest/weights/$',                      ListOrCreateModelView.as_view(resource=WeightResource), name='model-resource-root'),
    url(r'^rest/weight/(?P<pk>[0-9]+)/$',        InstanceModelView.as_view(resource=WeightResource)),
    url(r'^rest/expenses/$',                     ListOrCreateModelView.as_view(resource=ExpenseResource)),
    url(r'^rest/expense/(?P<pk>[0-9]+)/$',       InstanceModelView.as_view(resource=ExpenseResource)),
    url(r'^rest/authenticate$',                  AuthenticationView.as_view()),
    url(r'^rest/add_expense$',                   ExpenseAddView.as_view()),
    url(r'^rest/calculator$',                    CalculatorView.as_view()),
    url(r'^rest/event/(?P<pk>[0-9+])/participants$', EventParticipantsView.as_view()),
    url(r'^rest/event/(?P<pk>[0-9+])/expense_types$', EventExpenseTypesView.as_view()),
    url(r'^$',                                   login_required( IndexView.as_view() )),
    url(r'^login$',                              LoginView.as_view()),
    url(r'^events$',                             login_required( EventsView.as_view() )),
    url(r'^balance$',                            login_required( BalanceView.as_view() )),
)
