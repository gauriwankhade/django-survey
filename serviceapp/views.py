from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def HomeView(request) :

    if request.method == "POST" :
        return redirect('questions/')

    return render(request, 'index.html', {})

def get_sessionkey(session) :

    if not session.exists(session.session_key) :
        print("\nCreating new session ")
        session.create() 

    return session.session_key



def QuestionView(request) :
    session_key = get_sessionkey(request.session)
    survey_session, created = SurveySession.objects.get_or_create(session_key=session_key)

    if request.method == "POST" :
        results = request.POST
        queIds = [ str(obj.id) for obj in  Question.objects.all() ]
        print(queIds)
        for que in queIds :
            question = Question.objects.get(pk=que)
            answer = results[que] 
            ansObj, create = SurveyAnswer.objects.get_or_create(session=survey_session, question=question)
            ansObj.answer = answer
            ansObj.save()

        survey_session.completed = True
        survey_session.save()
        return JsonResponse({'response':'success'})

    return render(request, 'questions.html', {})



def QuestionRetrive(request):
    data = list(Question.objects.values()) 
    newData = {}

    for i in range(len(data)) :
        newData[i+1] = data[i]

    return JsonResponse({'data': newData})



