import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

# Twilio, SendGrid, Stripe imports – wrapped in try/except so project still runs
try:
    from twilio.rest import Client as TwilioClient
except Exception:  # pragma: no cover - for environments without twilio installed
    TwilioClient = None

try:
    import sendgrid
    from sendgrid.helpers.mail import Mail
except Exception:  # pragma: no cover
    sendgrid = None
    Mail = None

try:
    import stripe
except Exception:  # pragma: no cover
    stripe = None

# 14) OpenWeatherMap API
class WeatherView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        city = request.query_params.get("city", "London")
        api_key = os.environ.get("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        r = requests.get(url, timeout=10)
        data = r.json()
        return Response(data)

# 15) Google Geocoding API (address -> lat/lng)
class GeocodeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        address = request.query_params.get("address")
        if not address:
            return Response({"detail": "address query param required"}, status=400)
        api_key = os.environ.get("GOOGLE_MAPS_API_KEY", "YOUR_API_KEY_HERE")
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": address, "key": api_key}
        r = requests.get(url, params=params, timeout=10)
        return Response(r.json())

# 16) GitHub API – list repos and create repo (requires personal access token)
class GitHubReposView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        username = request.query_params.get("username")
        if not username:
            return Response({"detail": "username required"}, status=400)
        url = f"https://api.github.com/users/{username}/repos"
        r = requests.get(url, timeout=10)
        return Response(r.json())

    def post(self, request):
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            return Response({"detail": "Set GITHUB_TOKEN env var first"}, status=400)
        name = request.data.get("name", "test-repo-from-api")
        url = "https://api.github.com/user/repos"
        headers = {"Authorization": f"token {token}"}
        payload = {"name": name, "auto_init": True}
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        return Response(r.json(), status=r.status_code)

# 17) Twitter API – latest 5 tweets of a user
class TwitterTweetsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        username = request.query_params.get("username")
        bearer = os.environ.get("TWITTER_BEARER_TOKEN")
        if not username or not bearer:
            return Response({"detail": "username and TWITTER_BEARER_TOKEN required"}, status=400)
        url = f"https://api.twitter.com/2/tweets/search/recent"
        params = {"query": f"from:{username}", "max_results": 5}
        headers = {"Authorization": f"Bearer {bearer}"}
        r = requests.get(url, params=params, headers=headers, timeout=10)
        return Response(r.json())

# 18) REST Countries API – details of a given country
class CountryInfoView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        country = request.query_params.get("country")
        if not country:
            return Response({"detail": "country query param required"}, status=400)
        url = f"https://restcountries.com/v3.1/name/{country}"
        r = requests.get(url, timeout=10)
        return Response(r.json())

# 19) SendGrid – send confirmation email after registration
class SendGridEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if sendgrid is None or Mail is None:
            return Response({"detail": "sendgrid package not installed"}, status=500)
        api_key = os.environ.get("SENDGRID_API_KEY")
        if not api_key:
            return Response({"detail": "SENDGRID_API_KEY env var required"}, status=400)

        to_email = request.data.get("email")
        if not to_email:
            return Response({"detail": "email field required"}, status=400)

        sg = sendgrid.SendGridAPIClient(api_key)
        message = Mail(
            from_email="no-reply@example.com",
            to_emails=to_email,
            subject="Registration successful",
            html_content="<p>Thank you for registering!</p>",
        )
        response = sg.send(message)
        return Response({"status_code": response.status_code})

# 20) Twilio – send OTP SMS
class TwilioOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if TwilioClient is None:
            return Response({"detail": "twilio package not installed"}, status=500)

        phone = request.data.get("phone")
        if not phone:
            return Response({"detail": "phone field required"}, status=400)

        account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        from_phone = os.environ.get("TWILIO_FROM_PHONE")

        if not all([account_sid, auth_token, from_phone]):
            return Response({"detail": "Twilio env vars not set"}, status=400)

        client = TwilioClient(account_sid, auth_token)
        otp = "123456"  # in real life generate random
        body = f"Your OTP is {otp}"
        message = client.messages.create(body=body, from_=from_phone, to=phone)
        return Response({"sid": message.sid, "otp": otp})

# 21) Stripe – payment for doctor appointment
class StripePaymentView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if stripe is None:
            return Response({"detail": "stripe package not installed"}, status=500)

        stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
        if not stripe.api_key:
            return Response({"detail": "STRIPE_SECRET_KEY env var required"}, status=400)

        amount = int(request.data.get("amount", 1000))  # in cents
        currency = request.data.get("currency", "usd")

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )
        return Response({"client_secret": payment_intent.client_secret})

# 22/23) Google Maps display doctor locations in a city – here we just return coordinates
class DoctorLocationsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        city = request.query_params.get("city")
        doctors = Doctor.objects.all()
        if city:
            doctors = doctors.filter(city__iexact=city)
        serializer = DoctorSerializer(doctors, many=True)
        # Frontend map (JS/React) would use these results + Google Maps JS API to plot
        return Response(serializer.data)
