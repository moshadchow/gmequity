from django.db import models
from ckeditor.fields import RichTextField

class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title

class partner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=700, blank=False)
    image = models.ImageField(upload_to='partner/', blank=False)

    def __str__(self):
        return self.name

class advisor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to='partner/', blank=False)
    quote = models.TextField(max_length=700, blank=False)

    def __str__(self):
        return self.name

class service(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to='service/', blank=False)
    
    def __str__(self):
        return self.name

class approach(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to='approach/', blank=False)
    
    def __str__(self):
        return self.name

class strategy(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to='strategy/', blank=False)
    
    def __str__(self):
        return self.name

class fund_info(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.name

class fund_protect(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.name