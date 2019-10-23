from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

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

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('search', None)
        if query:
            medicaments = self.queryset.filter(name__contains=query)
        else:
            medicaments = self.queryset.all()
        serializer = self.serializer_class(medicaments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MedicamentInPharmacyView(generics.ListCreateAPIView):
    queryset = MedicamentInPharmacy.objects.all()
    serializer_class = MedicamentInPharmacySerializer

    def get(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.filter(branch_id=pk), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
