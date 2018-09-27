from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=300)
    header_pl = models.TextField(
        default='empty')
    header_en = models.TextField(
        default='empty')
    content_pl = models.TextField(
        default='empty')
    content_en = models.TextField(
        default='empty')
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True)
    
    def __str__(self):
        return self.name
