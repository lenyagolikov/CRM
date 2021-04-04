from django.contrib import admin
from django.urls import path, include

from .views import landing_page, LandingPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing-page'),
    path('leads/', include('leads.urls')),
]
