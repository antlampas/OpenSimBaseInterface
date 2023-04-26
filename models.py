#Author: antlampas
#Date: 2023-04-26
#This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from django.db import models

class Setting(models.Model):
    option = models.CharField(max_length=26)
    value  = models.CharField(max_length=256)
    models.UniqueConstraint(fields=['option'],name='unique_option')
    def __str__(self):
        return self.option + " = " + self.value
    def __unicode__(self):
        return self.option + " = " + self.value

class Grid(models.Model):
    name = models.CharField(max_length=26)
    models.UniqueConstraint(fields=['name'],name='unique_grid_name')
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Simulator(models.Model):
    name = models.CharField(max_length=26)
    grid = models.ForeignKey("Grid",on_delete=models.CASCADE,default=None)
    models.UniqueConstraint(fields=['name','grid'],name='unique_simulator_name')
    def __str__(self):
        return self.name + " on " + self.grid.name
    def __unicode__(self):
        return self.name + " on " + self.grid.name

class Region(models.Model):
    name      = models.CharField(max_length=26)
    simulator = models.ForeignKey("Simulator",on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['name','simulator'],name='unique_region_in_grid_simulator')
    def __str__(self):
        return self.name + " on " + self.simulator.__str__()
    def __unicode__(self):
        return self.name + " on " + self.simulator.__str__()

class Avatar(models.Model):
    firstName = models.CharField(max_length=26)
    lastName  = models.CharField(max_length=26)
    username  = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['firstName','lastName','username'],name='unique_user')
    def __str__(self):
        return self.username.username
    def __unicode__(self):
        return self.username.username
    

class OwnerRegionAssociation(models.Model):
    username = models.ForeignKey("Avatar",on_delete=models.CASCADE)
    region   = models.ForeignKey("Region",on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['username','region'],name='unique_user_region_association')
    def __str__(self):
        return self.region.__str__() + " owned by " + self.username.__str__()
    def __unicode__(self):
        return self.region.__str__() + " owned by " + self.username.__str__()