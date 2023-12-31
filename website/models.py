from django.db import models

# Create your models here.
class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 12)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 30)
    Zipcode = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"