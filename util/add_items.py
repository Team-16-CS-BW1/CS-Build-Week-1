from django.contrib.auth.models import User
from adventure.models import Player, Room, Item, RoomItem, PlayerItem
import random

items_dict = {'Hammer':'use this item carefully- Dont smash your thumb', 
         'Sword': 'Try not to impale yourself!!',
         'Toothpick': 'Looks like you have some seaweed stuck in your teeth.', 
         'Axe': 'If the door locks behind you, this will come in handy.', 
         'Shovel': 'Use this to dig up buried treasure', 
         'Sandwich': 'Hungry? Hope you like Turkey', 
         'Canteen': 'Thirsty?',
         'Flashlight': 'Illuminate the path w/ this handy flashlight', 
         'Key':'This key could unlock a grand fortune.', 
         'Grenade': 'Blow something up with this- ', 
         'Body Armor': 'This will keep you safe from IEDs', 
         'Bag of Gold Coins': "Its your lucky day! You're rich!",
         'Football': "Pass the time by tossin the ol' pigskin", 
         'Stray Kitten': 'Meowwww! Aww how cute',
         'Snowboard': 'Carve up the slopes', 
         'Box of Matches': 'It gets pretty cold here at night, hope you know how to build a fire', 
         'Telescope': 'Who doesnt love a good stargazing?',
         'Rope': 'Classic rope- so versatile', 
         'Hiking Boots': 'Feet getting sore? These should help.', 
         'Raincoat': "Fashion faux pas maybe, but at least you'll be dry", 
         'Magnifying Glass': 'Search for clues, start a fire, or kill some ants- your choice.', 
         'Jetpack': 'After you find the treasure, make youre escape in style'}

#populate the db w/ all the items
for key in items_dict.keys():
    title = key
    description = items_dict[key]
    item = Item(title=title, description=description)
    item.save()

#load all the items into a list:
items = Item.objects.all()
#50/50 chance of populating a room w/ an item
choices = [True, False]
#load lal the rooms into a list
rooms = Room.objects.all()
#iterate thru each room, if choice lands on True, grab random item and add it to the room
for room in rooms:
    choice = random.choice(choices)
    if choice:
        item = random.choice(items)
        room_item = RoomItem(room=room, item=item)
        room_item.save()
