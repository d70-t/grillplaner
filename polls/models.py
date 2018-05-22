from django.db import models

class Answer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    attends = models.BooleanField(verbose_name="Ich komme!")
    count = models.PositiveIntegerField(verbose_name="Anzahl Personen", default=1)
    brings = models.CharField(max_length=1000, verbose_name="Ich bringe mit", null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

