from django.db.models import Sum

from app.models import Participant, Expense, Weight

class Calculator(object):
    
    def __init__(self, event):
        self.event = event

    def amount(self):
        q = Expense.objects.filter(event=self.event).aggregate(Sum('amount')).values()[0]
        return q if q else 0
        
    def participantAmount(self, participant):
        total_group_debt = 0
        
        # participants belonging to the same group
        participants = Participant.objects.filter(group=participant.group)
        
        # event expenses
        event_expenses = Expense.objects.filter(event=self.event)
        for expense in event_expenses:
            expense_type = expense.expense_type
            
            weights = Weight.objects.filter(expense_type=expense_type)
            all_weights = 0
            group_weights = 0
            for w in weights:
                all_weights += w.weight
                if w.participant in participants:
                    group_weights += w.weight
            
            group_amount = 0
            if all_weights != 0:
                group_amount = expense.amount * group_weights / all_weights
            
            total_group_debt += (expense.amount if expense.payer in participants else 0) - group_amount
            
        return total_group_debt
    
    def participantBalance(self, participant):
        return None
