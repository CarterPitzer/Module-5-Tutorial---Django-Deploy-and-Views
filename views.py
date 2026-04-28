from django.shortcuts import render
from datetime import datetime

def post_list(request):
    context = {
        "username": "Carter",
        "current_time": datetime.now(),
        "items": ["Apples", "Bananas", "Carrots"]
    }
    return render(request, "blog/post_list.html", context)
