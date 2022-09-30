from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):

    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }

    return render(request, "app_pairpjt1/index.html", context)


def review(request):

    return render(request, "app_pairpjt1/review.html")


def create(request):

    title = request.GET.get("title")
    content = request.GET.get("content")

    Review.objects.create(title=title, content=content)

    return redirect("pjt1:index")
