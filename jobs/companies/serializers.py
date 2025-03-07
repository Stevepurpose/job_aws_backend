from rest_framework import serializers
from django.contrib.auth.models import User
from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
     owner = serializers.ReadOnlyField(source='owner.username')
     class Meta:
          model = Company
          fields = ['id', 'company_name', 'role', 'applied', 'Discussions', 'offer', 'advert_start', 'close_date', 'owner']




class UserSerializer(serializers.ModelSerializer):
    #companies = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password':{"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user