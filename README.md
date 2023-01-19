# Django URL Shortener
This is a simple URL shortener application built using Django. It allows users to input a long URL and receive a shortened version that can be easily shared.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python 3.9
Django 

## Installing
#### Clone the repository to your local machine:
```python
git clone https://github.com/your-username/django-url-shortener.git
```
#### Install the required packages:
```python
pip install django
```
#### Migrate the database (may be necessary):
```python
python manage.py makemigrations
python manage.py migrate
```
#### Run the development server:
```python
python manage.py runserver
```
## Using the URL shortener
Go to http://127.0.0.1:8000/ in your web browser.
Input the long URL you wish to shorten in the form field.
Click the "Shorten" button.
The shortened URL will be displayed on the page. You can now share this shortened URL with others.
## Built With
Django - The web framework used
Python - Programming language
## Authors
Zane Hirning - Initial work - https://github.com/zanehirning
