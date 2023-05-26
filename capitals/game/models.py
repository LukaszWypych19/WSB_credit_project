import datetime
from django.db import models
from django.utils import timezone


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


class Countries(models.Model):
    countries = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.countries}'

    class Meta:
        managed = True
        db_table = 'countries'


class Cities(models.Model):
    # countries = models.ForeignKey(Countries, on_delete=models.CASCADE)
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
