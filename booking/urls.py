from django.urls import path
from .views import  register, home, login,submit_appointment,appointment_success, Teams

urlpatterns = [
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('Teams/', Teams, name='Teams'),
    path('index/', home, name='index'),  # This should render index.html
    path('submit_appointment/', submit_appointment, name='submit_appointment'),  # Adjust the URL as needed
    path('appointment_success/', appointment_success, name='appointment_success'),
]
