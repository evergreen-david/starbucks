import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vugue.settings")
django.setup()

from product.models import *

IMAGE_CSV_PATH = './db/csv/sixth_6_image.csv'

with open(IMAGE_CSV_PATH, newline='') as image_csvfile:
	data_reader = csv.DictReader(image_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		print(row)

		drink = Drink.objects.get(id=int(row["drink_id"] ))


		Image.objects.create(
			image_url = row["\ufeffimage_url"],
			drink = drink
		)

		cnt += 1


DESCRIPTION_CSV_PATH = './db/csv/seventh_7_description.csv'
with open(DESCRIPTION_CSV_PATH, newline='') as description_csvfile:
	data_reader = csv.DictReader(description_csvfile)

	menu = 0
	category = 0
	cnt = 1
	for row in data_reader:
		
		drink = Drink.objects.get(id=int(row["drink_id"] ))

		Description.objects.create(
			description = row['\ufeffdescription'],
			drink=drink
		)

		cnt += 1
