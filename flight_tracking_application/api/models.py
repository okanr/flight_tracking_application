from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    take_off = models.DateTimeField()
    landing = models.DateTimeField()
    to_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING,
                                   verbose_name='to', related_name='to_airport')
    from_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING,
                                     verbose_name='from', related_name='from_airport')

    def __str__(self):
        return self.flight_number
