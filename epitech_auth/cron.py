from django.conf import settings
from epitech_auth.models import LabUser
import cronjobs, os, urllib
import bcrypt

@cronjobs.register
def update_ppp():
    ppp_url = getattr(settings, 'PPP_URL', 'http://perso.epita.fr/ppp.blowfish')
    ppp_file = getattr(settings, 'PPP_FILE', 'ppp_blowfish')

    try: os.remove(ppp_file)
    # Does not exist
    except OSError:
        pass

    urllib.urlretrieve(ppp_url, ppp_file)

@cronjobs.register
def generate_htpasswd():
    for labuser in LabUser.objects.filter(user__is_staff=False):
        print '%s:%s' % (
            labuser.user.username,
            bcrypt.hashpw(labuser.password, bcrypt.gensalt())
        )
