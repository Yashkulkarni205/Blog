from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'image')
    privacy = models.TextChoices('privacy','public private')
    privacy = models.CharField(max_length =10, choices=privacy.choices)

    def __str__(self):
        return self.name

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path) # Open image using self
        
        new_img = (240, 360)
        img.thumbnail(new_img)
        img.save(self.image.path)
