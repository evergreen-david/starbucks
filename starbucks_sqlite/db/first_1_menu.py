import csv
import os
import django
import sys

os.chdir("..")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbucks_sqlite.settings")
django.setup()

from product.models import *

CSV_PATH = './db/csv/first_1_menu.csv'

with open(CSV_PATH, newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)

	for row in data_reader:
		print(row)
		Menu.objects.create(
			name = row['\ufeffname']
		)
