from django.shortcuts import render, redirect	# response to template, redirect to another view

from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library


# ========================================================================================
# CONTAINERS
def container_search(request):
    username = auth.get_user(request)
    if username.is_superuser == True or username.groups.filter(name='container').exists():
        args = {}
        args['id'] = username.id
        return render(request, 'container_search.html', args)

    return redirect('/auth/login/')

# Container PDF reader from mail
def container_pdf(request):
    username = auth.get_user(request)
    if username.is_superuser == True or username.groups.filter(name='container').exists():
        args = {}
        args['id'] = username.id
        return render(request, 'container_pdf.html', args)

    return redirect('/auth/login/')

# Container PIN submit
def container_pin(request):
    username = auth.get_user(request)
    if username.is_superuser == True or username.groups.filter(name='container').exists():
        args = {}
        args['id'] = username.id
        return render(request, 'container_pin.html', args)

    return redirect('/auth/login/')

