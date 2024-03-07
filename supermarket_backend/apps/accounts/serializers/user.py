from allauth.account.adapter import get_adapter
from allauth.socialaccount.models import EmailAddress
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from dj_rest_auth.serializers import UserDetailsSerializer
from supermarket_backend.apps.accounts.models.user import (
    User,
    AccountType,
)


class AccountLoginSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type ": "password"})

    # Handle the non active account
    def validate_email(self, value):
        try:
            requested_user = User.objects.get(email=value)
            if not requested_user.is_active:
                raise ValidationError("The account is suspended")
            return value
        except User.DoesNotExist:
            raise ValidationError("No user exists with the given email")


class AccountRegisterSerializer(RegisterSerializer):
    account_type = serializers.ChoiceField(
        choices=AccountType.choices, default=AccountType.GENERAL
    )
    name = serializers.CharField(max_length=255)
    username = None

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and EmailAddress.objects.is_verified(email):
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address.",
            )
        return email

    def custom_signup(self, request, user):
        cleaned_data = self.get_cleaned_data()
        user.name = cleaned_data.get("name")
        user.account_type = cleaned_data.get("account_type")
        user.save()

    def get_cleaned_data(self):
        return {
            "name": self.validated_data.get("name", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "account_type": self._validated_data.get("account_type", "general"),
        }


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("profile_stage",)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "profile_pic")
