from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 맞지 않습니다."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("이메일이 존재하지 않습니다."))


class SignUpForm(forms.Form):

    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "email",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }
        password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

        def clean_email(self):
            password = self.cleaned_data.get("password")
            password1 = self.cleaned_data.get("password1")
            if password != password1:
                raise forms.ValidationError("비밀번호가 일치하지 않습니다")
            else:
                return password

        def save(self, *args, **kwargs):
            user = super().save(commit=False)
            email = self.cleaned_data.get("email")
            password = self.cleaned_data.get("password")
            user.username = email
            user.set_password(password)
            user.save()