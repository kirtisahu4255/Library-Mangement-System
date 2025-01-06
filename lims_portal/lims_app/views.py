from django.shortcuts import render, redirect
from .models import reader

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def readers(request):
    return render(request, "readers.html", context={"current_tab": "readers"})

def save_student(request):
    student_name = request.POST['student_name']
    return render(request, "welcome.html", context={'student_name': student_name})

def readers_tab(request):
    if request.method == "GET":
        readers = reader.objects.all()
        return render(request, "readers.html", context={"current_tab": "readers", "readers": readers})

    elif request.method == "POST":
        query = request.POST['query']
        readers = reader.objects.filter(reader_name__icontains=query)
        return render(request, "readers.html", context={"current_tab": "readers", "readers": readers,"query":query})

def save_reader(request):
    reader_item = reader(
        reference_id=request.POST['reference_id'],
        reader_name=request.POST['reader_name'],
        reader_contact=request.POST['reader_contact'],
        reader_address=request.POST['reader_address'],
        active=True
    )
    reader_item.save()
    return redirect('/readers')
