from django.db import models

# Create your models here.

class category(models.Model):
      name=models.CharField(max_length=50)
      def __str__(self):
            return self.name
      




class medicines(models.Model):
      x=[
            ('available','available'),
            ('unavailable','unavailable') 
      ]

      name=models.CharField(max_length=50)
      usage=models.TextField(max_length=100 ,null=True ,blank=True)
      medicine_photo=models.ImageField(upload_to='photos', null=True, blank=True)
      price=models.DecimalField(max_digits=5,decimal_places=2)
      active=models.BooleanField(default=True, null=True ,blank=True)
      status=models.CharField(max_length=50 , choices=x ,null=True ,blank=True)
      last_pieces=models.IntegerField( null=True ,blank=True)
      category=models.ForeignKey(category,on_delete=models.PROTECT,null=True ,blank=True)


      def __str__(self):
            return self.name

