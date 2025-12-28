from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify
from unidecode import unidecode


class PartPlace(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PartBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class PartSeries(models.Model):
    brand = models.ForeignKey(PartBrand, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)


class PartType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Part(models.Model):
    part_type = models.ForeignKey(PartType, on_delete=models.CASCADE, related_name='parttype')
    part_number = models.CharField(max_length=100, default='nothing')
    brand = models.ForeignKey(PartBrand, on_delete=models.CASCADE, null=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_series = models.ForeignKey(PartSeries, on_delete=models.CASCADE, null=True, related_name='parts_by_series')
    availability = models.BooleanField(default=True)
    condition = models.CharField(
        max_length=10,
        choices=[
            ('used', 'Б/у'),
            ('new', 'Новая'),
        ],
        default='new')
    made_in = models.ForeignKey(PartPlace, on_delete=models.CASCADE, related_name='part_place', null=True)
    slug = models.SlugField(blank=True, null=True)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.part_type.name))
        super().save(*args, **kwargs)
