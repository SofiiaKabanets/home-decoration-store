from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.DecimalField(max_digits=5, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-valid_from']
        verbose_name_plural = 'Vouchers'
        
    def __str__(self):
        return self.code