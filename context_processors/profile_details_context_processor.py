from django.contrib.auth.models import User
from apps.account.models import Profile, EduUniversity

def profile_details_context_processor(request):
    profile = None
    profile_semester = None
    profile_edu_university = None
    
    ctxp_profile_edu_university_name = None
    ctxp_profile_edu_institute_name = None
    ctxp_profile_edu_department_name = None
    ctxp_profile_edu_discipline_name = None
    
    ctxp_profile_edu_university_id = None
    ctxp_profile_edu_institute_id = None
    ctxp_profile_edu_department_id = None
    ctxp_profile_edu_discipline_id = None

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            
            # Ensure we correctly retrieve the EduUniversity object
            profile_edu_university = EduUniversity.objects.get(profile=profile)
            
            # Safely get the university and department names if they exist
            ctxp_profile_edu_university_name = (
                profile_edu_university.university.name
                if profile_edu_university.university else None
            )
            
            ctxp_profile_edu_institute_name = (
                profile_edu_university.institute.name
                if profile_edu_university.institute else None
            )
            
            ctxp_profile_edu_department_name = (
                profile_edu_university.department.name 
                if profile_edu_university.department else None
            )
            
            ctxp_profile_edu_discipline_name = (
                profile_edu_university.discipline.name 
                if profile_edu_university.discipline else None
            )
            
            # Retrieve university ID and department ID if they exist
            ctxp_profile_edu_university_id = (
                profile_edu_university.university.id
                if profile_edu_university.university else None
            )
            
            ctxp_profile_edu_institute_id = (
                profile_edu_university.institute.id
                if profile_edu_university.institute else None
            )
            
            ctxp_profile_edu_department_id = (
                profile_edu_university.department.id 
                if profile_edu_university.department else None
            )
            
            ctxp_profile_edu_discipline_id = (
                profile_edu_university.discipline.id
                if profile_edu_university.discipline else None
            )
            
            profile_semester = profile_edu_university.semester if profile_edu_university else None

        except Profile.DoesNotExist:
            # If the profile does not exist, these remain None
            profile = None

        except EduUniversity.DoesNotExist:
            # If the EduUniversity does not exist, these remain None
            profile_edu_university = None

    return {
        'profile': profile,
        'profile_semester': profile_semester,
        'ctxp_profile_edu_university': profile_edu_university,
        
        'ctxp_profile_edu_university_name': ctxp_profile_edu_university_name,
        'ctxp_profile_edu_institute_name': ctxp_profile_edu_institute_name,
        'ctxp_profile_edu_department_name': ctxp_profile_edu_department_name,
        'ctxp_profile_edu_discipline_name': ctxp_profile_edu_discipline_name,
        
        'ctxp_profile_edu_university_id': ctxp_profile_edu_university_id,
        'ctxp_profile_edu_institute_id': ctxp_profile_edu_institute_id,
        'ctxp_profile_edu_department_id': ctxp_profile_edu_department_id,
        'ctxp_profile_edu_discipline_id': ctxp_profile_edu_discipline_id,
    }
