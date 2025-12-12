from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/doctors/", include("doctors.urls")),           # CRUD + pagination
    path("api/auth/", include("accounts.urls")),             # register/login/logout, token
    path("api/integrations/", include("integrations.urls")), # external APIs (weather, maps, etc.)
    path("accounts/", include("allauth.urls")),              # google login routes
]
