from django.conf import settings
from django.contrib.auth.models import User
import bcrypt

class PPPAuth(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        # Try to authenticate with default backend
        try:
            # Return the local user, if login/pass match
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user

            # Only the password is invalid. It is maybe outdated in database
            ppp_pw = self.get_blowfish_passwd(username)
            if ppp_pw and bcrypt.hashpw(password, ppp_pw) == ppp_pw:
                user.set_password(password)
                user.save()
                return user

        # There is no local user
        except User.DoesNotExist:
            ppp_pw = self.get_blowfish_passwd(username)
            # Credentials are ok, create a user in database
            if ppp_pw and bcrypt.hashpw(password, ppp_pw) == ppp_pw:
                user = User(username=username)
                user.set_password(password)
                user.save()
                return user

        # Invalid credentials
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_blowfish_passwd(self, login):
        with open(getattr(settings, 'PPP_FILE', 'ppp.blowfish')) as f:
            for credentials in f:
                try:
                    ppp_l, ppp_pw = credentials.split()
                    if ppp_l == login:
                        return ppp_pw
                except: pass
        return None
