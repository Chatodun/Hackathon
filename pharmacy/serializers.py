from rest_framework import serializers

from pharmacy.models import Organization, Medicament, Branch, MedicamentInPharmacy


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
            organization_id=validated_data.pop('organization')['id'],
            **validated_data
        )
        return branch


class MedicamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicament
        fields = '__all__'


class MedicamentInPharmacySerializer(serializers.ModelSerializer):
    pharmacy_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source='pharmacy.id'
    )
    medicament_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicament.objects.all(),
        source='medicament.id'
    )

    class Meta:
        model = MedicamentInPharmacy
        fields = ('id', 'pharmacy_id', 'medicament_id', 'price', 'count')

    def create(self, validated_data):
        pharmacy_id = validated_data.pop('pharmacy')['id']
        medicament_id = validated_data.pop('medicament')['id']

        medicament_in_pharmacy = MedicamentInPharmacy.objects.create(
            pharmacy_id=pharmacy_id,
            medicamet_id=medicament_id,
            **validated_data
        )

        return medicament_in_pharmacy
