from django.urls import include, path
from .views import signupfunc

urlpatterns = [
    path('signup/', signupfunc),
]