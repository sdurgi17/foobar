from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
import json
import utils
import os
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from commons.models import Project, Post
from django.conf import settings
from commons.models import User

@csrf_exempt
def user_projects(request):

    # print "in signup"
    # try:
    #     print "dkfg"
    #     print request.method
    #     if request.method == 'POST':
    #         print "fgbknlkfg"
            
    #         first_name = request.POST['first_name']
    #         last_name = request.POST['last_name']
    #         email=  request.POST['email']
    #         password = request.POST['password']
    #         confirm_password = request.POST['renter_password']
    #         # session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]

    #         print "confirming password"
    #         if password == confirm_password:
    #             user_old = User.objects.filter(email= email)
    #             if user_old:
    #                 print "old user"
    #                 return HttpResponse("USER EXISTS")
    #             else:
    #                 User_object = User(name=first_name, email=email, password=password) #, session_id = session_key)
    #                 User_object.save()
    #                 print "something "
    #                 user_id = (User.objects.filter(email= email)[0]).id
    #                 print user_id

    user_id = request.GET['user_id']
    user_feed = utils.get_user_feed(user_id)
    project_contribution = utils.get_user_project_contribution(user_id)
    user_tags = utils.get_user_tags(user_id)

    data = {
        "user_feed": user_feed,
        "project_contribution": project_contribution,
        "user_tags": user_tags
    }
    json_dump = json.dumps(data)
    return render(request,'feed/project_view.html', {'json_dump' : json_dump})
    # except Exception as e:
    #     return HttpResponse(str(e))
    # return HttpResponse("Bad Request")

def project_tasks(request):
    user_id = request.GET['user_id']
    project_id = request.GET['project_id']
    project_feed = utils.get_project_feed(user_id, project_id)
    user_tags = utils.get_user_tags(user_id, project_id)
    hard_tasks = utils.get_hard_tasks(user_id, project_id)
    data = {
        "project_feed": project_feed,
        "user_tags": user_tags,
        "hard_tasks": hard_tasks
    }
    json_dump = json.dumps(data)
    return render(request,'feed/post_view.html', {'json_dump' : json_dump})
