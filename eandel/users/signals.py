from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Contact


@receiver(post_save, sender=Contact)
def send_mail(sender, instance, **kwargs):
    subject = instance.subject
    body = 'NAME: {}\nEMAIL: {}\nMESSAGE:\n{}'.format(instance.name, instance.email, instance.msg)
    to = ['chukwuma.akunyili@eandeafrica.com', 'uche.mbah@eandeafrica.com', 'hello@eandeafrica.com']
    from_email = 'admin@eandeafrica.com'
    # sm(subject, body, from_email, to)
