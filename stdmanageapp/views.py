from django.shortcuts import render ,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Students

# Create your views here.

def home(request):
    return render(request,'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user:
            login(request,user)
            if user.is_superuser:
                print(user.is_superuser)
                return redirect("admin_dashboard")
            else:
                return redirect("students_view")
       
    return render(request,'login.html')


def student_register(request):
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.create_user(
          
            first_name = fullname,
            username = username,
            password = password 
        )
        user.save()
        print("User Successfully Registered")
        
    return render(request,'register.html')


@login_required
def admin_dashboard(request):
    return render(request,'admin_dashboard.html')


def mark_form(request):
    if request.method == 'POST':
        student_name = request.POST.get("student_name")
        roll_no = request.POST.get("roll_no")
        tamil_mark = int(request.POST.get("tamil_mark"))
        english_mark = int(request.POST.get("english_mark"))
        maths_mark = int(request.POST.get("maths_mark"))
        science_mark =int( request.POST.get("science_mark"))
        social_mark = int(request.POST.get("social_mark"))
        total = tamil_mark + english_mark + maths_mark + science_mark + social_mark
        percentage = (total/500)*100
        
        
        s = Students.objects.create(
            student_name = student_name,
            roll_no = roll_no,
            tamil_mark = tamil_mark,
            english_mark = english_mark,
            maths_mark = maths_mark,
            science_mark = science_mark,
            social_mark = social_mark,
            total = total,
            percentage = percentage
        )
        
        s.save()
        print("Data is saved")
    students = Students.objects.all()
    return render(request,'mark_form.html',{"students" : students})
    


def admin_view(request):
    students = Students.objects.all()
    return render(request,'admin_view.html',{"students" : students})


def update_view(request,id):
    student = Students.objects.get(pk = id)
    if request.method == 'POST':
        student.student_name = request.POST.get("student_name")
        student.roll_no = request.POST.get("roll_no")
        student.tamil_mark = int(request.POST.get("tamil_mark"))
        student.english_mark = int(request.POST.get("english_mark"))
        student.maths_mark = int(request.POST.get("maths_mark"))
        student.science_mark = int(request.POST.get("science_mark"))
        student.social_mark = int(request.POST.get("social_mark"))
        student.total = student.tamil_mark + student.english_mark + student.maths_mark + student.science_mark + student.social_mark
        student.percentage = (student.total/500)*100
        student.save()
        print("Updated Successfully")
        return redirect("admin_view")
    return render(request,'update_form.html',{'student': student})

    
   


def delete(request,id):
    student = Students.objects.get(pk = id)
    student.delete()
    messages.success(request, f"Student {student.student_name} deleted....")
    return redirect('admin_view')


@login_required
def students_view(request):
    username = request.user.first_name
    students = Students.objects.all()
    return render(request,'students_view.html',{"students" : students,"username" : username})
   


def sign_out(request):
    logout(request)
    return redirect("home")