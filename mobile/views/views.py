from django.http import JsonResponse

from loginsys.models import *
from kamera.models import *
from datetime import datetime

def cam_img(request):
    user = request.META.get('USERNAME')
    ip = request.META.get('REMOTE_ADDR')
    args = {}
    args['rez'] = 'ok'
    args['user'] = user
    args['ip'] = ip

    return JsonResponse(args)


def Response_1(request):
    user = request.META.get('USERNAME')
    ip = request.META.get('REMOTE_ADDR')

    args = {}
#    args['foo'] = 'bar'
#    args['user'] = user
#    args['ip'] = ip

    cam = []
    kameras = Kamera.objects.all()
    count = 0
    next = False

    for k in kameras:
        if count == 5:
            next = True
            break
        cam.append( getattr( k, 'kamera_slug' ) )
        count += 1
#    args['result'] = cam

#    args['count'] = len(cam)
    if next:
        pass
#        args['next'] = 'http://kuvalda.lv:8005/mobile_api/?page=2'
    else:
        pass
#        args['next'] = ''

#    args['previous'] = ''

    date = datetime.now()
    min = date.minute
    if min % 2 != 0:
        args['kaka'] = 'True'
    else:
        args['kaka'] = 'False'

    return JsonResponse(args)

