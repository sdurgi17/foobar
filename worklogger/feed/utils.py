import os
import sys
import requests
import json
import datetime
from django.db import connections
from collections import defaultdict, Counter
from django.db.models import Count

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path = [os.path.join(SCRIPT_DIR + '/../')] + sys.path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "common.models")
from django.db import connections
from commons.models import Project, Post

db_name = 'default'


def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
            ]


def execute_query(query, cur):
    try:
        cur.execute(query)
    except:
        print 'failed'

    row = dictfetchall(cur)
    return row


def get_project_details_dict():
    projects = Project.objects.all()
    project_dict = defaultdict(dict)
    for row in projects:
        project_dict[row.__dict__['id']] = {
            'id': row.__dict__['id'],
            'name': row.__dict__['name'],
            'details': row.__dict__['details'],
            'is_completed': row.__dict__['is_completed']
        }
    return project_dict


def get_user_feed(user_id):
    project_rows_unprocessed = Post.objects.filter(
        user_id=user_id).order_by("updated_at").reverse()

    project_details = get_project_details_dict()

    project_rows = {}
    for row in project_rows_unprocessed:
        if not project_rows.get(row.project.id):
            project_rows[row.project.id] = project_details[row.project.id]
            project_rows[row.project.id]['updated_at'] = row.updated_at
    return project_rows


def get_user_project_contribution(user_id):
    task_counts = Post.objects.filter(user_id=user_id).values(
        'project').annotate(task_count=Count('project'))
    sum_task_counts = Post.objects.count()

    project_details = get_project_details_dict()

    project_contribution = {}
    for task_data in task_counts:
        project_contribution[task_data['project']] = {'count': task_data[
            'task_count'], 'project_name': project_details[task_data['project']]['name']}

    return project_contribution


def get_user_tags(user_id, project_id=0):
    if not project_id:
        query = """ SELECT count(t.name) as tag_count, t.name as tag_name
                    FROM commons_post p join commons_post_to_tag pt ON p.id = pt.post_id
                    JOIN commons_tag t ON pt.tag_id = t.id
                    WHERE p.user_id = {user_id}
                    GROUP BY t.id
                    ORDER BY tag_count;""".format(user_id=int(user_id))
    else:
        query = """ SELECT count(t.name) as tag_count, t.name as tag_name
                    FROM commons_post p join commons_post_to_tag pt ON p.id = pt.post_id
                    JOIN commons_tag t ON pt.tag_id = t.id
                    WHERE p.user_id = {user_id}
                    AND p.project_id = {project_id}
                    GROUP BY t.id
                    ORDER BY tag_count;""".format(user_id=int(user_id), project_id=int(project_id))
    cur = connections[db_name].cursor()
    results = execute_query(query, cur)
    return results


def get_project_feed(user_id, project_id):
    task_rows = Post.objects.filter(user_id=user_id, project_id=project_id).order_by(
        "updated_at")
    final_task_details = []
    for row in task_rows:
        temp = {
            'title': row.title,
            'details': row.details,
            'created at': str(row.created_at)
        }
        final_task_details.append(temp)
    return final_task_details


def get_hard_tasks(user_id, project_id):
    task_rows = Post.objects.filter(user_id=user_id, project_id=project_id).order_by(
        "created_at")
    task_time = {}
    task_data = defaultdict(dict)
    total_tasks = len(task_time)
    if total_tasks > 1:
        for i in xrange(0, total_tasks - 1):
            task_timedelta = task_rows[
                i + 1].created_at - task_rows[i].created_at

            task_time[task_rows[i].id] = task_timedelta.days * \
                1440 + task_timedelta.seconds / 60

            task_data[task_rows[i].id] = {
                "title": task_rows[i].title,
                "updated_at": task_rows[i].updated_at
            }
        last_task_timedelta = datetime.datetime.now(
        ) - task_rows[total_tasks - 1].created_at
        task_time[task_rows[total_tasks - 1].id] = last_task_timedelta.days * \
            1440 + last_task_timedelta.seconds / 60
        task_data[task_rows[total_tasks - 1].id] = {
            "title": task_rows[total_tasks - 1].title,
            "updated_at": task_rows[total_tasks - 1].updated_at
        }

    elif total_tasks == 1:

        last_task_timedelta = datetime.datetime.now() - task_rows[0].created_at

        task_time[task_rows[0].id] = last_task_timedelta.days * \
            1440 + last_task_timedelta.seconds / 60
        task_data[task_rows[0].id] = {
            "title": task_rows[0].title,
            "updated_at": task_rows[0].updated_at
        }

    sorted_task_ids = sorted(task_time, key=task_time.get)
    total_minutes = sum(task_time.values())
    results = []
    for task_id in sorted_task_ids:
        temp = {
            "title": task_data[task_id],
            "hardness": task_time * 100 / total_minutes
        }
        results.append(temp)
    return results
