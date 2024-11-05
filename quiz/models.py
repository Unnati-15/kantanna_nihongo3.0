from django.db import models
from django.contrib.auth.models import User

class QuizType(models.Model):
    title=models.CharField(max_length=80)
    detail=models.TextField()
    image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='QuizType'

    def __str__(self) :
        return self.title
    

class QuizQuestion(models.Model):
    type=models.ForeignKey(QuizType,on_delete=models.CASCADE)
    question=models.TextField()
    opt1=models.CharField(max_length=80)
    opt2=models.CharField(max_length=80)
    opt3=models.CharField(max_length=80)
    opt4=models.CharField(max_length=80)
    level=models.CharField(max_length=80)
    time_limit=models.IntegerField()
    right_ans=models.CharField(max_length=80)


    class Meta:
        verbose_name_plural='QuizQuestion'

    def __str__(self) :
        return self.question
    
class UserSubmittedAnswer(models.Model):
    question=models.ForeignKey(QuizQuestion,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    right_ans=models.CharField(max_length=80)


    class Meta:
        verbose_name_plural='User Submitted Answers'
