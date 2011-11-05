from django.contrib.auth import authenticate, login
from django.http import HttpRequest

from djangorestframework.views import View
from djangorestframework.resources import ModelResource
from djangorestframework.response import Response
from djangorestframework import status

from app.models import Participant, Group, Event, ExpenseType, Weight
from app.forms import AuthenticationForm

class ParticipantResource(ModelResource):
    model = Participant
    fields = ('first_name', 'last_name', 'join_date', 'group', 'url')
    ordering = ('first_name', 'last_name',)

class GroupResource(ModelResource):
    model = Group
    fields = ('name', 'url')
    ordering = ('name')

class EventResource(ModelResource):
    model = Event
    fields = ('name', 'start_date', 'end_date', 'url')
    ordering = ('start_date')

class ExpenseTypeResource(ModelResource):
    model = ExpenseType
    fields = ('name', 'event', 'participants', 'url')
    ordering = ('name')
    
class WeightResource(ModelResource):
    model = Weight
    fields = ('expense_type', 'participant', 'weight', 'url')
    ordering = ('participant')

class AuthenticationView(View):
    
    form = AuthenticationForm
    
    def post(self, request):
        user = authenticate(username=self.CONTENT['username'], password=self.CONTENT['password'])
        if user is None:
            return Response(status.HTTP_400_BAD_REQUEST)
        else:
            login(request, user)
            return Response(status.HTTP_200_OK)