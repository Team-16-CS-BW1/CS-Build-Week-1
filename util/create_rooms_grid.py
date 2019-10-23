from django.contrib.auth.models import User
from adventure.models import Player, Room
import random


Room.objects.all().delete()

world_matrix = [[None for _ in range(15)] for _ in range(15)]
#pick a random point in the grid, place a room there, and implement random walk algo to build rooms
start_x = random.choice(range(15))
start_y = random.choice(range(15))
#current x and y vars for each new room creation
x = start_x
y = start_y
#initialize room counter at 1
room_count = 1
#instantiate first room and save
room = Room(title = f'room{room_count}', description = f'desc{room_count}', x=x, y=y)
room.save()
#update the world_matrix position at x and y w/ the newly created room object
world_matrix[y][x] = room

#loop thru the random walk until 100 rooms have been created
while room_count < 100:
	directions = ['n', 's', 'e', 'w']
	reverse_map = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
	#get possible directions
	if room.x == 0: #left edge of grid, cant go west
		directions.remove('w')
	elif room.x == 14: #right edge, cant go east
		directions.remove('e')
	if room.y == 0: #top edge of grid, cant go north
		directions.remove('n')
	elif room.y == 14: #bottom edge, cant go south
		directions.remove('s')
	#random choice from poss directions
	direction = random.choice(directions)
	if direction == 'n':
		y -= 1 #its minus because rows go top to bottom in the matrix (0, 0 is upper left corner)
	elif direction == 's':
		y += 1
	elif direction == 'e':
		x += 1
	else: #west
		x -= 1
	prev_room = room
	#if no room exists in that direction:
	if world_matrix[y][x] is None:
		#increment room_count, instantiate the room, save it to the db, and update the world_matrix at x and y
		room_count += 1
		room = Room(title = f'room{room_count}', description = f'desc{room_count}', x=x, y=y)
		room.save()
		world_matrix[y][x] = room
	else: #room already there, just update current room with the room in that position
		room = world_matrix[y][x]
	#update the connections
	prev_room.connectRooms(room, direction)
	room.connectRooms(prev_room, reverse_map[direction])

players=Player.objects.all()
for p in players:
	p.currentRoom=world_matrix[start_y][start_x].id
	p.save()



# #start at 0,0 iterate across until x reaches 10, then move up one row
# room_coords = []
# for i in range(10):
# 	for j in range(10):
# 		room_coords.append((j,i))

# room_num = 1
# rooms = []
# for coord in room_coords:
# 	room = Room(title = f'room{room_num}', description = f'desc{room_num}', x=coord[0], y=coord[1])
# 	room.save()
# 	rooms.append(room)
# 	room_num += 1

# ### Link rooms together

# for room in rooms:
# 	if room.y < 9: #add connection to the north
# 		room_above = rooms[(room.id + 9) % 100]
# 		room.connectRooms(room_above, 'n')
# 	if room.y > 0: #add connection to the south
# 		room_below = rooms[(room.id - 11) % 100]
# 		room.connectRooms(room_below, 's')
# 	if room.x > 0: #add connection to the west
# 		room_left = rooms[(room.id -2) % 100]
# 		room.connectRooms(room_left, 'w')
# 	if room.x < 9: #add connection to the east
# 		room_right = rooms[room.id % 100]
# 		room.connectRooms(room_right, 'e')