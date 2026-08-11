from django.urls import path
from portfolio_app.views import *

urlpatterns = [
    path('', home_view, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]