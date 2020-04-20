import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbucks_sqlite.settings")
django.setup()

from product.models import *

NUTRITION_CSV_PATH = './db/csv/fourth_4_nutrition.csv'

with open(NUTRITION_CSV_PATH, newline='') as nutrition_csvfile:
	data_reader = csv.DictReader(nutrition_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		print(row)

		Nutrition.objects.create(
			one_serving_kcal = float(row["\ufeffone_serving_kcal"]),
			sodium_mg = float(row["sodium_mg"]),
			saturated_fat_g = float(row["saturated_fat_g"]),
			sugars_g = float(row["sugars_g"]),
			protein_g = float(row["protein_g"]),
			caffeine_mg = float(row["caffeine_mg"])

		)

		cnt += 1


DRINK_CSV_PATH = './db/csv/third_3_drink.csv'
with open(DRINK_CSV_PATH, newline='') as drink_csvfile:
	data_reader = csv.DictReader(drink_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		if row["menu_id"] == "1":
			menu = Menu.objects.get(id=1)
		elif row["menu_id"] == "2":
			menu = Menu.objects.get(id=2)

		if row["category_id"]=="1":
			category = Category.objects.get(id=1)
		elif row["category_id"]=="2":
			category = Category.objects.get(id=2)
		elif row["category_id"]=="3":
			category = Category.objects.get(id=3)
		
		nutrition_id=Nutrition.objects.get(id=cnt)

		Drink.objects.create(
			name = row['\ufeffname'],
			menu = menu,
			category = category,
			nutrition = nutrition_id
		)

		cnt += 1
