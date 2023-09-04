from django.db import models
from django.contrib.auth.models import User

cat =(('e','Electronics'),
      ('c','Clothing'),
      ('f','Furniture'),
      ('g','Grocery')
)

class Products(models.Model):
    image= models.ImageField(upload_to="imgs",null=True)
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=300)
    discount = models.IntegerField(blank=True,null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    category = models.CharField(choices=cat,max_length=3,null=False,default='e')
    def __str__(self):
        return self.name
class cartItem(models.Model):
    item = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.item.name
  

