from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .utils import extract_text_from_pdf
from .models import Resume
from .ats import calculate_ats_score
from django.contrib import messages
from .suggestions import generate_suggestions


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

            resume_text = extract_text_from_pdf(resume.resume.path)

            resume.extracted_text = resume_text

            resume.save()

            return redirect("analyze")

    else:

        form = ResumeForm()

    return render(request, "upload_resume.html", {"form": form})



@login_required
def analyze_resume(request):

    resume = Resume.objects.filter(user=request.user).last()

    if resume is None:
        return redirect("upload")

    if request.method == "POST":

        job_description = request.POST.get("job_description")

        result = calculate_ats_score(
            resume.extracted_text,
            job_description
        )

        result["suggestions"] = generate_suggestions(
            result["missing"]
        )

        return render(
            request,
            "result.html",
            {
                "result": result
            }
        )

    return render(
        request,
        "analyze.html",
        {
            "resume": resume
        }
    )