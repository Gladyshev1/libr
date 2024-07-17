from django.db import models
class book(models.Model):
    name=models.CharField(max_length=50)
    author= models.CharField(max_length=50)
    col=models.IntegerField()
    img=models.ImageField(blank=True,upload_to='images')
    description=models.TextField(max_length=2000)
    def __str__(self):
        return self.name



class take(models.Model):
    who=models.CharField(max_length=50)
    when=models.CharField(max_length=50)
    kom=models.TextField(max_length=2000)
    what=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.who