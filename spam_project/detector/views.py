from django.shortcuts import render
from .models import model

def home(request):
    result = None

    if request.method == "POST":
        pclass = int(request.POST.get("pclass"))
        sex = int(request.POST.get("sex"))
        age = float(request.POST.get("age"))
        fare = float(request.POST.get("fare"))

        prediction = model.predict([[pclass, sex, age, fare]])

        if prediction[0] == 1:
            result = "✅ Survived"
        else:
            result = "❌ Not Survived"

    return render(request, "home.html", {"result": result})

