from django.db import models
from shorty.models import shortyURL
# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, Shortyinstance):
        if isinstance(Shortyinstance, shortyURL):
            obj, created = self.get_or_create(shorty_url=Shortyinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    shorty_url = models.OneToOneField(shortyURL)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
