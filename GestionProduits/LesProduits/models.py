from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    code = models.IntegerField()
    price_ht = models.FloatField()
    fabrication_date = models.DateField(auto_now_add=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    
    def __unicode__(self):
        return "Le produit ({0}){1} au prix de {2}€ depuis le {3}. Il a un statut {4}".format(self.name, self.code, self.price_ht, self.fabrication_date, self.status.libelle)

class ProductItem(models.Model):
    code_item = models.IntegerField()
    color = models.CharField(max_length=100)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __unicode__(self):
        return "L'élément de code {0} appartient au produit ({1}){2} de couleur {3}".format(self.code_item, self.product.code, self.product.name, self.color)
    
class Status(models.Model):
    numero = models.IntegerField()
    libelle = models.CharField(max_length=100)

    def __unicode__(self):
        return "{0} {1}".format(self.numero, self.libelle)