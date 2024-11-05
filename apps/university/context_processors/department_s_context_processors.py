# from apps.university.models import *
# from django.db.models import Sum

# def department_s_context_view(request):
#     # user = request.user.id
#     department_id = None

#     # Assuming department_id is passed in the URL, for example: /department/1/
#     if 'department_id' in request.resolver_match.kwargs:
#         department_id = request.resolver_match.kwargs['department_id']

#     # TOTAL COURSES - SEMESTER WISE==========================
#     courses_sem1 = Course.objects.filter(department = department_id, semester='1st').count()
    
#     courses_sem2 = Course.objects.filter(department = department_id, semester='2nd').count()
    
#     courses_sem3 = Course.objects.filter(department = department_id, semester='3rd').count()
    
#     courses_sem4 = Course.objects.filter(department = department_id, semester='4th').count()
    
#     courses_sem5 = Course.objects.filter(department = department_id, semester='5th').count()
    
#     courses_sem6 = Course.objects.filter(department = department_id, semester='6th').count()
    
#     courses_sem7 = Course.objects.filter(department = department_id, semester='7th').count()
    
#     courses_sem8 = Course.objects.filter(department = department_id, semester='8th').count()
    
#     total_courses_s = Course.objects.filter(department = department_id).count()
    
#     # TOTAL CREDITS SEMESTER WISE===============================
#     credits_sem1 = Course.objects.filter(department = department_id, semester='1st').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem2 = Course.objects.filter(department = department_id, semester='2nd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem3 = Course.objects.filter(department = department_id, semester='3rd').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem4 = Course.objects.filter(department = department_id, semester='4th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem5 = Course.objects.filter(department = department_id, semester='5th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem6 = Course.objects.filter(department = department_id, semester='6th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem7 = Course.objects.filter(department = department_id, semester='7th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0
    
#     credits_sem8 = Course.objects.filter(department = department_id, semester='8th').aggregate(total_credits_s=Sum('credit'))['total_credits_s'] or 0

#     total_credits_s = credits_sem1 + credits_sem2 + credits_sem3 + credits_sem4 + credits_sem5 + credits_sem6 + credits_sem7 + credits_sem8
   
   
#     # TOTAL HOURS SEMESTER WISE===============================
#     hours_sem1 = Course.objects.filter(department = department_id, semester='1st').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem2 = Course.objects.filter(department = department_id, semester='2nd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem3 = Course.objects.filter(department = department_id, semester='3rd').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem4 = Course.objects.filter(department = department_id, semester='4th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem5 = Course.objects.filter(department = department_id, semester='5th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem6 = Course.objects.filter(department = department_id, semester='6th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem7 = Course.objects.filter(department = department_id, semester='7th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     hours_sem8 = Course.objects.filter(department = department_id, semester='8th').aggregate(total_hours_s=Sum('hour'))['total_hours_s'] or 0
    
#     total_hours_s = hours_sem1 + hours_sem2 + hours_sem3 + hours_sem4 + hours_sem5 + hours_sem6 + hours_sem7 + hours_sem8
    
#     # TOTAL RESOURCES SEMESTER WISE===============================
#     total_resources_sem1 = ResourcesQuestion.objects.filter(department = department_id, semester='1st').count() + ResourcesBook.objects.filter(department = department_id, semester='1st').count() + ResourcesLecture.objects.filter(department = department_id, semester='1st').count() + ResourcesNote.objects.filter(department = department_id, semester='1st').count()
    
#     total_resources_sem2 = ResourcesQuestion.objects.filter(department = department_id, semester='2nd').count() + ResourcesBook.objects.filter(department = department_id, semester='2nd').count() + ResourcesLecture.objects.filter(department = department_id, semester='2nd').count() + ResourcesNote.objects.filter(department = department_id, semester='2nd').count()
    
