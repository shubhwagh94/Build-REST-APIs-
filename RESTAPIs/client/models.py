from django.db import models


# Create your models here.
class Client(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return str(self.client_id)
