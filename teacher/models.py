from django.db import models

class BroadwayTeacher(models.Model):
    name = models.CharField(max_length=255, null=True,help_text='Teacher name')
    address = models.CharField(max_length=33, null=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    
    def _str_(self):
        return f'{self.name}-{self.address}'