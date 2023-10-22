from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
]

