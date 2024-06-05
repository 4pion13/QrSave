from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from pytils.translit import slugify

class Test(models.Manager):
    test = models.CharField(max_length=25)

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
    title = models.CharField(max_length=50)
    content = models.TextField()
    box_id = models.CharField(max_length=32,null=True)
    img = models.ImageField(upload_to='images/')
    img_photo = models.ImageField(upload_to='in_box/')
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(InformationAboutBoxes, self).save(*args, **kwargs)




    def get_absolute_url(self):
        return reverse('qr:qr_detail', args=[self.box_id])



    def _str_(self):
        return self.title
