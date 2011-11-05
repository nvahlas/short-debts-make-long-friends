from django.views.generic import TemplateView
from django.db.models import Q

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status
from djangorestframework import permissions

from app.calculator import Calculator
from app.models import Participant

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"

class EventsView(TemplateView):
    template_name = "events.html"
    
class BalanceView(TemplateView):
    template_name = "balance.html"

class CalculatorView(View):

    permissions = ( permissions.IsAuthenticated, )

    def get(self, request):
        participant = Participant.objects.get(
            Q(email=request.user.username) | Q(email=request.user.email)
        )
        event = participant.event.select_related()[0]
        calculator = Calculator(event)
        return Response(
            status.HTTP_200_OK,
            {
                "event"            : event,
                "amount"           : calculator.amount(),
                "participantAmount": calculator.participantAmount(participant)
            }
        )

