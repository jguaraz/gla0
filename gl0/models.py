from django.db import models
from django.utils import timezone
# Create your models here.
class G(models.Model):
    id_p = models.PositiveSmallIntegerField(default=1)
    datetime = models.CharField(max_length=20)
    value = models.PositiveSmallIntegerField()

    def publish(self):
        '''self.id_p = 1'''
        self.save()

    def __str__(self):
        return str(self.value)