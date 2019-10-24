from django.contrib import admin
from .models import Player, Room

# Register your models here.
admin.site.register(Player)
admin.site.register(Room)
admin.site.register(Item)
admin.site.register(RoomItem)
admin.site.register(PlayerItem)
