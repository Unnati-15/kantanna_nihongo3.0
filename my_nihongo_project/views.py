
from django.http import HttpResponse
from translate import Translator
from django.shortcuts import render
from django.db import models
from flashcard.models import FlashCard
from flashcard import models
from quiz import models
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request,'templates/home.html')
def phrases(request):
    return render(request,'templates/PHRASES.html')

def hiragana(request):
    typeData=models.QuizType.objects.filter(title='Hiragana Test').values()
    return render(request,'templates/HIRAGANA.html',{'typeData':typeData})

def katakana(request):
    typeDatak=models.QuizType.objects.filter(title='Katakana Test').values()
    return render(request,'templates/KATAKANA.html',{'typeDatak':typeDatak})

def translate(request):
    if request.method == 'POST':

        text = request.POST['translate']
        to_lang = request.POST['tolanguage']
        from_lang = request.POST["fromlanguage"]
        translator = Translator(to_lang=to_lang, from_lang=from_lang)
        translation = translator.translate(text)
        
        context = {
            'translation': translation,
            
        }
        return render(request,'templates/translation.html', context)
    return render(request, 'templates/translation.html')

def kanji(request):
    return render(request,'templates/KANJI.html')

def examdetails(request):
    return render(request,'templates/EXAMDETAILS.html')

def resources(request):
    return render(request,'templates/RESOURCES.html')

def contact(request):
    return render(request,'templates/CONTACT.html')

def aboutus(request):
    return render(request,'templates/ABOUTUS.html')


@login_required
def flashcard(request):
    if request.method == 'POST':
        data = request.POST
        user=request.user
        fc_name = data.get('fc_name')
        fc_description = data.get('fc_description')

        FlashCard.objects.create(
            user=user,
            fc_name=fc_name,
            fc_description=fc_description,
        )
        return render(request,'templates/flashcard.html')

    queryset = FlashCard.objects.filter(user=request.user)

    context = {'flashcard': queryset}
    return render(request, 'templates/flashcard.html', context)

@login_required
def delete_flashcard(request, id):
    queryset = FlashCard.objects.get(id=id)
    queryset.delete()
    return render(request,'templates/flashcard.html')

@login_required
def update_flashcard(request, id):
    queryset = FlashCard.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        fc_name = data.get('fc_name')
        fc_description = data.get('fc_description')
        queryset.fc_name = fc_name
        queryset.fc_description = fc_description
        queryset.save()
    context = {'flashcard': queryset}
    return render(request, 'update_flashcard.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created successfully')
    
        return render(request,'templates/registration/LOGIN.html')
    else:
        return render(request,'templates/registration/REGISTER.html')

def login(request):
    if request.method == 'POST':
          username=request.POST['username']
          password1=request.POST['password']

          user=auth.authenticate(username=username,password=password1)
          if user is not None:
            auth.login(request,user)
            
            return render(request,'templates/PHRASES.html')
            
          else:
            messages.info(request,'invalid credentials')
            return render(request,'templates/registration/LOGIN.html')
    else:
        return render(request,'templates/registration/LOGIN.html')
    
@login_required
def hiraganaquiz(request,h_id):
       if not request.user.is_authenticated:
           return render(request,'templates/registration/LOGIN.html')
       else:
            h=models.QuizType.objects.get(id=h_id)
            q1=models.QuizQuestion.objects.filter(type=h).order_by('id').first()
            return render(request,'templates/HIRAGANAQUIZ.html',{'q1':q1 ,'h':h})

@login_required
def submitanswer(request,h_id,q_id):
       if request.method=='POST':
           h=models.QuizType.objects.get(id=h_id)
           q1=models.QuizQuestion.objects.filter(type=h,id__gte=q_id).exclude(id=q_id).order_by('id').first()
           
           if 'skip' in request.POST:
               if q1:
                   quest=models.QuizQuestion.objects.get(id=q_id)
                   user=request.user
                   answer='Not Submitted'
                   models.UserSubmittedAnswer.objects.create(user=user,quest=quest,right_answer=answer)
                   return render(request,'templates/HIRAGANAQUIZ.html',{'q1':q1 ,'h':h})
           else:
               quest=models.QuizQuestion.objects.get(id=q_id)
               user=request.user
               answer=request.POST['answer']
               models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_ans=answer)
           if q1:
                return render(request,'templates/HIRAGANAQUIZ.html',{'q1':q1 ,'h':h})
           
           result=models.UserSubmittedAnswer.objects.filter(user=request.user)
           return render(request,'templates/HIRAGANARESULT.html',{'result':result})
       else:
           return HttpResponse("method not allowed")
       
@login_required
def katakanaquiz(request,k_id):
       if not request.user.is_authenticated:
           return render(request,'templates/registration/LOGIN.html')
       else:
            k=models.QuizType.objects.get(id=k_id)
            q2=models.QuizQuestion.objects.filter(type=k).order_by('id').first()
            return render(request,'templates/KATAKANAQUIZ.html',{'q2':q2 ,'k':k})

@login_required
def submitanswerk(request,k_id,q2_id):
       if request.method=='POST':
           k=models.QuizType.objects.get(id=k_id)
           q2=models.QuizQuestion.objects.filter(type=k,id__gte=q2_id).exclude(id=q2_id).order_by('id').first()
           
           if 'skip' in request.POST:
               if q2:
                   quest=models.QuizQuestion.objects.get(id=q2_id)
                   user=request.user
                   answer='Not Submitted'
                   models.UserSubmittedAnswer.objects.create(user=user,quest=quest,right_answer=answer)
                   return render(request,'templates/KATAKANAQUIZ.html',{'q2':q2 ,'k':k})
           else:
               quest=models.QuizQuestion.objects.get(id=q2_id)
               user=request.user
               answer=request.POST['answer']
               models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_ans=answer)
           if q2:
                return render(request,'templates/KATAKANAQUIZ.html',{'q2':q2,'k':k})
           
           resultk=models.UserSubmittedAnswer.objects.filter(user=request.user)
           return render(request,'templates/HIRAGANARESULT.html',{'resultk':resultk})
       else:
           return HttpResponse("method not allowed")


def logout(request):
    auth.logout(request)
    return render(request,'templates/registration/LOGIN.html')

@login_required
def result(request):
    result=models.UserSubmittedAnswer.objects.filter(user=request.user)
    resultk=models.UserSubmittedAnswer.objects.filter(user=request.user)
    return render(request,'templates/HIRAGANARESULT.html',{'result':result,'resultk':resultk})