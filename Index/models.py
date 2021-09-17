from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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
    description = RichTextUploadingField()
    css_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class approach(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    css_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class strategy(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    css_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class fund_info(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class financial_info(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class company_goal(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class sip(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class board_member(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.name

class fund_protect(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class faq (models.Model):
    question = models.CharField(max_length=200)
    answer =  RichTextUploadingField()
    
    def __str__(self):
        return self.question

class news (models.Model):
    name = models.CharField(max_length=200)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name

class tax (models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    
    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=200,blank=False)
    subject = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=700,blank=False)

    def __str__(self):
        return self.subject