from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
date = datetime.now()

print(date)
print('*' * 80)
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        context = {
            "show": Shows.objects.all()
        }
        grab = Shows.objects.filter(title=postData['title'])
        if len(postData['title']) < 2:
            errors['title'] = "Title should be more than 2 characters"
            print(grab)
        if len(grab) > 0:
            errors['title'] = "Title already exists"
        if len(postData['network']) < 2:
            errors['network'] = "Network should be more than 2 characters"
        if len(postData['date']) < 0:
            errors['date'] = "Please input a date"
        if postData['date'] > str(date):
            errors['date'] = "You aint from the future"
        if len(postData['description']) > 0:
            if len(postData['description']) < 10:
                errors['location'] = "Description must be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    descriptions = models.TextField()
    release_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowsManager()
    def __repr__(self):
        return f"<Shows object: {self.id} ({self.title})>"