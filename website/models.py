from django.db import models


class Contact_us(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    number = models.IntegerField()
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
