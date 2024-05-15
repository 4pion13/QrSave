from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                        .filter(status=InformationAboutBoxes.Status.PUBLISHED)

class InformationAboutBoxes(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    title = models.CharField(max_length=25)
    content = models.TextField()
    img = models.ImageField(upload_to='images/')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()




    def get_absolute_url(self):
        return reverse('qr:qr_detail', args=[self.publish.day, self.publish.month, self.publish.year, self.slug, self.id])

