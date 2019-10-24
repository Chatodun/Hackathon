from rest_framework import serializers

from pharmacy.models import Organization, Medicament, Branch, MedicamentInBranch, Category


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(),
        source='organization.id'
    )

    class Meta:
        model = Branch
        fields = ('id', 'organization_id', 'address', 'phone', 'open_time', 'close_time')

    def create(self, validated_data):
        branch = Branch.objects.create(
            organization=validated_data.pop('organization')['id'],
            **validated_data
        )
        return branch


class BranchWithMedicamentInfoSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source='branch.id'
    )
    organization_name = serializers.CharField(
        source='branch.organization.name'
    )
    address = serializers.CharField(
        source='branch.address'
    )
    phone = serializers.CharField(
        source='branch.phone'
    )
    open_time = serializers.CharField(
        source='branch.open_time'
    )
    close_time = serializers.CharField(
        source='branch.close_time'
    )
    medicament_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicament.objects.all(),
        source='medicament.id'
    )

    class Meta:
        model = MedicamentInBranch
        fields = ('id', 'branch_id', 'medicament_id', 'price', 'count',
                  'organization_name', 'address', 'phone', 'open_time', 'close_time')


class MedicamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicament
        fields = '__all__'


class MedicamentInBranchSerializer(serializers.ModelSerializer):
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source='branch.id'
    )
    medicament_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicament.objects.all(),
        source='medicament.id'
    )

    class Meta:
        model = MedicamentInBranch
        fields = ('id', 'branch_id', 'medicament_id', 'price', 'count')

    def create(self, validated_data):
        branch = validated_data.pop('branch')['id']
        medicament = validated_data.pop('medicament')['id']

        medicament_in_pharmacy = MedicamentInBranch.objects.create(
            branch=branch,
            medicament=medicament,
            **validated_data
        )

        return medicament_in_pharmacy


class CategorySerializer(serializers.ModelSerializer):
    products = MedicamentSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'products', )
