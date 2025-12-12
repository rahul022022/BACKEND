from django.db import models

class Doctor(models.Model):
    """Doctor model used across practicals 3–9, 11–12, 21–22."""
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, help_text="For Google Maps examples")

    def __str__(self):
        return f"{self.name} - {self.specialty}"
