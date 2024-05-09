from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from meals.models import Meals
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Numéro_de_téléphone  = models.CharField(max_length=15,default=+216)  # Ajoutez le champ pour le numéro de téléphone

    Repas = models.ForeignKey(Meals, null=True, on_delete=models.SET_NULL)
    Quantité= models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=3)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculer le prix total basé sur la quantité du repas et son prix unitaire
        self.total_price = self.Repas.price * self.Quantité
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.pk} - meal: {self.Repas } - Quantity: {self.Quantité} - Total: {self.total_price} - Numéro_de_téléphone: {self.Numéro_de_téléphone} "
