from datetime import datetime

from django.views.generic import TemplateView
from django.db.models import Q

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status
from djangorestframework import permissions

from app.calculator import Calculator
from app.models import Participant, Event, ExpenseType, Expense

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "login.html"

class EventsView(TemplateView):
    template_name = "events.html"
    
class BalanceView(TemplateView):
    template_name = "balance.html"
    
    def __init__(self, *args, **kwargs):
        TemplateView.__init__(self, *args, **kwargs)
        self.participant = None
    
    def get(self, request):
        self.participant = Participant.objects.get(
            Q(email=request.user.username) | Q(email=request.user.email)
        )
        return TemplateView.get(self,request)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BalanceView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['participant'] = self.participant
        return context

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
                "participant"      : participant,
                "amount"           : calculator.amount(),
                "participantAmount": calculator.participantAmount(participant)
            }
        )

class EventParticipantsView(View):

    permissions = ( permissions.IsAuthenticated, )

    def get(self, request, **kwargs):
        event = Event.objects.get(**kwargs)
        return Response(
            status.HTTP_200_OK,
            Participant.objects.filter(event=event)
        )

class EventExpenseTypesView(View):

    permissions = ( permissions.IsAuthenticated, )

    def get(self, request, **kwargs):
        event = Event.objects.get(**kwargs)
        return Response(
            status.HTTP_200_OK,
            ExpenseType.objects.filter(event=event)
        )

class ExpenseAddView(View):

    def post(self, request, **kwargs):
        print request, kwargs
        expense = Expense(
            expense_type = ExpenseType.objects.get(id=self.CONTENT["expense_type"]["id"]),
            amount = self.CONTENT["amount"],
            event = Event.objects.get(id=self.CONTENT["event"]["id"]),
            payer = Participant.objects.get(id=self.CONTENT["payer"]["id"]),
            date = datetime.now()
        )
        expense.save()
        expense.participants = [Participant.objects.get(id=participant["id"]) for participant in self.CONTENT["participants"]]
        expense.save()

