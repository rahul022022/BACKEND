MODULE 17 – REST FRAMEWORK PRACTICALS (DOCTOR FINDER PROJECT)
=============================================================

FOLDERS INSIDE ZIP
------------------
1) 01_joke_api/
   - random_joke.py              -> Practical 1 (simple API consumer)

2) 02_django_setup/
   - requirements.txt            -> Practical 2 (project requirements)
   - setup_django_project.py     -> optional helper script

3) doctor_finder/
   - Django project containing:
     * doctors app      -> Practicals 3,4,5,6,7,8,9,11,12, 22/23
     * accounts app     -> Practical 13 (token-based auth)
     * integrations app -> Practicals 14–21 (OpenWeather, Maps, GitHub, Twitter,
                           REST Countries, SendGrid, Twilio, Stripe, locations)
STEP 1 – CREATE VIRTUAL ENV
---------------------------
On Windows (PowerShell):

    python -m venv venv
    venv\Scripts\activate

On Linux/macOS:

    python3 -m venv venv
    source venv/bin/activate

STEP 2 – INSTALL REQUIREMENTS
-----------------------------
Go inside the 02_django_setup folder and install packages:

    cd 02_django_setup
    pip install -r requirements.txt

(You can ignore setup_django_project.py because the project is ALREADY
created inside doctor_finder/.)

STEP 3 – RUN MIGRATIONS
-----------------------
Go to the Django project folder (where manage.py is):

    cd ../doctor_finder

Run migrations to create the SQLite database:

    python manage.py migrate

(Optional) create a superuser for admin:

    python manage.py createsuperuser

STEP 4 – RUN DEVELOPMENT SERVER
-------------------------------
Still inside doctor_finder:

    python manage.py runserver

Django will run on http://127.0.0.1:8000/

IMPORTANT API ENDPOINTS
-----------------------

DOCTORS CRUD + PAGINATION (Practicals 3,4,5,6,7,8,9,11,12)
---------------------------------------------------------
List (GET) + Create (POST):

    GET/POST  http://127.0.0.1:8000/api/doctors/

Detail / Update / Delete doctor by id:

    GET/PUT/PATCH/DELETE  http://127.0.0.1:8000/api/doctors/<id>/

Example POST body (JSON):

    {
        "name": "Rahul Sharma",
        "specialty": "Cardiologist",
        "contact_details": "9876543210",
        "city": "Ahmedabad"
    }

Pagination: use ?page=1, ?page=2 etc.

AUTHENTICATION (Practical 13)
-----------------------------
Register:

    POST http://127.0.0.1:8000/api/auth/register/

Login (get token):

    POST http://127.0.0.1:8000/api/auth/login/

Logout:

    POST http://127.0.0.1:8000/api/auth/logout/

EXTERNAL INTEGRATIONS (14–21)
-----------------------------
Weather (OpenWeatherMap):

    GET /api/integrations/weather/?city=Ahmedabad

Geocoding (Google Maps):

    GET /api/integrations/geocode/?address=Ahmedabad

GitHub:

    GET  /api/integrations/github/repos/?username=<your-github-username>
    POST /api/integrations/github/repos/      (requires GITHUB_TOKEN env variable)

Twitter:

    GET /api/integrations/twitter/tweets/?username=<twitter-username>

REST Countries:

    GET /api/integrations/countries/info/?country=India

SendGrid Email (after registration):

    POST /api/integrations/email/sendgrid/
    body: { "email": "user@example.com" }
    (requires SENDGRID_API_KEY env variable)

Twilio SMS OTP:

    POST /api/integrations/sms/twilio/
    body: { "phone": "+911234567890" }
    (requires TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_PHONE)

Stripe Payment:

    POST /api/integrations/payments/stripe/
    body: { "amount": 1000, "currency": "usd" }
    (requires STRIPE_SECRET_KEY)

Doctor Locations (Google Maps front-end usage):
-----------------------------------------------
    GET /api/integrations/doctors/locations/?city=Ahmedabad

The API will return doctor objects with city. In a real project you would use
these together with Google Maps JavaScript API on the frontend to show markers
on a map.

SIMPLE API CONSUMER SCRIPT (Practical 1)
----------------------------------------
To run the random joke script:

    cd 01_joke_api
    python random_joke.py

This will call a public joke API and print a random joke in the console.
