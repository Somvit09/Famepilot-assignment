from rest_framework import serializers
from .models import Account


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password', ]

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        email = data.get('email')


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2', 'date_of_birth', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            date_of_birth=self.validated_data['date_of_birth'],
            phone_number=self.validated_data['phone_number']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
