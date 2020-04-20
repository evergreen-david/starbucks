import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbucks_sqlite.settings")
django.setup()

from product.models import *

SIZE_CSV_PATH = './db/csv/fifth_5_size.csv'

with open(SIZE_CSV_PATH, newline='') as size_csvfile:
	data_reader = csv.DictReader(size_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		print(row)

		nutrition = Nutrition.objects.get(id=int(row["nutrition_id"] ))


		Size.objects.create(
			name = row["\ufeffname"],
			size_ml = int( row["size_ml"]),
			size_fluid_ounce = float( row["size_fluid_ounce"]),
			nutrition = nutrition
		)

		cnt += 1
