from djangorestframework.resources import ModelResource
from app.models import Participant, Group, Event, ExpenseType, Weight

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