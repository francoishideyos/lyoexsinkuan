from __future__ import unicode_literals

import datetime
from django.db import models
from django.dispatch import receiver
from django.core.validators import RegexValidator


# Create your models here.


# these will determine the default formality of correspondence

class Guest(models.Model):
    """
    A single guest
    """
    STATE_CHOICES = (
        (True, u'Will Attend'),
        (False, u'Will Not Attend'),
    )

    name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Format: AreaCode+Number - 6592962824.")
    whatsapp_number = models.CharField(max_length=13) # validators should be a list
    is_attending = models.BooleanField(default=None,choices=STATE_CHOICES)
    # is_child = models.BooleanField(default=False)
    comments = models.CharField(max_length=1000)

    # @property
    # def name(self):
    #     return u'{} {}'.format(self.first_name, self.last_name)

    # def __unicode__(self):
    #     return 'Guest: {} {}'.format(self.first_name, self.last_name)

