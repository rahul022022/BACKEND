from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    # /api/doctors/
    path("", DoctorListCreateView.as_view(), name="doctor-list-create"),
    # /api/doctors/<id>/
    path("<int:pk>/", DoctorRetrieveUpdateDestroyView.as_view(), name="doctor-detail"),
]
