from django.urls import path
from .views import ActivityCreateView, report,home

urlpatterns = [
    path('', home, name='home'),
    path('api/activity/', ActivityCreateView.as_view(), name='activity-create'),
    path('report/', report, name='report'),
]
