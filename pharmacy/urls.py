from django.conf.urls import url
from django.urls import path

from pharmacy import views
from pharmacy.views import CommandReceiveView

urlpatterns = [
    path('organizations/', views.OrganizationView.as_view()),
    path('branches/', views.BranchView.as_view()),
    path('branches/<int:pk>/medicaments/', views.MedicamentInBranchView.as_view()),
    path('medicaments/', views.MedicamentView.as_view()),
    url(r'^bot/(?P<bot_token>.+)/$', CommandReceiveView.as_view(), name='command'),
]
