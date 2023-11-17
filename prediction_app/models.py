# models.py
from django.db import models

class UserInput(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Prediction(models.Model):
    user_input = models.ForeignKey(UserInput, on_delete=models.CASCADE)
    result = models.BooleanField()