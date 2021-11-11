from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user_id)
