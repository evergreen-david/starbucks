import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vugue.settings")
django.setup()

from product.models import *

CSV_PATH = './db/csv/second_2_category.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	menu = 0
	for row in data_reader:
		print(row)

		if row["menu"] == "1":
			menu = Menu.objects.get(id=1)
		elif row["menu"] == "2":
			menu = Menu.objects.get(id=2)

		Category.objects.create(
			name = row['\ufeffname'],
			menu = menu
		)
