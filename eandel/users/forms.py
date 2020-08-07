from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms as f
from django.contrib import messages
from .models import Contact

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class ContactForm(f.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'msg')
        widgets = {
            'name': f.TextInput(
                    attrs={
                        'class': 'form-control input-box',
                        'id': 'name',
                        'placeholder': 'Your Name'
                    }
                ),
            'email': f.TextInput(
                attrs={
                    'class': 'form-control input-box',
                    'id': 'email',
                    'placeholder': 'Your Email'
                }
            ),
            'subject': f.TextInput(
                attrs={
                    'class': 'form-control input-box',
                    'id': 'subject',
                    'placeholder': 'Subject'
                }
            ),
            'msg': f.Textarea(
                attrs={
                    'class': 'form-control textarea-box',
                    'id': 'message',
                    'placeholder': 'Message',
                    'rows': '8'
                }
            )
        }
