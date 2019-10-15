from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

import json

import pycrfsuite_spacing
from pycrfsuite_spacing import CharacterFeatureTransformer
from pycrfsuite_spacing import TemplateGenerator
from pycrfsuite_spacing import PyCRFSuiteSpacing

model_path = 'model/review_space.crfsuite'

@csrf_exempt 
def spacing_view(request):
    return render(request, 'spacing/index.html', {
        'step':'step 1'
    })

@csrf_exempt 
def check_spacing(request):
	# if( request.method == 'POST'):
        # raise Exception('Allow get method Only')
	# else:
        # request.
    spacingModel = modelInit()
    textValue = request.POST.get("textValue")
    
    result = spacingModel(textValue)
    print(result)
    responseData = {"result":result}

    return HttpResponse(
        json.dumps(responseData), 
        content_type="application/json")


def modelInit():
    print('modelInit !!')
    to_feature = CharacterFeatureTransformer(
        TemplateGenerator(begin=-2, 
        end=2,
        min_range_length=3,
        max_range_length=3)
    )

    correct = PyCRFSuiteSpacing(
        to_feature = to_feature,
        feature_minfreq=3, # default = 0
        max_iterations=100,
        l1_cost=1.0,
        l2_cost=1.0
    )
    
    correct = PyCRFSuiteSpacing(to_feature)
    correct.load_tagger(model_path)
    return correct