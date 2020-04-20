from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    name          = models.CharField(max_length=50)
    menu          = models.ForeignKey('Menu', on_delete = models.SET_NULL, null=True)
    category      = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    nutrition     = models.OneToOneField('Nutrition', on_delete = models.SET_NULL, null=True)
    allergy_drink = models.ManyToManyField('Allergy', through='AllergyDrink')

    class Meta:
        db_table = 'drinks'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg        = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g  = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g         = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g        = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg      = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.URLField(max_length= 2000)
    drink     = models.ForeignKey('Drink', on_delete = models.SET_NULL,  null=True)

    class Meta:
        db_table = 'images'

class Description(models.Model):
    description = models.CharField(max_length=1000)
    drink       = models.ForeignKey('Drink', on_delete = models.SET_NULL,  null=True)

    class Meta:
        db_table = 'descriptions'

class Size(models.Model):
    name             = models.CharField(max_length=45)
    size_ml          = models.IntegerField(default = 0)
    size_fluid_ounce = models.DecimalField(max_digits=10, decimal_places=2)
    nutrition        = models.ForeignKey('Nutrition', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'sizes'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = 'allergies'

class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete = models.SET_NULL, null=True)
    drink   = models.ForeignKey('Drink', on_delete = models.SET_NULL, null=True)

    class Meta:
        db_table = 'allergies_drinks'
