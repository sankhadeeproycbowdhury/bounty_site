from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@ login_required(login_url="/login/")
def receipes(request):
    if request.method == 'POST':
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
        receipe_name = receipe_name,
        receipe_description = receipe_description,
        receipe_image = receipe_image,

        )
        return redirect('/receipes/')
    
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipes' : queryset}

    return render(request , 'receipes.html' , context)




@ login_required(login_url="/login/")
def update(request ,id ):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')
        

    context = {'receipe' : queryset}
    return render(request , 'update_receipes.html' , context)




@ login_required(login_url="/login/")
def delete(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes/')




def login_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid UserName.")
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if user is None:
            messages.info(request, "Invalid Password.")
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/receipes/')

    return render(request , 'login.html')




def logout_page(request):
    logout(request)
    return redirect('/login/')




def register_page(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully.")
        return redirect('/register/')

    return render(request , 'register.html')
    


from django.db.models import Q,Sum

def get_students(request):
    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) 
            )
    
    paginator = Paginator(queryset, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request , 'report/students.html' , {'queryset' : page_obj})



# just a seed Fuction
def generate_report_card():
    current_rank = -1
    
    ranks = Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks','-student_age')
    i = 0
    
    for rank in ranks:
        i=i+1
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )



def see_marks(request , student_id):
    #generate_report_card()    
    querryset = SubjectMarks.objects.filter(student__student_id__Student_id = student_id)
    #total_marks = querryset.aggregate(total_marks = Sum('marks'))
    
    return render(request , 'report/see_marks.html' , {'queryset' : querryset})
   
    
