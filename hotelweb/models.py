from django.db import models
from django.utils import timezone

# Create your models here.
# course categories.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length= 100, null=False)
    id_number = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, null=False)
    has_baby = models.CharField(max_length=10, null=False)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user_id

class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length = 20, null=False)
    room_type = models.CharField(max_length = 50, null=False)
    floor = models.CharField(max_length=10, null=False)
    cleaning_status = models.CharField(max_length=10, null = False)

    def __str__(self):
        return self.room_id




