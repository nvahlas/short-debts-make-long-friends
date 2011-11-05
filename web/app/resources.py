from djangorestframework.resources import ModelResource
from app.models import Participant

class ParticipantResource(ModelResource):
    model = Participant
    fields = ('name', 'pub_date', 'url')
    ordering = ('name',)


