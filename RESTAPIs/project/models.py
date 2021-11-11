from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.project_id)