from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

rooms = Room.objects.all()

adjectives = ['Horror', 'Confusion', 'Wonder', 'Doom', 'Solitude', 
             'Ecstacy', 'Sadness', 'Despair', 'Mirrors', 'Fire',
             'Tears', 'Happiness', 'Eternal Suffering', 'Death',
             'Randomness']
nouns = ['Dungeon', 'Cave', 'Valley', 'Room', 'Prison', 'Dwelling',
        'Castle', 'Forest', 'Island', 'Ship', 'House', 'Den', 'Library',
        'Lighthouse', 'Bedroom', 'Graveyard', 'Warehouse', 'Fortress']
descriptions = ['Why is it so dark? Did you bring a flashlight', 'What is that smell??', 
                'I think you should go back.', 'Gettig tired in this maze- At least this room has booze!'
                'I think I just saw a rat!', 'You should stay a while, this place seems cozy.',
                'Oh my, this place seems magical!', 'Seems like a great place to take a nap.. ZZZZ',
                "I hope you brought a snack- I don't see any food anywhere!", 
                'Watch out for boobie traps!', 'I wonder if theres buried treasure here!']
                

for room in rooms:
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    desc = random.choice(descriptions)
    room.title = f'{noun} of {adj}!'
    room.description = f'Welcome to the {room.title}! {desc}'
    room.save()