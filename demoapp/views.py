from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
#import pdb;pdb.set_trace()
from demoapp.models import Data

# Create your views here.

def home(request):
	data = Data.objects.all()
	return render_to_response('home.html',{'data':data},context_instance=RequestContext(request))

def add(request):
	if request.method == 'POST':
		data = Data()
		data.name = request.POST['name']
		data.email = request.POST['email'] 
		data.phone = request.POST['phone']
		data.save()
		return redirect('home')
	else:
		return render_to_response('add.html',context_instance=RequestContext(request))
