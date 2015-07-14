from django import forms
from django.contrib.auth import get_user_model


class RegistrationForm(forms.ModelForm):
    repeat_password = forms.CharField(widget=forms.PasswordInput,
                                      required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'profile_image',
            'first_name',
            'last_name',
            'email',
            'address',
            'mobile_phone',
            'password',
        )

    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeated_password = self.cleaned_data.get("repeat_password")
        if not (password == repeated_password):
            raise forms.ValidationError("passwords do not match")
        return repeated_password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        user.set_password(user.password)
        user.save()
        return user
