from django.db import models

class TestTable(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=52)
    quantity = models.IntegerField()
    distance = models.IntegerField()

    def return_query(self):
        pass