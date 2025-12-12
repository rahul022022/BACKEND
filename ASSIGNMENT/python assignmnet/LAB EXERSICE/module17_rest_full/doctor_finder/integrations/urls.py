from django.urls import path

from .views import (
    WeatherView,
    GeocodeView,
    GitHubReposView,
    TwitterTweetsView,
    CountryInfoView,
    SendGridEmailView,
    TwilioOTPView,
    StripePaymentView,
    DoctorLocationsView,
)

urlpatterns = [
    path("weather/", WeatherView.as_view(), name="weather"),
    path("geocode/", GeocodeView.as_view(), name="geocode"),
    path("github/repos/", GitHubReposView.as_view(), name="github-repos"),
    path("twitter/tweets/", TwitterTweetsView.as_view(), name="twitter-tweets"),
    path("countries/info/", CountryInfoView.as_view(), name="country-info"),
    path("email/sendgrid/", SendGridEmailView.as_view(), name="sendgrid-email"),
    path("sms/twilio/", TwilioOTPView.as_view(), name="twilio-otp"),
    path("payments/stripe/", StripePaymentView.as_view(), name="stripe-payment"),
    path("doctors/locations/", DoctorLocationsView.as_view(), name="doctor-locations"),
]
