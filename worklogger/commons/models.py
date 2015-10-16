from django.contrib.gis.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    organisation = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    session_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    name = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=255, blank=True)
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)    


class Post(models.Model):
    user_id = models.ForeignKey(User)
    project_id = models.ForeignKey(Project)
    title = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_type = models.IntegerField(blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True)
    count = models.IntegerField(blank=True)

class Post_To_Tag(models.Model):
    post_id = models.ForeignKey(Post)
    tag_id = models.ForeignKey(Tag)
    


        
