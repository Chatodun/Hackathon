from rest_framework import generics, status
from rest_framework.response import Response

from pharmacy.models import Organization, Branch, Medicament, MedicamentInBranch, Category
from pharmacy.serializers import OrganizationSerializer, BranchSerializer, MedicamentSerializer, \
    MedicamentInBranchSerializer, CategorySerializer


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
        query = request.query_params.get('query', None)
        if query:
            medicaments = self.queryset.filter(name__contains=query)
        else:
            medicaments = self.queryset.all()
        serializer = self.serializer_class(medicaments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MedicamentInBranchView(generics.ListCreateAPIView):
    queryset = MedicamentInBranch.objects.all()
    serializer_class = MedicamentInBranchSerializer

    def get(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.filter(branch_id=pk), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
