from django.shortcuts import render
from commons.models import User
from django.http import HttpResponse

# Create your views here.
def test(request):
	# x = User(name = 'karra', session_id = 1)
	# x.save()
	# print x
	# return HttpResponse('ddd')
	if request.method == 'POST':
		print request.POST.get('header')
		print request.POST.get('project')
		print request.POST.get('body')
		print request.POST.get('tags')

	return render(request, '/home/dev/hackathon/foobar/worklogger/testing/templates/name.html', {})

def receive_message(request):

	return HttpResponse('abc')