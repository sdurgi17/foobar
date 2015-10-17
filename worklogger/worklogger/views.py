from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
import urllib2
import datetime
from django.conf import settings
from commons.models import User

# from django.template.context import RequestContext

#@login_required(login_url='/')
def home(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    user = {}
    try:
        user["name"] = request.user
        user["email"] =  request.user.email
        user["session_key"] = request.COOKIES[settings.SESSION_COOKIE_NAME]
    except Exception as e:
        print "Cannot make account:", str(e)
        return render_to_response('home.html',
                             context_instance=context)
    user_old = User.objects.filter(email= user['email'])
    if user_old:
        print user_old[0].name
    else:
        save_to_db(user)

    #print request.user.get_full_name
#   social_user =  request.user.social_auth.filter(provider='facebook').first()
#   if social_user:
#       url = u''
    return render_to_response('home.html',
                             context_instance=context)


#def logout(request):
#    auth_logout(request)
#    return redirect('/')


def save_to_db(kwarg):
    # print kwarg['session_key'] , kwarg['name'] , kwarg['email']
    name = kwarg.get('name','')
    email = kwarg.get('email',"foobar@fuckers.com")
    created_at = datetime.datetime.now().strftime('%Y-%m-%d')
    password = kwarg.get('password','')
    organisation = kwarg.get('organisation','')
    position = kwarg.get('position','')
    location = kwarg.get('location','')
    age = kwarg.get('age','')
    session_id = kwarg.get('session_id','')

    User_object = User(name=name, email=email, password=password, organisation=organisation,
                         position=position, created_at=created_at, session_id=int(session_id))
    # a = User (name = name , email = email , session_id = 10)
    # a.save()
    User_object.save()






