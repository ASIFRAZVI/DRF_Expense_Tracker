from django.urls import path
from .views import Registration,Login,DashboardView

urlpatterns=[
    path('signup/', Registration.as_view(), name="signupuser" ),
    path('signin/', Login.as_view(), name="Loginuser"),
    path('dashboard/', DashboardView.as_view(), name="Dashboard")
]