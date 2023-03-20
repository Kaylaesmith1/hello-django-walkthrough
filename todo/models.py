from django.db import models


class Item(models.Model):
    # This means you can't leave the name blank
    name = models.CharField(max_length=50, null=False, blank=False)
    # to ensure 'to do' items aren't marked as 'not done' by default
    done = models.BooleanField(null=False, blank=False, default=False)

    # this returns the name that WE put into the form not the 'item object' etc
    def __str__(self):
        return self.name
