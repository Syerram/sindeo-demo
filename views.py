from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from launch.models import UserEmails
from launch.forms import UserEmailsForm
from launch.models import UserEmailsModelForm

def landing_page(request):
	return render_to_response('landing_page.html', {'form': UserEmailsForm()})

def subscribe(request):
	form = UserEmailsForm(request.POST)
	if form.is_valid():
		cleaned_up_form = form.cleaned_data
		print form.cleaned_data
		usrEmlMdl = UserEmails(email=cleaned_up_form['email'], feedback=cleaned_up_form['feedback'], subscribed=True)
		usrEmlMdl.save()
		return HttpResponseRedirect('/subscribe/thanks/')
	else:
		return render_to_response('landing_page.html', {'form': form})		
def thanku(request):
	return render_to_response('thanku.html')


def hours_ahead(request, offset):
	try:
		offset=int(offset)
	except ValueError:
		raise Http404()
	dt=datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('future_time.html', {'offset':offset, 'future':dt})

def req_meta(request):
	return render_to_response('req_meta.html', {'req': request.META.items()})

def search(request):
	error = False
	if 'q' in request.GET: 
		q = request.GET['q']
		if not q:
			error = True
		else:
			usr_emails = UserEmails.objects.filter(email__icontains=q)
			return render_to_response('search_results.html', {'usr_emails': usr_emails})
	return render_to_response('search_form.html', {'error': error})
