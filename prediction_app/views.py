# prediction_app/views.py
from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import UserInput, Prediction
import joblib


def index(request):
    return render(request, 'index.html')

def predict_heart_disease(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            # Extract values from the form and convert to a list
            input_values = [form.cleaned_data[field] for field in form.fields]

            # Load the pre-trained model
            model = joblib.load('heart_disease_model.joblib')

            # Predict using the model
            result = model.predict([input_values])[0]

            # Save user input and prediction to the database
            user_input = form.save()
            Prediction.objects.create(user_input=user_input, result=result)

            return render(request, 'prediction_result.html', {'result': result})
    else:
        form = UserInputForm()
    return render(request, 'predict_heart_disease.html', {'form': form})
