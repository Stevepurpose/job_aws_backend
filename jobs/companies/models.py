from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
     company_name = models.CharField(max_length=255, verbose_name='Company Name')
     role = models.CharField(max_length=255, verbose_name='Role')
     applied = models.BooleanField(verbose_name ='Applied', default=False)
     Discussions= models.TextField(default=False)
     offer = models.BooleanField(verbose_name='Offer', default=False)
     advert_start = models.DateTimeField(verbose_name='Advert Date')
     close_date = models.DateTimeField(verbose_name ='Advert Closes', null = True, editable = True)
     owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)

     class Meta:
          ordering = ['company_name']


     def __str__(self):
        return self.company_name
