from django.shortcuts import render
from .models import student
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'pages/index.html')


def form(request):
    if request.method=='POST':
        id = request.POST.get('Id')
        username = request.POST.get('Name')
        date_birth = request.POST.get('date_birth')
        faculty = request.POST.get('Faculty')
        phone = request.POST.get('Phone')
        address = request.POST.get('address')
        relative = request.POST.get('Next of kin')
        if student.objects.filter(student_id=id).exists():
            return HttpResponse('A student with this ID already exists.')
        data = student(student_id=id,name=username,Date=date_birth,Faculty=faculty,Phone=phone,ADDRESS=address,nex=relative)
        data.save()

    return render(request,'pages/form.html')



def view(request):
    x={'pro':student.objects.all()}
    return render(request,'pages/std_display.html',x)
def search(request):
    search_std = None
    if request.method == 'POST':
        # Handling search
        if 'std_search' in request.POST:
            std = request.POST['std_search']
            search_std = student.objects.filter(student_id=std)
        if 'delete' in request.POST:
            delete_id = request.POST['delete']
            delete_std = student.objects.filter(student_id=delete_id)
            if delete_std:
                delete_std.delete()

    data = {'std': search_std}
    return render(request, 'pages/std_search.html', data)
