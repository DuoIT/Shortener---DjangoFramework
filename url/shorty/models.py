from django.db import models
from .utils import code_generator, create_shortcode
# Create your models here.


class shortyURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(shortyURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self, items=None):
        qs = shortyURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_code += 1
        return "New codes made: {i}".format(i=new_code)


class shortyURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, default='abc123', unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = shortyURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(shortyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
