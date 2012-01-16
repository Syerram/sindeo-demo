from django.db import models
from django.forms import ModelForm

# Create your models here.
class UserEmails(models.Model):
	email = models.EmailField()
	subscribed = models.BooleanField()
	feedback = models.CharField(max_length=1000, blank=True, null=True) 

	def __unicode__(self):
		return self.email

class UserEmailsModelForm(ModelForm):
	class Meta:
		model= UserEmails
