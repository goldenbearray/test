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