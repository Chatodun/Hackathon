from rest_framework import generics

from pharmacy.models import Organization, Branch, Medicament, MedicamentInPharmacy
from pharmacy.serializers import OrganizationSerializer, BranchSerializer, MedicamentSerializer, \
    MedicamentInPharmacySerializer


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BranchView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class MedicamentView(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer


class MedicamentInPharmacyView(generics.ListCreateAPIView):
    queryset = MedicamentInPharmacy
    serializer_class = MedicamentInPharmacySerializer
