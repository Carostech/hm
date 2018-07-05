from django.db import models

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
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_id


