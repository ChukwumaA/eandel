from .models import Contact
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail as sm


@receiver(post_save, sender=Contact)
def send_mail(sender, instance, **kwargs):
    subject = instance.subject
    body = 'NAME: {}\nEMAIL: {}\nMESSAGE:\n{}'.format(instance.name, instance.email, instance.msg)
    to = ['ijeoma.mbah@eandeafrica.com', 'uche.mbah@eandeafrica.com']
    from_email = 'admin@eandeafrica.com'
    # sm(subject, body, from_email, to)
