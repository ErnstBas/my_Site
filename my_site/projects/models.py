
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="images")
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['date']
