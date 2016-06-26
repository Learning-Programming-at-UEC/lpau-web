import datetime

from django.db import models
from django.utils import timezone


class DataFile(models.Model):

    data = models.FileField(upload_to='files')
    file_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)

    def __str__(self):
        return self.file_name
