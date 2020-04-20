# create database vugue character set utf8mb4 collate utf8mb4_general_ci;
import os
os.chdir("..")
print("Current dir for migration files=", end=""), print(os.getcwd())
a = os.system('find . -path "*/migrations/*.py"')
print(a)
b = os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
print(b)

os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

os.chdir("./db")
print("Current dir for db sync=", end=""), print(os.getcwd())
os.system('python initialize_total_database.py')
