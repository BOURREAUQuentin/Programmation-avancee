from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10, null=True, unique=True)
    price_ht = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fabrication_date = models.DateTimeField(blank=True, default=timezone.now)
    status = models.ForeignKey("Status", on_delete=models.CASCADE, default=0)
    
    def __str__(self):
        return "Le produit {0} (code = {1}) au prix de {2}€ depuis le {3}. Il a un statut {4}.".format(self.name, self.code, self.price_ht, self.fabrication_date, self.status.libelle)

class ProductItem(models.Model):
    code_item = models.CharField(max_length=10, null=True, unique=True)
    color = models.CharField(max_length=100)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return "L'élément de code {0} appartient au produit ({1}){2} de couleur {3}.".format(self.code_item, self.product.code, self.product.name, self.color)
    
class Status(models.Model):
    numero = models.IntegerField(null=True, unique=True)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return "Le statut {0} de numéro {1}.".format(self.libelle, self.numero)