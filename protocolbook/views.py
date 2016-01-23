from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Protocol

# Create your views here.
def index(request):
	latest_protocol_list = Protocol.objects.order_by('protocolNo')
	template = loader.get_template('protocolbook/index.html')
	context = {
		'latest_protocol_list': latest_protocol_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, protocol_id):
	protocol = Protocol.objects.filter(pk=protocol_id)
	template = loader.get_template('protocolbook/detail.html')
	context = {
		'protocol': protocol,
	}
	return HttpResponse(template.render(context, request))