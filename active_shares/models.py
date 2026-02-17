from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Shareholder(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shareholder', verbose_name="Utilisateur")
    company_name = models.CharField(max_length=200, verbose_name="Nom de l’entreprise")
    description = models.TextField(blank=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    class Meta:
        verbose_name = "Actionnaire"
        verbose_name_plural = "Actionnaires"
        ordering = ['-created_at']

    def __str__(self):
        return self.company_name

class Buyer(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='buyer',
        verbose_name="Utilisateur"
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name = "Prénom"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name = "Nom"
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Date de création"
    )

    class Meta:
        verbose_name = "Acheteur"
        verbose_name_plural = "Acheteurs"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Share(models.Model):

    shareholder = models.ForeignKey(
        Shareholder,
        on_delete=models.CASCADE,
        related_name='shares',
        verbose_name="Actionnaire"
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Titre de l’action"
    )
    description = models.TextField(
        verbose_name="Description"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix unitaire"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantité disponible"
    )
    buyers = models.ManyToManyField(
        Buyer,
        through='Purchase',
        related_name='purchased_shares',
        verbose_name="Acheteurs"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Dernière modification"
    )

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.shareholder.company_name}"

    @property
    def total_sold(self):
        result = self.purchases.aggregate(total=Sum('quantity'))['total']
        return result or 0

    def is_available(self):
        return self.total_sold < self.quantity

    def remaining_quantity(self):
        return self.quantity - self.total_sold

class Purchase(models.Model):
    
    buyer = models.ForeignKey(
        Buyer, 
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    share = models.ForeignKey(
        Share, 
        on_delete=models.CASCADE,
        related_name='purchases'
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Nombre de parts achetées",
        default=1
    )
    purchased_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'achat"
    )

    class Meta:
        verbose_name = "Achat"
        verbose_name_plural = "Achats"
        ordering = ['-purchased_at']

    def __str__(self):
        return f"{self.buyer} a acheté {self.quantity} parts de {self.share.title}"