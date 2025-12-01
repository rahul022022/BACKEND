from django.contrib import admin
from .models import Doctor, PatientProfile

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'location', 'availability', 'email', 'phone')
    search_fields = ('name', 'specialization', 'location')

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
