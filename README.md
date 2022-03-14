# Bookstore
Bookstore project relied on docker with authorization and authentication system for restricting access to book contents.

## Installation:
1. Clone the repository:
```
https://github.com/Techinek/rango.git
```

2. Install all the needed packages:
```
pip install -r reqs.txt
```
3. Make migrations:
```
python manage.py makemigrations и $ python manage.py migrate
```
4. After making migrations run the following script to generate
categories and pages:
```
python populate_rango.py
```
5. Finally run local server:
```
python manage.py runserver
```
