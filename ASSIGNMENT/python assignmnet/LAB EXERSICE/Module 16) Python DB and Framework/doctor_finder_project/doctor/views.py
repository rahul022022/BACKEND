from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Doctor, PatientProfile
from .forms import DoctorForm, PatientRegistrationForm, PatientProfileForm

def home(request):
    return render(request, 'doctor/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})

@login_required
def doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully!')
            return redirect('doctor:doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_form.html', {'form': form, 'title': 'Add Doctor'})

@login_required
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully!')
            return redirect('doctor:doctor_detail', pk=pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor/doctor_form.html', {'form': form, 'title': 'Edit Doctor'})

@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctor:doctor_list')
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('doctor:login')
    else:
        form = PatientRegistrationForm()
        profile_form = PatientProfileForm()
    return render(request, 'doctor/register.html', {'form': form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('doctor:home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'doctor/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('doctor:home')

@login_required
def profile(request):
    try:
        profile = request.user.patientprofile
    except PatientProfile.DoesNotExist:
        profile = PatientProfile(user=request.user)
        profile.save()
    if request.method == 'POST':
        profile_form = PatientProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated!')
            return redirect('doctor:profile')
    else:
        profile_form = PatientProfileForm(instance=profile)
    return render(request, 'doctor/profile.html', {'profile_form': profile_form})

@login_required
def payment(request):
    # This is a simplified placeholder view. In real Paytm integration,
    # you would generate a checksum and redirect to Paytm payment page.
    if request.method == 'POST':
        # pretend payment is processed
        return redirect('doctor:payment_success')
    return render(request, 'doctor/payment.html')

@login_required
def payment_success(request):
    return render(request, 'doctor/payment_success.html')

def map_view(request):
    doctors = Doctor.objects.exclude(latitude__isnull=True, longitude__isnull=True)
    return render(request, 'doctor/map.html', {'doctors': doctors})

# AJAX views
@login_required
def api_doctor_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return JsonResponse({'success': True, 'id': doctor.id, 'name': doctor.name})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
def api_doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            return JsonResponse({'success': True, 'id': doctor.id, 'name': doctor.name})
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
def api_doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
