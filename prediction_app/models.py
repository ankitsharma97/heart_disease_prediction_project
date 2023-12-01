# models.py
from django.db import models

class UserInput(models.Model):
    age = models.IntegerField()# age - age in years
    sex = models.IntegerField()# sex - sex (1 = male; 0 = female)
    cp = models.IntegerField()# cp - chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 4 = asymptomatic)
    trestbps = models.IntegerField()# trestbps - resting blood pressure (in mm Hg on admission to the hospital)
    chol = models.IntegerField()# chol - serum cholestoral in mg/dl
    fbs = models.IntegerField()# fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
    restecg = models.IntegerField()# restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)
    thalach = models.IntegerField()# thalach - maximum heart rate achieved
    exang = models.IntegerField()# exang - exercise induced angina (1 = yes; 0 = no)
    oldpeak = models.FloatField()# oldpeak - ST depression induced by exercise relative to rest
    slope = models.IntegerField()# slope - the slope of the peak exercise ST segment (1 = upsloping; 2 = flat; 3 = downsloping)
    ca = models.IntegerField()# ca - number of major vessels (0-3) colored by flourosopy
    thal = models.IntegerField()# thal - 3 = normal; 6 = fixed defect; 7 = reversable defect

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Prediction(models.Model):
    user_input = models.ForeignKey(UserInput, on_delete=models.CASCADE)
    result = models.BooleanField()

