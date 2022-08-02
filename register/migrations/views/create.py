from django.shortcuts import render,redirect
from ...forms import EmployeeForm, EtudiantForm
from ...models import Employee, Etudiant
from django.contrib.auth.decorators import login_required 
from register.decorators import allowed_users

# Create your views here.

# Employee

@login_required(login_url='/employee/login/')
@allowed_users(allowed_roles=['admin'])
def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "register/employee_list.html",context)



@login_required(login_url='/employee/login/')
@allowed_users(allowed_roles=['admin'])
def employee_create(request):
    
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "register/employee_form.html",{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/employee/list')



# Etudiant

@login_required(login_url='/employee/login/')
@allowed_users(allowed_roles=['util'])
def etudiant_list(request):
    context = {'etudiant_list':Etudiant.objects.all()}
    return render(request, "register/etudiant_list.html",context)



@login_required(login_url='/employee/login/')
@allowed_users(allowed_roles=['util'])
def etudiant_create(request):
    
    if request.method == "GET":
        form = EtudiantForm()
        return render(request, "register/etudiant_form.html",{'form':form})
    else:
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('/employee/list1')
