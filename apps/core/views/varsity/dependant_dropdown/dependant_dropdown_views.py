from django.shortcuts import render, redirect
from apps.university.models import *
from apps.account.models.profile_models import Profile
from apps.account.models.education_models import EduUniversity

def load_universities(request):
    university_type_id = request.GET.get('university_type_id')
    universities = University.objects.filter(university_type_id=university_type_id).all()
    return render(request, 'varsity/dependant_dropdown/university_dropdown_list_options.html', {'universities': universities})

def load_faculties(request):
    university_id = request.GET.get('university_id')
    faculties = Faculty.objects.filter(university_id=university_id).all()
    # print(faculties)
    return render(request, 'varsity/dependant_dropdown/faculty_dropdown_list_options.html', {'faculties': faculties})


def load_departments(request):
    university_id = request.GET.get('university_id')
    faculty_id = request.GET.get('faculty_id')
    # university_id = 2
    # faculty_id =
    departments = Department.objects.filter(university_id=university_id, faculty_id = faculty_id).all()
    return render(request, 'varsity/dependant_dropdown/department_dropdown_list_options.html', {'departments': departments})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    
def load_courses(request):
    # university_id = request.GET.get('university_id')
    # department_id = request.GET.get('department_id')
    user = request.user
    profile = Profile.objects.get(user=user)
    edu_university = EduUniversity.objects.get(profile=profile)
    university_id = edu_university.university.id
    department_id = None
    if edu_university.department:
        department_id = edu_university.department.id
    
    discipline_id = None
    if edu_university.discipline:
        discipline_id = edu_university.discipline.id
        
    semester = request.GET.get('semester')
    # year = request.GET.get('year')
    courses = Course.objects.filter(university_id=university_id, department_id = department_id, discipline_id=discipline_id,  semester = semester).all()
    return render(request, 'varsity/dependant_dropdown/course_dropdown_list_options.html', {'courses': courses})