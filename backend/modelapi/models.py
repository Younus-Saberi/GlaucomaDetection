from django.db import models

# Create your models here.
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #result = models.CharField(max_length=50)

    def __str__(self):
        return self.image.name