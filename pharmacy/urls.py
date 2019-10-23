from django.urls import path

from pharmacy import views

urlpatterns = [
    path('organizations/', views.OrganizationView.as_view()),
    path('branches/', views.BranchView.as_view()),
    path('medicaments/', views.MedicamentView.as_view()),

]
