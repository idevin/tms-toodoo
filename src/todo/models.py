from django.db import models


class List(models.Model):
    title = models.CharField(null=False, default=None, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Priority(models.Model):
    title = models.CharField(null=False, default=None, max_length=255)
    color = models.CharField(null=False, default=None, max_length=255)


class Note(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(null=False, default=None, max_length=255)
    content = models.TextField(null=False, default=None)
    sortby = models.IntegerField(default=1)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
