#from django.contrib.sites.models import Site
from loginsys.models import User_data
from django.utils.timezone import now
import datetime, pytz

from datetime import timedelta
from django.conf import settings
from django.contrib import auth

class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
#            # CHECK IF user_last_visit is older than ??? (10 min)
            user = User_data.objects.filter(pk = request.user.pk)                # User_data object list

            for usr in user:
                user_visit = getattr(usr, 'user_last_visit')
                time_now = datetime.datetime.now().replace(tzinfo=pytz.timezone('EET'))

                timeDiff = ( time_now - user_visit ).total_seconds()
                if timeDiff > 60:      # 1 MINUTE
                # Update last visit time after request finished processing.
#                   User_data.objects.filter(user_user=request.user.pk).update( user_last_visit = now() )
                    usr.user_last_visit = now()
                    usr.save()

        return response

class AutoLogout:
    def process_request(self, request):
        if not request.user.is_authenticated() :
            #Can't log out if not logged in
            return
        try:
            if now() - request.session['last_touch'] > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError:
            pass
        request.session['last_touch'] = now()
