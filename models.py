from django.db import models
import uuid

class hello(models.Model):
    id= models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    email = models.EmailField()
    active= models.BooleanField(default=True)
    
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.date}, {self.time}, {self.email}, {self.active}'

