from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5 , decimal_places=3)
    preperation_time =models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Meals , self).save(*args , **kwargs)



    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)



    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name






class Review(models.Model):
   meals = models.ForeignKey(Meals, on_delete=models.CASCADE, related_name='reviews')
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
   comment = models.TextField(max_length=1000)
   slug = models.SlugField(blank=True, null=True)

   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'Review by {self.user} on {self.meals}'