# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Mark(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    zip = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    open_at = models.TimeField(auto_now=False, auto_now_add=False)
    close_at = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    
    def __unicode__(self):
        return self.title