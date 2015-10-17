from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
import json
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
import urllib2
import datetime
from django.conf import settings
from commons.models import User

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        context = RequestContext(request,
                               {'request': request,
                                'user': request.user})
        try:
            email = request.POST['email']
            password = request.POST['password']
            user_exist = User.objects.filter(email= email)[0]
            p_ = user_exist.password
            if password == user_exist.password:
                user_id = (User.objects.filter(email= email)[0]).id
                return  render(request,'feed/project_view.html', {'user_id':user_id})
            else:
                return HttpResponse("PASSWORD DO NOT MATCH")
        except Exception as e:
            return render_to_response('feed/home.html',context_instance=context)

@csrf_exempt
def open_form(request):
    return render_to_response('feed/sign_up.html')
    
@csrf_exempt
def logout (request):
    return HttpResponse("LOGOUTTED")

@csrf_exempt
def signup(request):
    print request.method
    if request.method == 'POST':
        print request.POST
        # context = RequestContext(request,
        #                        {'request': request,
        #                         'user': request.user})
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email=  request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['renter_password']
            # session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]

            print "something shgbnmm"

            if password == confirm_password:
                print "kdfgfdkdbnkjdnbd"
                user_old = User.objects.filter(email= email)
                print user_old
                if user_old:
                    print "old user"
                    return HttpResponse("USER EXISTS")
                else:
                    print "ksjfgjkdf bd bkhd "
                    User_object = User(name=first_name, email=email, password=password)# , session_id = session_key)
                    User_object.save()
                    print "something "
                    user_id = (User.objects.filter(email= email)[0]).id
                    print user_id
                    return render(request,'feed/project_view.html', {'user_id':user_id})
            else:
                return HttpResponse("PASSWORD DO NOT MATCH")
        except Exception as e:
            return render(request,'feed/home.html', {})
    return HttpResponse('SIGNUP SUCCESSFUL')


@csrf_exempt
def signup_facebook(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    
    try:
        name = request.user
        email =  request.user.email
        session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]

    except Exception as e:
        print "Cannot make account:", str(e)
        return render_to_response('feed/home.html',context_instance=context)
    user_old = User.objects.filter(email= email)
    
    if user_old:
        return HttpResponse("USER EXISTS")
    else:
        User_object = User(name=name, email=email,session_id=session_key)
        User_object.save()
    
    return render_to_response('feed/home.html',
                             context_instance=context)





