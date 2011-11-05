from datetime import datetime

from app.models import Participant, Group, Event, ExpenseType, Weight, Expense

group_a = Group(name="Family A")
group_a.save()
group_b = Group(name="Family B")
group_b.save()

event = Event(name="Holidays in Greece", start_date=datetime.now(), end_date=datetime.now())
event.save()

participant_a = Participant(
    first_name ="John",
    last_name  = "A",
    email      = "john@a.com",
    join_date  = datetime.now(),
    group      = group_a
)
participant_a.save()
participant_a.event = [event]
participant_a.save()

participant_b = Participant(
    first_name ="Jack",
    last_name  = "B",
    email      = "Jack@b.com",
    join_date  = datetime.now(),
    group      = group_b
)
participant_b.save()
participant_b.event = [event]
participant_b.save()

expense_type_food = ExpenseType(
    name  = "food",
    event = event
)
expense_type_food.save()

expense_type_hotel = ExpenseType(
    name  = "hotel",
    event = event
)
expense_type_hotel.save()

weight_a_food = Weight(
    expense_type = expense_type_food,
    participant  = participant_a,
    weight       = 0.7
)
weight_a_food.save()

weight_b_food = Weight(
    expense_type = expense_type_food,
    participant  = participant_b,
    weight       = 1.0
)
weight_b_food.save()

weight_a_hotel = Weight(
    expense_type = expense_type_hotel,
    participant  = participant_a,
    weight       = 1.0
)
weight_a_hotel.save()

weight_b_hotel = Weight(
    expense_type = expense_type_hotel,
    participant  = participant_b,
    weight       = 3.0
)
weight_b_hotel.save()

expense_john_food = Expense(
    event        = event,
    expense_type = expense_type_food,
    amount       = 150.4,
    payer        = participant_a,
    date         = datetime.now()
)
expense_john_food.save()
expense_john_food.participants = [participant_a, participant_b]
expense_john_food.save()

expense_jack_food = Expense(
    event        = event,
    expense_type = expense_type_food,
    amount       = 55.7,
    payer        = participant_b,
    date         = datetime.now()
)
expense_jack_food.save()
expense_jack_food.participants = [participant_a, participant_b]
expense_jack_food.save()

expense_john_hotel = Expense(
    event        = event,
    expense_type = expense_type_hotel,
    amount       = 220.0,
    payer        = participant_a,
    date         = datetime.now()
)
expense_john_hotel.save()
expense_john_hotel.participants = [participant_a, participant_b]
expense_john_hotel.save()

