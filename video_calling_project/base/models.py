from django.db import models

# Create your models here.
# This is using ORM, so the sql becomes easy for us.

# This will store the users-name, uid, room name, so we can give it when the frontend 
# asks 
class RoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    insession = models.BooleanField(default=True)

    def __str__(self):
        return self.name