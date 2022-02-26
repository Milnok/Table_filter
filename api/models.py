from django.db import models


class Table(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()

    def __str__(self):
        return self.title
