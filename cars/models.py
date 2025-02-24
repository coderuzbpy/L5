from django.db import models
# Create your models here.


class Cars(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='car_images/', blank=True, null=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Cars'

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

