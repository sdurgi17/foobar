from django.shortcuts import render
from django.http import HttpResponse
from commons.models import *
import json
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt

import os
import sys
# import ast
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


@csrf_exempt
def store_uid(request):
	try:
		if request.method == 'POST':
			user_id = request.POST.get('user_id', 1)
			user = User.objects.filter(id = user_id)[0]
			project_name = request.POST.get('project_name', 'random')
			project_details = request.POST.get('project_details', '')
			new_project = Project(name= project_name, user=user, details=project_details)
			new_project.save()
		return render(request, 'create_post.html', {})
	except Exception as e:
		return HttpResponse(json.dumps(e))

@csrf_exempt
def create_project(request):
	try:
		if request.method == 'GET':
			user_id = request.GET['user_id']
		return render(request, 'create_project.html', {})		
	except Exception as e:
		return HttpResponse(json.dumps(e))


@csrf_exempt
def create_post(request):
	try:
		if request.method == 'POST':
			user_id = request.POST.get('user_id', 1)
			user = User.objects.filter(id = user_id)[0]
			project_id = request.POST.get('project_id', -1)
			if project_id == -1:
				project_id = Project.objects.filter(name = 'random', user = user)[0]
			else:
				project_id = Project.objects.filter(id = project_id)[0]
			title = request.POST.get('title', '')
			details = request.POST.get('details', '')
			access_type = request.POST.get('access_type', 1)
			
			new_post = Post(user=user, project=project_id, title=title, details=details, access_type=access_type)
			new_post.save()
			
			tags = request.POST.get('tags', [])
			tags = json.loads(tags)
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
			# return HttpResponse("adios")
		return render(request, 'create_post.html', {})
	except Exception as e:
		return HttpResponse(e)