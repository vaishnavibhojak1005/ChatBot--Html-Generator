from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        # Send this to Hugging Face model
        response = requests.post(
            "https://api-inference.huggingface.co/models/Salesforce/codegen2",
            headers={"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"},
            json={"inputs": user_message}
        )

        result = response.json()
        generated_html = result[0]["generated_text"] if isinstance(result, list) else result.get("generated_text", "")
        return JsonResponse({"html": generated_html})

    return JsonResponse({"error": "Invalid request"})

def home_view(request):
    return render(request, "bot/home.html")
