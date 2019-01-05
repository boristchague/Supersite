

from django.db import models
from django.utils import timezone


def Announcement (models):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    departure = models.CharField(max_length=30)
    arrival = models.charField(max_length=30)
    weight = models.IntegerField(verbose_name="weight available")
    publishDate = models.DateTimeField(default=timezone.now, verbose_name="Date of publication")

    class Meta: 
        verbose_name = "shipment Ad"
        ordering = ['publishDate']

    def __str__(self):
        return self.destination


def User (models):
    
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta: 
            verbose_name = "advertiser"
            ordering = ['firstName']

    def __str__(self):
         return self.firstName

