from django.db import models

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('candles', 'Candles'),
        ('shipping', 'Orders & Shipping'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question