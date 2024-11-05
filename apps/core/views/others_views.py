from django.shortcuts import render, redirect
from apps.account.models.profile_models import *
from apps.account.models.education_models import *
from django.db.models import Q
from ..forms import *


def search_results(request):
    university = None
    department = None
    discipline = None
    faculty = None
    institute = None
    school = None
    center = None
    profile = None

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            edu_university = EduUniversity.objects.filter(profile=profile).first()
            university = edu_university.university if edu_university else None
            faculty = edu_university.faculty if edu_university else None
            institute = edu_university.institute if edu_university else None
            school = edu_university.school if edu_university else None
            center = edu_university.center if edu_university else None
            department = edu_university.department if edu_university else None
            discipline = edu_university.discipline if edu_university else None
            # semester = edu_university.semester if edu_university else None
        except Profile.DoesNotExist:
            profile = None
    else:
        profile = None
            
    query = request.GET.get('q', '')
    
    if query:
        universities = University.objects.filter(
            Q(acronym__icontains=query) |
            Q(name__icontains=query) |
            Q(location_district__icontains=query) |
            Q(location_division__icontains=query)
        )
        
        faculties = Faculty.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        institutes = Institute.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        schools = School.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        centers = Center.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )

        departments = Department.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        disciplines = Discipline.objects.filter(
            Q(name__icontains=query) |
            Q(university__name__icontains=query)
        )
        
        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query) |
            Q(department__name__icontains=query) |
            Q(department__university__name__icontains=query)
        )
        
        profiles = Profile.objects.filter(
            Q(user__username__icontains=query) |
            Q(fullname__icontains=query) |
            Q(nickname__icontains=query) |
            Q(email__icontains=query)
        )

        total_search_results_universities = universities.count()
        total_search_results_faculties = faculties.count()
        total_search_results_institutes = institutes.count()
        total_search_results_centers = centers.count()
        total_search_results_schools = schools.count()
        total_search_results_departments = departments.count()
        total_search_results_disciplines = disciplines.count()
        total_search_results_courses = courses.count()
        total_search_results_profiles = profiles.count()
    else:
        universities = University.objects.all()
        faculties = Faculty.objects.all()
        institutes = Institute.objects.all()
        schools = School.objects.all()
        centers = Center.objects.all()
        departments = Department.objects.all()
        disciplines = Discipline.objects.all()
        courses = Course.objects.all()
        profiles = Profile.objects.all()
        
        total_search_results_universities = universities.count()
        total_search_results_faculties = faculties.count()
        total_search_results_institutes = institutes.count()
        total_search_results_centers = centers.count()
        total_search_results_schools = schools.count()
        total_search_results_departments = departments.count()
        total_search_results_disciplines = disciplines.count()
        total_search_results_courses = courses.count()
        total_search_results_profiles = profiles.count()

    context = {
        'university': university,
        'faculty': faculty,
        'institute': institute,
        'school': school,
        'center': center,
        'department': department,
        'discipline': discipline,
        
        'universities': universities,
        'faculties': faculties,
        'institutes': institutes,
        'schools': schools,
        'centers': centers,
        'departments': departments,
        'disciplines': disciplines,
        
        'courses': courses,
        'profile': profile,
        'profiles': profiles,
        
        'total_search_results_universities': total_search_results_universities,
        'total_search_results_faculties': total_search_results_faculties,
        'total_search_results_institutes': total_search_results_institutes,
        'total_search_results_centers': total_search_results_centers,
        'total_search_results_schools': total_search_results_schools,
        'total_search_results_departments': total_search_results_departments,
        'total_search_results_disciplines': total_search_results_disciplines,
        'total_search_results_courses': total_search_results_courses,
        'total_search_results_profiles': total_search_results_profiles,
        'query': query,
        'is_home': True,
    }

    return render(request, 'search_results.html', context)
