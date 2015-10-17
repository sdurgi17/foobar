# from django.shortcuts import render
# from django.http import HttpResponse
# from commons.models import *
# import json
# from django.db.models import F
# from django.views.decorators.csrf import csrf_exempt

# import os
# import sys
# # import ast
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# @csrf_exempt
# def store_uid(request):
#   try:
#       if request.method == 'POST':
#           user_id = request.POST.get('user_id', 1)
#           user = User.objects.filter(id = user_id)[0]
#           project_name = request.POST.get('project_name', 'random')
#           project_details = request.POST.get('project_details', '')
#           print user_id, project_name, project_details
#           new_project = Project(name= project_name, user=user, details=project_details)
#           new_project.save()
#       return render(request, 'new_post.html' , dict(user = user_id, project = new_project.id))
#   except Exception as e:
#       return HttpResponse(json.dumps(e))


# @csrf_exempt
# def create_project(request):
#   try:
#       if request.method == 'GET':
#           user_id = request.GET.get('user_id', 1)
#       return render(request, 'create_project_new.html')

#   except Exception as e:
#       return HttpResponse(json.dumps(e))



# @csrf_exempt
# def create_post(request):
#   try:
#       print request.POST
#       if request.method == 'POST':
#           user_id = request.POST.get('user_id', 1)
#           print "user_id = ", user_id
#           user = User.objects.filter(id = user_id)[0]
#           project_id = request.POST.get('project_id', -1)
#           # return HttpResponse(json.dumps(user_id+project_id))
#           if project_id == -1:
#               project_id = Project.objects.filter(name = 'random', user = user)[0]
#           else:
#               project_id = Project.objects.filter(id = project_id)[0]
#           title = request.POST.get('title', '')
#           details = request.POST.get('details', '')
#           access_type = request.POST.get('access_type', 1)
            
#           new_post = Post(user=user, project=project_id, title=title, details=details, access_type=access_type)
#           new_post.save()
            
#           tags = request.POST.get('tags', [])
#           tags = json.loads(tags)
#           for tag in tags:
#               tag_exist = Tag.objects.filter(name=tag)
#               flag = len(tag_exist)
#               if flag != 0:
#                   print "updating tag"
#                   new_tag = Tag.objects.filter(name=tag).update(count=F('count')+1)
#                   post_id = Post.objects.filter(id=new_post.id)[0]
#                   tag_id = Tag.objects.filter(id=tag_exist[0].id)[0]
#                   post_tag = Post_To_Tag(post=post_id, tag=tag_id)
#                   post_tag.save()
#               else:
#                   print "creating new tag"
#                   new_tag = Tag(name=tag, count=1)
#                   new_tag.save()

#                   post_id = Post.objects.filter(id=new_post.id)[0]
#                   tag_id = Tag.objects.filter(id=new_tag.id)[0]
#                   post_tag = Post_To_Tag(post=post_id, tag=tag_id)
#                   post_tag.save()
#       return render(request, 'feed/user_projects.html', dict(user_id=user_id))
#   except Exception as e:
#       return HttpResponse(e)



from django.shortcuts import render
from django.http import HttpResponse
from commons.models import *
import json
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
import feed
import os
import sys
import ast
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
 
 
@csrf_exempt
def store_uid(request):
        try:
                if request.method == 'POST':
                        user_id = request.POST.get('user_id', 1)
                        user = User.objects.filter(id = user_id)[0]
                        project_name = request.POST.get('project_name', 'random')
                        project_details = request.POST.get('project_details', '')
                        print user_id, project_name, project_details
                        new_project, created = Project.objects.get_or_create(name= project_name, user=user, defaults={'details': project_details})
                        # json_dump = json.dumps({'user_id':user_id})
                return render(request, 'create_post_new.html' , dict(user = user_id))
        except Exception as e:
                return HttpResponse(json.dumps(e))
 
 
@csrf_exempt
def create_project(request):
        try:
                if request.method == 'GET':
                        user_id = request.GET.get('user_id', 1)
                return render(request, 'create_project_new.html')
 
        except Exception as e:
                return HttpResponse(json.dumps(e))
 
@csrf_exempt
def redirect_post(request):
    try:
        if request.method == 'GET':
                user_id = request.GET.get('user_id', 1)
                user_feed = feed.utils.get_user_feed(user_id)
                print "shbfgkj => "
                print user_feed
                project_contribution = feed.utils.get_user_project_contribution(user_id)
                user_tags = feed.utils.get_user_tags(user_id)

                print "user feed = > ", user_feed

                data = {
                    "user_id": user_id,
                    "user_feed": user_feed,
                    "project_contribution": project_contribution,
                    "user_tags": user_tags
                }
                json_dump = json.dumps(data)
        # return render(request, 'feed/project_view.html', dict(user_id=user_id))
        return render(request, 'create_post_new.html', dict(user = user_id))
    except Exception as e:
            return HttpResponse(json.dumps(e))

 
 
@csrf_exempt
def create_post(request):
        try:
                print request.POST
                user_id = int(request.POST.get('user_id', 1))
                print "user_id = ", user_id
                user = User.objects.filter(id = user_id)[0]
                print "object id", user.id
                print request.POST.get('title')
                project_name = request.POST.get('project_name', 'dev')
                print "abc", project_name
 
                project_id = Project.objects.filter(name = project_name, user = user)
               
                print "project_id is", project_id , len(project_id)
                if len(project_id) == 0:
                        project_id = Project.objects.filter(name = 'dev', user = user)[0]
                else:
                        project_id = project_id[0]                     
               
                print project_id
                title = request.POST.get('title', '')
                details = request.POST.get('details', '')
                access_type = request.POST.get('access_type', 1)
               
                new_post = Post(user=user, project=project_id, title=title, details=details, access_type=access_type)
                new_post.save()
               
                print "Saved"
                tag = request.POST.get('tags', 'project')
                tags = tag.split(", ")
                for tag in tags:
                        tag_exist = Tag.objects.filter(name=tag)
                        flag = len(tag_exist)
                        if flag != 0:
                                print "updating tag"
                                new_tag = Tag.objects.filter(name=tag).update(count=F('count')+1)
                                post_id = Post.objects.filter(id=new_post.id)[0]
                                tag_id = Tag.objects.filter(id=tag_exist[0].id)[0]
                                post_tag = Post_To_Tag(post=post_id, tag=tag_id)
                                post_tag.save()
                        else:
                                print "creating new tag"
                                new_tag = Tag(name=tag, count=1)
                                new_tag.save()
 
                                post_id = Post.objects.filter(id=new_post.id)[0]
                                tag_id = Tag.objects.filter(id=new_tag.id)[0]
                                post_tag = Post_To_Tag(post=post_id, tag=tag_id)
                                post_tag.save()

                        user_feed = feed.utils.get_user_feed(user_id)
                        print "shbfgkj => "
                        print user_feed
                        project_contribution = feed.utils.get_user_project_contribution(user_id)
                        user_tags = feed.utils.get_user_tags(user_id)

                        print "user feed = > ", user_feed

                        data = {
                            "user_id": user_id,
                            "user_feed": user_feed,
                            "project_contribution": project_contribution,
                            "user_tags": user_tags
                        }
                        json_dump = json.dumps(data)
                return render(request, 'feed/project_view.html', {'json_dump': json_dump})
        except Exception as e:
                return HttpResponse(e)