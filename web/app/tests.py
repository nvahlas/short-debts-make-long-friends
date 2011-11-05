from django.utils import unittest
from app.models import Event, Expense
from app.calculator import Calculator

#To Run: python manage.py test app.CalculatorTest

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.event = Event(pk=1)
        self.calculator = Calculator(self.event)
    
    def testAmount(self):
        self.assertEqual(self.calculator.amount(), 100)