#     total_resources_sem3 = ResourcesQuestion.objects.filter(department = department_id, semester='3rd').count() + ResourcesBook.objects.filter(department = department_id, semester='3rd').count() + ResourcesLecture.objects.filter(department = department_id, semester='3rd').count() + ResourcesNote.objects.filter(department = department_id, semester='3rd').count()
    
#     total_resources_sem4 = ResourcesQuestion.objects.filter(department = department_id, semester='4th').count() + ResourcesBook.objects.filter(department = department_id, semester='4th').count() + ResourcesLecture.objects.filter(department = department_id, semester='4th').count() + ResourcesNote.objects.filter(department = department_id, semester='4th').count()
    
#     total_resources_sem5 = ResourcesQuestion.objects.filter(department = department_id, semester='5th').count() + ResourcesBook.objects.filter(department = department_id, semester='5th').count() + ResourcesLecture.objects.filter(department = department_id, semester='5th').count() + ResourcesNote.objects.filter(department = department_id, semester='5th').count()
    
#     total_resources_sem6 = ResourcesQuestion.objects.filter(department = department_id, semester=6).count() + ResourcesBook.objects.filter(department = department_id, semester=6).count() + ResourcesLecture.objects.filter(department = department_id, semester=6).count() + ResourcesNote.objects.filter(department = department_id, semester=6).count()
    
#     total_resources_sem7 = ResourcesQuestion.objects.filter(department = department_id, semester=7).count() + ResourcesBook.objects.filter(department = department_id, semester=7).count() + ResourcesLecture.objects.filter(department = department_id, semester=7).count() + ResourcesNote.objects.filter(department = department_id, semester=7).count()
    
#     total_resources_sem8 = ResourcesQuestion.objects.filter(department = department_id, semester=8).count() + ResourcesBook.objects.filter(department = department_id, semester=8).count() + ResourcesLecture.objects.filter(department = department_id, semester=8).count() + ResourcesNote.objects.filter(department = department_id, semester=8).count()
    
#     total_resources_all_sem = total_resources_sem1 + total_resources_sem2 + total_resources_sem3 + total_resources_sem4 + total_resources_sem5 + total_resources_sem6 + total_resources_sem7 + total_resources_sem8
    
    
#     # TOTAL RESOURCES COURSE WISE===============================
    
    
#     context = {
#         'total_courses_s': total_courses_s,

#         'courses_sem1': courses_sem1,
#         'courses_sem2': courses_sem2,
#         'courses_sem3': courses_sem3,
#         'courses_sem4': courses_sem4,
#         'courses_sem5': courses_sem5,
#         'courses_sem6': courses_sem6,
#         'courses_sem7': courses_sem7,
#         'courses_sem8': courses_sem8,
        
#         'credits_sem1': credits_sem1,
#         'credits_sem2': credits_sem2,
#         'credits_sem3': credits_sem3,
#         'credits_sem4': credits_sem4,
#         'credits_sem5': credits_sem5,
#         'credits_sem6': credits_sem6,
#         'credits_sem7': credits_sem7,
#         'credits_sem8': credits_sem8,
        
#         'hours_sem1': hours_sem1,
#         'hours_sem2': hours_sem2,
#         'hours_sem3': hours_sem3,
#         'hours_sem4': hours_sem4,
#         'hours_sem5': hours_sem5,
#         'hours_sem6': hours_sem6,
#         'hours_sem7': hours_sem7,
#         'hours_sem8': hours_sem8,
        
#         'total_credits_s': total_credits_s,
#         'total_hours_s': total_hours_s,
        
#         'total_resources_sem1': total_resources_sem1,
#         'total_resources_sem2': total_resources_sem2,
#         'total_resources_sem3': total_resources_sem3,
#         'total_resources_sem4': total_resources_sem4,
#         'total_resources_sem5': total_resources_sem5,
#         'total_resources_sem6': total_resources_sem6,
#         'total_resources_sem7': total_resources_sem7,
#         'total_resources_sem8': total_resources_sem8,
#         'total_resources_all_sem': total_resources_all_sem,
#     }

#     return context