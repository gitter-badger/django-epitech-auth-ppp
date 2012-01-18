from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from epitech_auth.models import LabUser
import random
import bcrypt

PASSWORD_CHARS = 'abcdefghijklmnopqrstuvwxyz_-!@#$%^&*()_='
PASSWORD_LENGTH = 8

@login_required
def create_password(request):
    try:
        labuser = LabUser.objects.get(user=request.user)
    except LabUser.DoesNotExist:
        labuser = None

    if request.method == 'POST':
        (labuser, created) = LabUser.objects.get_or_create(user=request.user)
        labuser.password = ''.join(random.choice(PASSWORD_CHARS) for x in range(PASSWORD_LENGTH))
        labuser.encrypted_password = bcrypt.hashpw(labuser.password, bcrypt.gensalt())
        labuser.save()

    return direct_to_template(request,
        'registration/create_password.html',
        extra_context={'current_password': labuser.password if labuser else None}
    )
