from django.shortcuts import render
from django.http import HttpResponse
#import stub
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.

from sklearn.externals import joblib
#clf = joblib.load('C:\Users\Ray\Desktop\classifier\LR_classifier.pkl') 
import pickle
clf = joblib.load('classifier\LR_classifier.pkl') 
vectorizer = pickle.load(open(r'vectorizer\vectorizer.pickle','rb'))
d = {}
with open(r"resolution\label_resolution_share_format.txt") as f:
	for line in f:
		(key, val) = line.split("\t")
	 	d[key] = val
#vectorizer = pickle.load(open(r'C:\Users\Ray\Desktop\vectorizer\vectorizer.pickle','rb'))
def predict(text):
	intention_feature = vectorizer.transform([text])
	if(intention_feature.max()==0):
		max_predict_prob=0
		result=[text]
		return result
	intention_feature = intention_feature.toarray()
	prediction_probability = clf.predict_proba(intention_feature)
	max_predict_prob=prediction_probability.max()
	predict_result=clf.predict(intention_feature)
	print predict_result
	resolution_actions=d[predict_result[0]]
	seperated_resolution_actions=resolution_actions.split("|")
	call_resolution=str.split(str(predict_result),";")
	predict_call_type=call_resolution[0][2:]
	predict_resolution_code=call_resolution[1][:-2]
	result=[text]
	result.append(max_predict_prob)
	result.append(predict_call_type)
	result.append(predict_resolution_code)
	result.append(seperated_resolution_actions)
	return result


def index(request):
	
    context = {}
    return render(request, 'polls/index.html', context)
    
def about(request):
	return render(request, 'polls/about.html',{})
	

def detail(request, text):
	#result = stub.predict(text)
	result = predict(text)
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
