epitech_auth
============
by brmzkw for the Epitech Security Laboratory
---------------------------------------------

This django application contains:

* An authentication backend. It checks if the provided credentials match for the default backend and if not, the blowfish file (named *ppp.blowfish* by default, overridable with **settings.PPP_FILE**) is used to create a user in database, updating the password if necessary. Add **AUTHENTICATION_BACKENDS = ('epitech_auth.backends.PPPAuth',)** in your *settings.py* to use it
* Two cronjobs you (you probably want to call them from a crontab)
    - *python manage.py cron update\_ppp* to get the new version of the *ppp.blowfish* file (get from *http://perso.epita.fr/ppp.blowfish* by default, overridable with **settings.PPP_URL**)
    - *python manage.py cron generate\_htpasswd* generates a htpasswd file, named *logins.htpasswd* (overridable with **settings.HTPASSWD_OUTFILE**)
* A *create_password* view (epitech_auth.views.create_password). We use this view to generate passwords: instead of using their ppp password which might be compromised, users will use this password on our websites
