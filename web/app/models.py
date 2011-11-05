from django.db import models
from django.core.validators import MinValueValidator


class Event(models.Model):
    name       = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date   = models.DateTimeField('end date')

class Group(models.Model):
    name = models.CharField(max_length=200)

class Participant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    group      = models.ForeignKey(Group)
    join_date  = models.DateTimeField('joining date')

class ExpenseType(models.Model):
    name         = models.CharField(max_length=200)
    event        = models.ForeignKey(Event)
    participants = models.ManyToManyField(Participant, through="Weight")

class Expense(models.Model):
    expense_type = models.ForeignKey(ExpenseType)
    event        = models.ForeignKey(Event)
    amount       = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    payer        = models.ForeignKey(Participant, related_name="expense_payer")
    participants = models.ManyToManyField(Participant, db_table="expense_participants")


class Refund(models.Model):
    amount      = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    source      = models.ForeignKey(Participant, related_name="refund_source")
    destination = models.ForeignKey(Participant, related_name="refund_destination")

class Weight(models.Model):
    expense_type = models.ForeignKey(ExpenseType)
    participant  = models.ForeignKey(Participant)
    weight       = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])

