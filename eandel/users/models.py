from django.contrib.auth.models import AbstractUser
from django.db  import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=500)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['-created_at']
    
