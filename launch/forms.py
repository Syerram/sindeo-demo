from django import forms
from launch.models import UserEmails 

class UserEmailsForm(forms.Form):
	email= forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea, required=False)

	def clean_email(self):
		email_raw= self.cleaned_data['email']
		email_in_db = UserEmails.objects.filter(email__icontains=email_raw)
		if(email_in_db):
			raise forms.ValidationError('it seems you have already subscribed. thanks for checking up again.')
		return email_raw
