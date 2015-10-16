from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
import json
import utils

from commons.models import Project, Post


def user_projects(request):
    user_id = request.GET['user_id']
    user_feed = utils.get_user_feed(user_id)
    project_contribution = utils.get_user_project_contribution(user_id)
    user_tags = utils.get_user_tags(user_id)

    data = {
        "user_feed": user_feed,
        "project_contribution": project_contribution,
        "user_tags": user_tags
    }
    return HttpResponse('hi')


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
    return HttpResponse('hello')
