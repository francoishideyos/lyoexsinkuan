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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Format: AreaCode+Number - 6592962824.")
    whatsapp_phone_number = models.CharField(default='0',help_text='Format: 85291790376',max_length=30, validators=[phone_regex]) # validators should be a list
    is_attending = models.NullBooleanField(default=None)
    is_child = models.BooleanField(default=False)

    @property
    def name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def __unicode__(self):
        return 'Guest: {} {}'.format(self.first_name, self.last_name)

