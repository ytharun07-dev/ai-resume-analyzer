from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def upload_resume(request):

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            resume = form.save(commit=False)

            resume.user = request.user

            resume.save()

            return redirect("dashboard")

    else:

        form = ResumeForm()

    return render(request, "upload_resume.html", {"form": form})