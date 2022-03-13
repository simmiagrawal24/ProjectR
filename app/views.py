from xml.dom.minidom import TypeInfo
from django.shortcuts import render
from django.http import HttpResponse
from .models import projinfo, stud


def find_proj(request):

    f = open('projdata.txt')
    projdata = f.read()
    projdata = projdata.splitlines()
    search = 'biosciences'
    proj1= projinfo()
    proj2= projinfo()
    proj3= projinfo()
    cnt=1

    for val in projdata:
        if search in val:
            val = val.split(sep='_')
            if cnt==1:
                proj1.profname = val[1]
                proj1.desc = val[2]
                proj1.duration = val[3]
            if cnt==2:
                proj2.profname = val[1]
                proj2.desc = val[2]
                proj2.duration = val[3]
            if cnt==3:
                proj3.profname = val[1]
                proj3.desc = val[2]
                proj3.duration = val[3]
            cnt=cnt+1
    
    projs = [proj1,proj2,proj3]
    
    return render(request, 'ProjectR-main/search_project.html', {'projs':projs})

def profile(request, no):

    student = stud()

    f = open('2.txt')
    studdata = f.read()
    studdata = studdata.splitlines()
    roll='2'
    temp=[]

    for val in studdata:
            val = val.split(sep='_')
            if val[0]==roll:
                temp= val
                break
    
    student.about = temp[2]
    student.skill = temp[3]
    student.cert = temp[4]
    student.exp = temp[5]
    student.lang = temp[6]
    student.interest = 'none'
    student.prev = temp[7]

    return render(request, 'ProjectR-main/student_profile.html', {'student': student} )

def home(request):

    return render(request, 'ProjectR-main/Home_page.html' )

def login(request):

    return render(request, 'ProjectR-main/login_page.html' )

def track(request):

    return render(request, 'ProjectR-main/current_status.html' )

def create(request):

    return render(request, 'ProjectR-main/project_page.html' )

def req(request):

    proj = projinfo()

    f = open('projdata.txt')
    project = f.read()
    project = project.splitlines()
    roll='5'
    temp=[]

    for val in project:
            val = val.split(sep='_')
            if val[0]==roll:
                temp= val
                break
    
    proj.projname = temp[4]
    proj.profname = temp[1]
    proj.desc = temp[2]
    proj.duration = temp[3]

    return render(request, 'ProjectR-main/request_project.html', {'proj':proj})

def sel(request):

    return render(request, 'ProjectR-main/studentorprof.html' )
    
def inter(request):

    pwd = request.GET.get('pwd', 'abc')
    
    if pwd=='abc':
        return render(request, 'ProjectR-main/Home_page.html' )
    else:
        return HttpResponse('incorrect password')

def search(request):

    search = request.GET.get('mySearch', 'biosciences')
    return render(request, 'search_project.html')
    
def ser(request):

    return render(request, 'ProjectR-main/search.html')
