from django.db import models
from decimal import Decimal

class Piece(models.Model):
    quantite = models.PositiveIntegerField()
    designation = models.CharField(max_length=50, unique=True)
    voiture = models.CharField(max_length=255, null=True, blank=True)
    
    prix_brut = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_net = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_montant = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    reduction = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))  # en pourcentage

    def __str__(self):
        return f"{self.designation} - {self.voiture} (x{self.quantite}) | {self.prix_vente_reduction}€"

    @property
    def prix_vente_reduction(self):
        """Prix de vente après application de la réduction."""
        return self.prix_vente * (1 - (self.reduction / 100))

    @property
    def est_disponible(self):
        """Retourne True si la pièce est disponible (quantité > 0)."""
        return self.quantite > 0
