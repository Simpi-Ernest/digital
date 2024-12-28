from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    # path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(template_name='Registration/login.html'), name='login'),

    path('logout/', logout_view, name='logout'),

]