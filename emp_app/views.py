from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from . models import Department,Role,Employee
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def View_emp(request):
    emps=Employee.objects.all()
    context={
        "emps":emps
    }

    return render(request,"View_emp.html",context)

def Add_emp(request):
    if request.method=="POST": 
       first_name=request.POST["first_name"]
       last_name=request.POST["last_name"]
       salary=int(request.POST["salary"])
       bonus=int(request.POST["bonus"])
       mobile_no=int(request.POST["mobile_no"])
       role=int(request.POST["role"])
       dept=int(request.POST["dept"])
       new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,mobile_no=mobile_no,role_id=role,dept_id=dept)
       new_emp.save()
       return HttpResponse("Employee added Sucessfull")
    elif request.method=="GET":
        return render(request,"Add_emp.html")
    else:
        return HttpResponse("An Accseption acccur")




    

def Remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("delet Employee Detail")
        except:
            return HttpResponse("plz insert valid input id")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,"Remove_emp.html",context)

def Filter_emp(request):
    if request.method=="POST":
        name=request.POST["name"]
        role=request.POST["role"]
        dept=request.POST["dept"]
        emps=Employee.objects.all()

        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if role:
            emps=emps.filter(role__name=role)
        if dept:
            emps=emps.filter(dept__name=dept)
        context={
            "emps":emps
        }
        return render(request,"View_emp.html",context)

    elif request.method=="GET":


        return render(request,"filter_emp.html")
    else:
        return HttpResponse("An Accseption acccur")

def Update_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_modify=Employee.objects.get(id=emp_id)
            emp_to_be_modify.first_name="rahul"
            emp_to_be_modify.save()
            

        except:
            return HttpResponse("please fill correct value")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,"Update_emp.html",context)


        

    