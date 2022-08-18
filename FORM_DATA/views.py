from django.shortcuts import render
from .models import StudentData

# Create your vistudent_dataews here.

def student_data(request):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
    
        s_data=StudentData()
        s_data.id=id
        s_data.name=name
        s_data.email=email
        s_data.contact=contact
        s_data.save()

    return render(request,"index1.html")
