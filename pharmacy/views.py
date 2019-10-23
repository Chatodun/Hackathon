from rest_framework import generics, status
from rest_framework.response import Response

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
    queryset = MedicamentInPharmacy.objects.all()
    serializer_class = MedicamentInPharmacySerializer

    def get(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.filter(branch_id=pk), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
