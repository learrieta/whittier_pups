from django.db import models

# Create your models here.
    
class BabyDogs(models.Model):
    is_sold = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    description = models.TextField(null=True, blank= True)
    feature_image = models.ImageField(null=True, blank=True)
    page_picture1 = models.ImageField(null=True, blank=True)
    page_picture2 = models.ImageField(null=True, blank=True)
    page_picture3 = models.ImageField(null=True, blank=True)
    page_picture4 = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)



    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        img = ''
        try:
            if self.feature_image.url:
                img = self.feature_image.url
        except:
            img = ''

        return img
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    