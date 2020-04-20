import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vugue.settings")
django.setup()

from product.models import *

ALLERGY_CSV_PATH = './db/csv/eighth_8_allergy.csv'

with open(ALLERGY_CSV_PATH, newline='') as allergy_csvfile:
	data_reader = csv.DictReader(allergy_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		print(row)

		Allergy.objects.create(
			name = row["\ufeffname"]
		)

		cnt += 1



ALLERGY_DRINK_CSV_PATH = './db/csv/nineth_9_allergydrink.csv'

with open(ALLERGY_DRINK_CSV_PATH, newline='') as allergy_drink_csvfile:
	data_reader = csv.DictReader(allergy_drink_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		print(row)

		allergy_id = Allergy.objects.get(id= int(row["\ufeffallergy_id"] ))
		drink_id = Drink.objects.get(id= int(row["drink_id"]))

		AllergyDrink.objects.create(
			allergy = allergy_id,
			drink = drink_id
		)

		cnt += 1

