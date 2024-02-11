from django.shortcuts import render
import datetime
def home(request):
    print("This method is hit")
    date  =  datetime.datetime.now()
    student_details = {
        "name" :"abc",
        "college" : "XYZZ",
        "RollNo" : "1"
    }
    subjects = ["AAAAAa","BBBBBBBbbb","CCCCCCCCCCc","DDDDDD"]

    data = {
        "date" : date,
        "student" :student_details,
        "isActive" :True,
        "subjects":subjects
    }
    return render(request,"home.html",data)

def about(request):
    if request.POST:
        check =request.POST['check']
        print(check)
    print("This method is hit : about")
    return render(request,"about.html",{})
