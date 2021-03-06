# Generated by Django 3.0.1 on 2020-07-21 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='AllergyDrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Allergy')),
            ],
            options={
                'db_table': 'allergies_drinks',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('allergy_drink', models.ManyToManyField(through='product.AllergyDrink', to='product.Allergy')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category')),
            ],
            options={
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_ml', models.IntegerField(default=0)),
                ('size_fluid_ounce', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nutrition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Nutrition')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('drink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Drink')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Menu'),
        ),
        migrations.AddField(
            model_name='drink',
            name='nutrition',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Nutrition'),
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('drink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Drink')),
            ],
            options={
                'db_table': 'descriptions',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Menu'),
        ),
        migrations.AddField(
            model_name='allergydrink',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Drink'),
        ),
    ]
