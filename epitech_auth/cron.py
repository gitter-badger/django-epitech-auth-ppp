from django.conf import settings
import cronjobs, os, urllib

@cronjobs.register
def update_ppp():
    ppp_url = getattr(settings, 'PPP_URL', 'http://perso.epita.fr/ppp.blowfish')
    ppp_file = getattr(settings, 'PPP_FILE', 'ppp_blowfish')

    try: os.remove(ppp_file)
    # Does not exist
    except OSError:
        pass

    urllib.urlretrieve(ppp_url, ppp_file)
