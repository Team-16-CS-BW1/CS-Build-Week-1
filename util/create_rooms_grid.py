from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

#start at 0,0 iterate across until x reaches 10, then move up one row
room_coords = []
for i in range(10):
	for j in range(10):
		room_coords.append((j,i))

room_num = 1
rooms = []
for coord in room_coords:
	room = Room(title = f'room{room_num}', description = f'desc{room_num}', x=coord[0], y=coord[1])
	room.save()
	rooms.append(room)
	room_num += 1

### Link rooms together

for room in rooms:
	if room.y < 9: #add connection to the north
		room_above = rooms[(room.id + 9) % 100]
		room.connectRooms(room_above, 'n')
	if room.y > 0: #add connection to the south
		room_below = rooms[(room.id - 11) % 100]
		room.connectRooms(room_below, 's')
	if room.x > 0: #add connection to the west
		room_left = rooms[(room.id -2) % 100]
		room.connectRooms(room_left, 'w')
	if room.x < 9: #add connection to the east
		room_right = rooms[room.id % 100]
		room.connectRooms(room_right, 'e')

players=Player.objects.all()

for p in players:
	p.currentRoom=rooms[0].id
	p.save()