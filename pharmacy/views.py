from rest_framework import generics, status
from rest_framework.response import Response

from pharmacy.models import Organization, Branch, Medicament, MedicamentInBranch
from pharmacy.serializers import OrganizationSerializer, BranchSerializer, MedicamentSerializer, \
    MedicamentInBranchSerializer, BranchWithMedicamentInfoSerializer


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BranchView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self, request, *args, **kwargs):
        medicament_id = request.query_params.get('medicament_id', None)
        if medicament_id:
            branches = self.queryset.filter(medicamentinbranch__medicament_id=medicament_id)
        else:
            branches = self.queryset.all()
        serializer = self.serializer_class(branches, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MedicamentView(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            medicaments = self.queryset.filter(name__contains=query)[0]
            serializer = self.serializer_class(medicaments)
        else:
            medicaments = self.queryset.all()
            serializer = self.serializer_class(medicaments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MedicamentInBranchView(generics.ListCreateAPIView):
    queryset = MedicamentInBranch.objects.all()
    serializer_class = BranchWithMedicamentInfoSerializer

    def get(self, request, *args, **kwargs):
        medicament_id = request.query_params.get('medicament_id', None)
        if medicament_id:
            queryset = self.queryset.filter(medicament_id=medicament_id)
        else:
            queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
