from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Reservation, CustomUser


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = "__all__"


class CustomerUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "phone_number",
        )


class CustomerUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
