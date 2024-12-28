from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    # path('blog_detail/<int:id>/', blog_detail, name='team_detail'),
    path('team_detail/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
    path('contact/', contact, name='contact'),
    path('counter/', counter, name='counter'),

]