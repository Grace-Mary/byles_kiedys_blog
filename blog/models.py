from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=200)
    description = models.TextField(default="Two-three sentences as a description")
    text = models.TextField()
    text_two = models.TextField(default="N/A")
    text_three = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_one = models.ImageField(default='image.png', blank=True)
    image_two = models.ImageField(default='image2.png', blank=True)
    image_three = models.ImageField(default='image3.png', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
