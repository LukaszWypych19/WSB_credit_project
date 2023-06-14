import datetime
from django.db import models
from django.utils import timezone



class Countries(models.Model):
    countries = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.countries}'

    class Meta:
        managed = True
        db_table = 'countries'


class Cities(models.Model):
    countries = models.OneToOneField(Countries, on_delete=models.CASCADE, null=True)
    cities = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.cities}'

    class Meta:
        managed = True
        db_table = 'cities'


class Cc(models.Model):
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.country} - {self.city}'

    class Meta:
        managed = True
        db_table = 'cc'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return f'{self.username}'
        # return f'{self.id} - {self.username}'

    class Meta:
        managed = False
        db_table = 'auth_user'



class History(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)
    username_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question} - {self.correct_ans} - {self.username_id}'

    class Meta:
        managed = True
        db_table = 'history'



# class Questions(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#
#     def __str__(self):
#         return f'Pytanie o treści: {self.question_text}'
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f'Odpowiedź: {self.choice_text} z {self.votes} glosami'

