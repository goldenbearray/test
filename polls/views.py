from django.shortcuts import render
from django.http import HttpResponse
import stub
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm


# Create your views here.
def index(request):
	
    context = {}
    return render(request, 'polls/index.html', context)
    
def about(request):
	return render(request, 'polls/about.html',{})
	

def detail(request, text):
	result = stub.predict(text)
	if len(result)==1:
		Intention=result[0]
		return render(request, 'polls/no_feature.html',{'Intention':Intention})
	Intention=result[0]
	Prediction_probability=result[1]
	call_type=result[2]
	resolution_code=result[3]
	seperated_resolution_action=result[4]
	return render(request, 'polls/result.html', {'Intention':Intention, 'Prediction_probability':Prediction_probability, 'call_type':call_type, 'resolution_code':resolution_code,'seperated_resolution_action':seperated_resolution_action})
#	return HttpResponse(html_result)

def query(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            text = form.cleaned_data['intention']
            #print text
            # redirect to a new URL:
            url = '/polls/detail/' + text
            return HttpResponseRedirect(url)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})
