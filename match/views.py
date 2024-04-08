from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login ,logout # Import as auth_login
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .algos.use import use
from .forms import CustomUserCreationForm
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')



@csrf_exempt
def results_view(request):
    jobTitle = request.POST['jobTitle']
    skills = request.POST['skills'].split(',')
    jobType = request.POST['job-type']

    resultData = use(jobTitle, jobType, skills)
    data = []
    for key in resultData['jobtitle'].keys():
        data.append([resultData['joblocation_address'][key], resultData['jobtitle'][key], resultData['company'][key],
        resultData['skills'][key], resultData['employmenttype_jobstatus'][key]])
    context = {
        'data' : data
    }
    return render(request, 'results.html', context)

@csrf_exempt
def tests_view(request):
    userData = [['Javascript Dev', 'full time', ['html', 'css', 'javascript', 'python', 'git']],
    ['Python Developer', 'full time', ['javascript', 'python', 'django', 'flask']],
    ['AI Developer', 'full time', ['python', 'numpy', 'flask']], ['Machine learning Developer', 'full time', ['html', 'css', 'js']]]

    resultRefinedData = {}
    for uData in userData:
        uData = (uData[0], uData[1], tuple(uData[2]))
        testResultData = use(uData[0], uData[1], uData[2])


        data = []
        for key in testResultData['jobtitle'].keys():
            data.append([testResultData['joblocation_address'][key], testResultData['jobtitle'][key], testResultData['company'][key],
            testResultData['skills'][key], testResultData['employmenttype_jobstatus'][key]])

        resultRefinedData[tuple(uData)] = tuple(data)

    context = {
        'data' : resultRefinedData
    }
    return render(request, 'tests.djhtml', context)
