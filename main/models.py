from django.db import models
from django.forms import ModelForm

from auth.models import User

class Content(models.Model):
        content_type = models.CharField(max_lenth=5, blank=False, null=False)
	title = models.CharField(max_length=15, blank=False, null=False)
	owner = models.ForeignKey(User)
	creation_date = models.DateField()
        def __unicode__(self):
                return self.title

class Workspace(models.Model):
	title = models.CharField(max_length=15, blank=False, null=False)
	author = models.ForeignKey(User)
	last_updated = models.DateField()
	comments = models.ManyToManyField(WorkspaceComment)	
	contents = models.ManyToManyField(Content, through='WorkspaceContent')

class WorkspaceComment(models.Model):
	workspace = models.ForeignKey(Workspace)
	commenter = models.ForeignKey(User)
	comment = models.CharField(max_length=255, blank=True, null=True)
	creation_date = models.DateField()

class WorkspaceContent(models.Model):
	workspace = models.ForeignKey(Workspace)
	content = models.ForeignKey(Content)
	last_updated = models.DateField()
	creation_date = models.DateField()


