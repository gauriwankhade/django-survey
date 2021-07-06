from django.db import models

# Create your models here.

class Question(models.Model) :

    CHOICES = (('TEXT', 'TEXT'),
               ('RATING', 'RATING'))

    question_details = models.TextField(blank=True, null=True)
    answer_type = models.CharField(choices=CHOICES, max_length=50)
    rating_limit = models.IntegerField(blank=True, null=True)


    def __str__(self) :
        return str(self.id)



class SurveySession(models.Model) :

    session_key = models.CharField(max_length=255, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 


    def __str__(self) :
        return self.session_key


class SurveyAnswer(models.Model) :

    session = models.ForeignKey(SurveySession, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    
    def __str__(self) :
        return self.session.session_key + ' Answer of Question: ' + str(self.question.id)

