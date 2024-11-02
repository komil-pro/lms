from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Student
from django.template import loader

def index(request):
    students = Student.objects.all()
    template = loader.get_template("students/index.html")
    context = {
        "students": students,
    }
    return HttpResponse(template.render(context, request))

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, "students/detail.html", {"student": student})
