from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=255)
    pub_date= models.DateTimeField()
    image= models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def summary(self):
        return self.body[:100]

  
    def publish_date(self):
        return self.pub_date.strftime('%b %e,%Y')
    
    def __str__(self):
        return self.title