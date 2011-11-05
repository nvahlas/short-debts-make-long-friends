from django.db import models
from django.core.validators import MinValueValidator


class Event(models.Model):
    name       = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date   = models.DateTimeField('end date')

    def __unicode__(self):
        return u'<Event %s>' % (self.name)

class Group(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'<Group %s>' % (self.name)

class Participant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    email      = models.EmailField()
    group      = models.ForeignKey(Group)
    join_date  = models.DateTimeField('joining date')
    event      = models.ManyToManyField(Event)

    def __unicode__(self):
        return u'<Person %s %s>' % (self.first_name, self.last_name)

class ExpenseType(models.Model):
    name         = models.CharField(max_length=200)
    event        = models.ForeignKey(Event)
    participants = models.ManyToManyField(Participant, through="Weight")

    def __unicode__(self):
        return u'<ExpenseType %s for %s>' % (self.name, self.event)

class Expense(models.Model):
    expense_type = models.ForeignKey(ExpenseType)
    event        = models.ForeignKey(Event)
    amount       = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    payer        = models.ForeignKey(Participant, related_name="expense_payer")
    participants = models.ManyToManyField(Participant, db_table="expense_participants")

    def __unicode__(self):
        return u'<Expense of %s>' % (self.amount)


class Refund(models.Model):
    amount      = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    source      = models.ForeignKey(Participant, related_name="refund_source")
    destination = models.ForeignKey(Participant, related_name="refund_destination")

    def __unicode__(self):
        return u'<Refund of %s from %s to %s>' % (self.amount, self.source, self.destination)

class Weight(models.Model):
    expense_type = models.ForeignKey(ExpenseType)
    participant  = models.ForeignKey(Participant)
    weight       = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])

    def __unicode__(self):
        return u'<Weight of %s for %s and %s>' % (self.weight, self.participant, self.expense_type)

