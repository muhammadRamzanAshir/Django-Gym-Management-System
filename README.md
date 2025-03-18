# Django-Gym-Management-System
This is a Django-based dynamic gym management system designed to streamline gym operations. Full Dynamic site .
![Pasted image](https://github.com/user-attachments/assets/caedef9c-ed27-4da4-a24a-1279f910a76b)
Dynamic Homepage: The first page is fully dynamic, allowing admins to update content such as banners, pricing plans, featured trainers, and workout sections directly from the Django admin panel.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

Django

PostgreSQL/MySQL (or SQLite for development)

Steps

Clone the repository

git clone https://github.com/your-repo/django-gym.git
cd django-gym

Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Configure database

Update settings.py with your database credentials.

Apply migrations:

python manage.py migrate

Create a superuser (for admin access)

python manage.py createsuperuser

Run the development server

python manage.py runserver

Usage

Access the system via http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

Register/Login as a gym member

Manage workouts, trainers, and payments from the admin panel

Dynamic Homepage Management: Update homepage content via the admin panel without modifying code.

Technologies Used

Backend: Django, Django REST Framework

Database: PostgreSQL/MySQL/SQLite

Frontend: HTML, CSS, JavaScript, Bootstrap

Authentication: Django Auth

Future Enhancements

Mobile app integration

AI-based workout recommendations

Automated billing system

Contributing

Pull requests are welcome! Please fork the repo and submit a PR for review.
