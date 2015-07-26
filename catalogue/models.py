from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CatalogueItem(models.Model):
    title = models.CharField(max_length=80)
    # TODO check database max lengths for text fields
    description = models.CharField(max_length=2000, blank=True)
    topic_area = models.CharField(max_length=50)
    level = models.CharField(max_length=10)
    link = models.CharField(max_length=255)
    discovered_by = models.CharField(max_length=50)
    what_learn = models.CharField(max_length=2000, blank=True)
    how_apply = models.CharField(max_length=2000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # Python 2
        return self.title


class TopicArea(models.Model):
    name = models.CharField(max_length=40)
    # TODO check database max lengths for text fields
    definition = models.CharField(max_length=2000, blank=True)
    curator = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):  # Python 2
        return self.name


# Extending the default Django user model with Profile to allow addition of extra fields
class Profile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=2000, blank=True)
    pledge = models.CharField(max_length=2000, blank=True)
    is_curator = models.BooleanField(default=False)