# from django.shortcuts import render

from rest_framework import generics
from .models import Activity
from .serializers import ActivitySerializer
from textblob import TextBlob

# API endpoint (Extension data receive करने के लिए)
class ActivityCreateView(generics.CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Report generate करने के लिए (Normal Django view)
from django.shortcuts import render

def report(request):
    activities = Activity.objects.all().order_by('-timestamp')[:50]
    analysis = []
    for act in activities:
        sentiment = TextBlob(act.title).sentiment.polarity
        mood = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
        analysis.append({
            "url": act.url,
            "title": act.title,
            "mood": mood,
            "timestamp": act.timestamp
        })
    return render(request, 'report.html', {'analysis': analysis})

from django.shortcuts import redirect

def home(request):
    return redirect('report')