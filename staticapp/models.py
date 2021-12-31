from django.db import models

class table(models.Model):
    Name=models.CharField(max_length=50)
    Mobile_no=models.IntegerField()
    def __str__(self):
        return self.Name
