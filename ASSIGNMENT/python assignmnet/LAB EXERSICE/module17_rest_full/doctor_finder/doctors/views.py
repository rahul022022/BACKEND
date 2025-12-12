from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer

# Practical 3,4,5,7,8,9,11,12 – CRUD + pagination + POST creation

class DoctorListCreateView(generics.ListCreateAPIView):
    """GET: list doctors (paginated), POST: create new doctor."""
    queryset = Doctor.objects.all().order_by("id")
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """GET/PUT/PATCH/DELETE single doctor by id."""
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]
