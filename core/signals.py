from allauth.account.signals import email_confirmed
from django.dispatch import receiver

@receiver(email_confirmed)
def auto_login_after_email_confirm(request, email_address, **kwargs):
    # Force la connexion après confirmation d'email
    user = email_address.user
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    from django.contrib.auth import login
    login(request, user)