import pytest

from eandel.users.forms import UserCreationForm, ContactForm
from eandel.users.tests.factories import UserFactory, ContactFactory

pytestmark = pytest.mark.django_db


class TestUserCreationForm:
    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user._password,
                "password2": proto_user._password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors


class TestContactForm:

    def test_empty_form_inputs(self):

        form = ContactForm(
            {
                "name": "",
                "email": "",
                "subject": "",
                "msg":""
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 4

    def test_valid_form_inputs(self):
        proto_contact = ContactFactory.build()

        form = ContactForm(
            {
                "name": proto_contact.name,
                "email": proto_contact.email,
                "subject": proto_contact.subject,
                "msg": proto_contact.msg
            }
        )

        assert form.is_valid()
