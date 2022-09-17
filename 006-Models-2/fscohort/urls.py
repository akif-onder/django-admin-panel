from django.urls import path

from .views import fscohort, subfolder

urlpatterns = [
    path('', fscohort),
    path('subfolder/', subfolder),
]