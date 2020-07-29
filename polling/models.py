from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    free_answers = models.BooleanField(default=False)
    launched = models.BooleanField(default=False)
    anonymous_answers = models.BooleanField(default=False)
    total_votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)

    def __str__(self):
        return self.choice_text

class User(models.Model):
    username = models.CharField(max_length=25)
    is_professor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
