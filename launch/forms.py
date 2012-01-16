from django import forms

class UserEmailsForm(forms.Form):
	email= forms.EmailField()
	feedback = forms.CharField(widget=forms.Textarea, required=False)
