from django.db import models

# Create your models here.
class download(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=700, blank=False)
    image = models.ImageField(upload_to='partner/', blank=False)

    def __str__(self):
        return self.name
