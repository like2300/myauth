from django.urls import include, path
from .views import *
from django.views.generic import RedirectView



# ================= static urls 


static_urls = [
    path('', RedirectView.as_view(url='/home', permanent=False)),
    path('home', HomeView.as_view(), name='home'),
]
 



urlpatterns = [
    path('', include(static_urls)),
]
