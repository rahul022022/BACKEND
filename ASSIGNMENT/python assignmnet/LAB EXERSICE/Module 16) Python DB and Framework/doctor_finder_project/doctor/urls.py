from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/add/', views.doctor_add, name='doctor_add'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('payment/', views.payment, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),

    path('map/', views.map_view, name='map'),

    # AJAX endpoints
    path('api/doctors/add/', views.api_doctor_add, name='api_doctor_add'),
    path('api/doctors/<int:pk>/edit/', views.api_doctor_edit, name='api_doctor_edit'),
    path('api/doctors/<int:pk>/delete/', views.api_doctor_delete, name='api_doctor_delete'),
]
