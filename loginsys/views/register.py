# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth

from kamera.models import Kamera
from loginsys.models import User_data, User_kamera, Username_list
from django.contrib.auth.models import User     # autorisation library

from loginsys import mail

#from statistic.models import Ip_list, Ip_hit # import statistic objects
import datetime, pytz
import textwrap
import os


# E-MAIL SENDER
def sendMail(TO,SUBJECT,TEXT):
    import smtplib
    message = textwrap.dedent("""\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % ('info@kuvalda.lv', TO, SUBJECT, TEXT))
    # Send the mail
    server = smtplib.SMTP('localhost')
    server.sendmail('info@kuvalda.lv', TO, message.encode('utf-8'))
    server.quit()


# !!!!! REGISTER
def register(request):
    username = auth.get_user(request)
    args = {}
#    args.update(csrf(request))  # encript data
    args['ip'] = ip_statistic(request)
    args['heading'] = u'Jauna lietotāja izveidošana'	# unicode string

    if request.POST:    # actions if login Form is submitted
        user = request.POST.get('user', '')     # usermname <= get variable from Form (name="user"), if not leave blank
        email = request.POST.get('email', '')     # user_email <= get variable from Form (name="emial"), if not leave blank
        passw1 = request.POST.get('passw1', '')
        passw2 = request.POST.get('passw2', '')
        kamera = request.POST.get('kamera', '')     # kamera <= get variable from Form (name="kamera"), if not leave blank
        kamera_type = request.POST.get('kamera_type', '')

        # define args in case of error
        args['user'] = user
        args['email'] = email
        args['kamera'] = kamera
        error = False # define error state

        # search username in Auth.User
        for u in User.objects.all():
            if u.username == user:
                args['user_error'] = u'Lietotāja vārds jau tiek izmantots'
                error = True
        # search username in loginsys.models.Username_list
        for u in Username_list.objects.all():
            if u.username == user:
                args['user_error'] = u'Lietotāja vārds jau tiek izmantots'
                error = True
        # search e-mail in Auth.User
        for u in User.objects.all():
            if u.email == email:
                args['email_error'] = u'Lietotāja e-pasta adrese jau tiek izmantota'
                error = True
        # search e-mail in loginsys.models.Username_list
        for u in Username_list.objects.all():
            if u.user_email == email:
                args['email_error'] = u'Lietotāja e-pasta adrese jau tiek izmantota'
                error = True
        if passw1 != passw2 or passw1 == '':
                args['passw_error'] = u'Parole nav ievadīta vai arī ievadītās paroles nesakrīt'
                error = True
        # If any error return form
        if error == True:
            args['error'] = True
            return render(request, 'register.html', args)

        # INCOGNITO REGISTRATION
        username_wanted = Username_list(username=user, user_email=email, datums=datetime.datetime.now(), kamera=kamera, kamera_type=kamera_type, passw=passw1 )
      # CREATE NEW loginsys.models.Username_list
        username_wanted.save()

        # MAIL TO SUPERUSER
        sendMail('sga@dexed.eu', 'INFO', u'jauns lietotāja pieteikums')
        sendMail('fizmats@inbox.lv', 'INFO', u'jauns lietotāja pieteikums')

        # MAIL TO USER
#        try:
#            sendMail(email, 'INFO', u'Labdien! jūsu pieteikums reģistrācijai  http://www.kuvalda.lv/ ir saņemts, gaidiet apstiprinājumu')
#        except:
#            pass

        response = render(request, 'reg_response.html', args)
        return response

    else:       # actions if activated hyperlink to login Form
        return render(request, 'register.html', args)


# !!!!! NEW USER LIST
def new_users(request):
    username = auth.get_user(request)
    args = {}
    args['username'] = username
    if username.is_superuser:
        args['heading'] = u'Jaunu lietotāju apstiprināšana'        # unicode string
        args['newuser'] = Username_list.objects.all()
        response = render(request, 'new_user_list.html', args)
        return response
    return redirect('/')


# !!!!! USER ADD
def user_add(request, id):
    username = auth.get_user(request)
    if username.is_superuser:
        try:
            new_user = Username_list.objects.get(id = id)	# get user register data
            create_user = User.objects.create_user( new_user.username, new_user.user_email, new_user.passw)       # CREATE NEW Auth.User
            data = User_data( user_user=create_user, user_last_visit=datetime.datetime.now()) # CREATE NEW loginsys.models.User_data
            data.save()

            new_kamera_data = mail.generate_mail()	# generate kamer_email, kamera_img_dir
            new_mail = new_kamera_data[0]
            img_dir = new_kamera_data[1]
            new_kamera = Kamera(kamera_nos=new_user.kamera, kamera_type=new_user.kamera_type, kamera_email=new_mail, kamera_img_dir=img_dir)	# CREATE NEW kamera.models.Kamera
            new_kamera.save()

            os.mkdir('/home/' + img_dir)

            usr_kamera = User_kamera(user = create_user, kamera = new_kamera)	# CREATE NEW loginsys.models.User_kamera
            usr_kamera.save()
        # !!!!!! E_MAIL TO USER --> ACCEPTED
#            try:
#                sendMail( new_user.user_email, u'Apstiprinājums', u'Labdien! jūsu reģistrācija http://www.kuvalda.lv/ ir apstiprināta !!! epasts fotogrāfiju sūtīšanai no kameras uz serveri - lvxxxx@kuvalda.lv')
#            except:
#                pass
            new_user.delete()	# DELETE USER FROM loginsys.models.Username_list
        except:
            pass
        return redirect ('/auth/new_users/')

    return redirect ('/')


# !!!!! USER DELETE
def user_del(request, id):
    username = auth.get_user(request)
    if username.is_superuser:
        new_user = Username_list.objects.get(id = id)
    # !!!!!! E_MAIL TO USER --> DENIED
#        try:
#            sendMail( str(new_user.user_email), u'Noraidījums', u'Labdien! jūsu reģistrācija http://www.kuvalda.lv/ ir noraidīta, mēiģiniet veikt reģistrāciju atkārtoti')
#        except:
#            pass
        new_user.delete()

        return redirect ('/auth/new_users/')
    return redirect ('/')
