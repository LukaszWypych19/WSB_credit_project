import datetime
from django.db import models
from django.utils import timezone


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f'Pytanie o treści: {self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Odpowiedź: {self.choice_text} z {self.votes} glosami'