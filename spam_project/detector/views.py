from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import model, vectorizer

def home(request):
    result = None

    if request.method == "POST":
        message = request.POST.get("message")
        msg_vector = vectorizer.transform([message])
        prediction = model.predict(msg_vector)

        if prediction[0] == 1:
            result = "🚨 Spam"
        else:
            result = "✅ Not Spam"

    return render(request, "home.html", {"result": result})