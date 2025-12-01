Doctor Finder - Django Project
==============================

This project implements a simple **Doctor Finder** web application built with Django.

It covers:
- HTML, CSS, JavaScript in Django templates
- Django MVT architecture
- Forms and authentication (login, logout, registration)
- Django ORM and CRUD operations
- AJAX-based CRUD for doctors
- Basic (demo) Paytm payment flow placeholder
- Google Maps integration placeholder
- Social authentication skeleton using django-allauth
- Admin panel customization
- SQLite database

## Setup Instructions

1. Create and activate virtual environment (example for Windows):

```bash
python -m venv venv
venv\Scripts\activate
```

On Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create superuser for admin panel:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser at http://127.0.0.1:8000/

### Google Maps

Set environment variable `GOOGLE_MAPS_API_KEY` with your key or replace it directly in `map.html`.

### Paytm

`payment` view is a **demo placeholder**. To integrate real Paytm gateway, you need to:
- Install official Paytm SDK and follow their documentation.
- Generate checksum and redirect to Paytm payment URL.
- Handle callback in `payment_success` view.

### Social Auth (Google/Facebook)

`django-allauth` is installed and basic settings are in `settings.py`.

To fully enable Google/Facebook login:
- Add your client IDs and secrets in the Django admin under **Social Accounts**.
- Update allowed redirect URLs in Google/Facebook console.

The project should run without errors even if you don't configure these keys,
as long as you don't open the social login URLs.
