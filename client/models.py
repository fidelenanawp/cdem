from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    occupation = models.CharField(blank=True, null=True, max_length=500)
    address = models.CharField(blank=True, null=True, max_length=500)
    event_location = models.CharField(blank=True, null=True, max_length=100)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    validated=models.BooleanField(default=False)
    validation_datetime = models.DateTimeField(blank=True, null=True)
    valided_by = models.CharField(blank=True, null=True, max_length=50)
    qrcode = models.CharField(blank=True, null=True, max_length=50)
    year_of_experience=models.CharField(blank=True, null=True, max_length=50)


    def __str__(self):
        return self.qrcode+ " | " + self.first_name+ " " + self.last_name

