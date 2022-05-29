import os
import datetime
from django.db import models
from numpy import require

def get_upload_path(instance, filename):
    today_date = datetime.datetime.today().date()
    return os.path.join("static/data_files", str(today_date), filename)

# Create your models here.
class DataTable(models.Model):
    data_file = models.FileField(upload_to=get_upload_path)
    chisqr = models.FloatField(blank=True, null=True)

    @property
    def file_name(self):
        return os.path.basename(str(self.data_file))