from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    current_room = {
        'id': room.id,
        'x': room.x,
        'y': room.y,
        'n_to': room.n_to,
        's_to': room.s_to,
        'e_to': room.e_to,
        'w_to': room.w_to,
    }
    # trying out map stuff here:
    rooms = Room.objects.all()
    world_map = {
        "rooms": [
                {
                    'id': i.id,
                    'x': i.x,
                    'y': i.y,
                    'n_to': i.n_to,
                    's_to': i.s_to,
                    'e_to': i.e_to,
                    'w_to': i.w_to,
                } for i in rooms]
    }
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name': player.user.username, 'title': room.title, 'description': room.description, 'players': players, 'world_map': world_map, 'current_room': current_room}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs = {"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom = nextRoomID
        player.save()
        # room = player.room()
        current_room = {
            'id': room.id,
            'x': room.x,
            'y': room.y,
            'n_to': room.n_to,
            's_to': room.s_to,
            'e_to': room.e_to,
            'w_to': room.w_to,
        }
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name': player.user.username, 'title': nextRoom.title, 'description': nextRoom.description, 'players': players, 'current_room': current_room, 'error_msg': ""}, safe=True)
    else:
        players = room.playerNames(player_id)
        current_room = {
            'id': room.id,
            'x': room.x,
            'y': room.y,
            'n_to': room.n_to,
            's_to': room.s_to,
            'e_to': room.e_to,
            'w_to': room.w_to,
        }
        return JsonResponse({'name': player.user.username, 'title': room.title, 'description': room.description, 'players': players, 'current_room': current_room, 'error_msg': "You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error': "Not yet implemented"}, safe=True, status=500)
