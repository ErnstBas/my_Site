from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    description = models.TextField()
    image = models.FileField(upload_to="images")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

          
