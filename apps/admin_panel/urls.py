# admin_panel/urls.py
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('moderator_base/', moderator_base, name='moderator_base'),
    
    
#BATCH MODERATOR URLS ---------------------------------------
    path('need_verification/', need_verification, name='need_verification'),

    path('sent_verification_req/', sent_verification_req, name='sent_verification_req'),

    path('sent_verification_req/', sent_verification_req, name = 'sent_verification_req'),
    
    path('batch_wise_users/', batch_wise_users, name='batch_wise_users'),

    path('pending_for_verify_users/', pending_for_verify_users, name='pending_for_verify_users'),

    path('make_verified_user/<int:user_id>/', make_verified_user, name='make_verified_user'),

    path('make_not_verified_user/<int:user_id>/', make_not_verified_user, name='make_not_verified_user'),

    path('pending_user_list/', pending_user_list, name='pending_user_list'),
    
    path('approve_profile/<int:profile_id>/', approve_profile, name='approve_profile'),
    
    path('reject_profile/<int:profile_id>/', reject_profile, name='reject_profile'),


#DEPARTMENTAL MODERATOR URLS ---------------------------------------
    path('department_info_moderator/<int:department_id>', department_info_moderator, name='department_info_moderator'),
    
    path('edit_department_info_moderator/<int:department_id>', edit_department_info_moderator, name='edit_department_info_moderator'),
    
    path('edit_syllabus/<int:department_id>/', edit_syllabus, name='edit_syllabus'),
    # path('course_settings/<int:department_id>', course_settings, name='course_settings'),
    
    
    path('course_details/', course_details, name='course_details'),
    
    path('view_courses_s/<int:university_id>/<int:department_id>/<int:semester_id>/', view_courses_s, name='view_courses_s'),
    
    path('add_course/', add_course, name='add_course'),
    
    path('edit_course/<int:course_id>/', edit_course, name='edit_course'),
    
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    
    path('approved_moderator_list/', approved_moderator_list, name='approved_moderator_list'),

#UNIVERSITY MODERATOR URLS ---------------------------------------
    path('add_base_university_mod/', add_base_university_mod, name='add_base_university_mod'),
    
    path('show_base_university_mod/', show_base_university_mod, name='show_base_university_mod'),
    
    path('show_faculties_mod/<int:university_id>/', show_faculties_mod, name='show_faculties_mod'),
    
    path('show_schools_mod/<int:university_id>/', show_schools_mod, name='show_schools_mod'),
    
    path('show_centers_mod/<int:university_id>/', show_centers_mod, name='show_centers_mod'),
    
    path('show_departments_mod/<int:university_id>/', show_departments_mod, name='show_departments_mod'),
    
    path('show_disciplines_mod/<int:university_id>/', show_disciplines_mod, name='show_disciplines_mod'),
    
    path('edit_faculty_mod/<int:university_id>/<int:faculty_id>/', edit_faculty_mod, name='edit_faculty_mod'),
    
    path('edit_institute_mod/<int:university_id>/<int:institute_id>/', edit_institute_mod, name='edit_institute_mod'),
    
    path('edit_school_mod/<int:school_id>/', edit_school_mod, name='edit_school_mod'),
    
    path('edit_center_mod/<int:center_id>/', edit_center_mod, name='edit_center_mod'),
    
    path('edit_department_mod/<int:department_id>/', edit_department_mod, name='edit_department_mod'),
    
    path('edit_discipline_mod/<int:discipline_id>/', edit_discipline_mod, name='edit_discipline_mod'),
    
    path('show_institutes_mod/<int:university_id>/', show_institutes_mod, name='show_institutes_mod'),
    
    path('add_institute_mod/<int:university_id>/', add_institute_mod, name='add_institute_mod'),
    
    path('add_school_mod/<int:university_id>/', add_school_mod, name='add_school_mod'),
    
    path('add_center_mod/<int:university_id>/', add_center_mod, name='add_center_mod'),
    
    path('add_faculty_mod/<int:university_id>/', add_faculty_mod, name='add_faculty_mod'),
    
    path('show_departments_by_faculty_mod/<int:faculty_id>/', show_departments_by_faculty_mod, name='show_departments_by_faculty_mod'),
    
    path('show_institutes_by_faculty_mod/<int:faculty_id>/', show_institutes_by_faculty_mod, name='show_institutes_by_faculty_mod'),
    
    path('show_departments_by_institute_mod/<int:institute_id>/', show_departments_by_institute_mod, name='show_departments_by_institute_mod'),
    
    path('add_department_by_faculty_mod/<int:faculty_id>/', add_department_by_faculty_mod, name='add_department_by_faculty_mod'),
    
    path('add_institute_by_faculty_mod/<int:faculty_id>/', add_institute_by_faculty_mod, name='add_institute_by_faculty_mod'),
    
    path('edit_department_by_faculty_mod/<int:faculty_id>/<int:department_id>/', edit_department_by_faculty_mod, name='edit_department_by_faculty_mod'),
    
    path('edit_institute_by_faculty_mod/<int:faculty_id>/<int:institute_id>/', edit_institute_by_faculty_mod, name='edit_institute_by_faculty_mod'),
    
    path('department_list/<int:university_id>/', department_list, name='department_list'),

    # path('university/<int:university_id>/add-department/', add_department, name='add_department'),
    
    path('add_department_mod/<int:university_id>/', add_department_mod, name='add_department_mod'),
    
    path('add_discipline_mod/<int:university_id>/', add_discipline_mod, name='add_discipline_mod'),
    
    path('edit_department/<int:department_id>/', edit_department, name='edit_department'),
    
    path('delete_department/<int:department_id>/', delete_department, name='delete_department'),
    
    path('delete_institute/<int:institute_id>/', delete_institute, name='delete_institute'),
    
    path('delete_school_mod/<int:school_id>/', delete_school_mod, name='delete_school_mod'),
    
    path('delete_center_mod/<int:center_id>/', delete_center_mod, name='delete_center_mod'),
    
    path('delete_department_mod/<int:department_id>/', delete_department_mod, name='delete_department_mod'),
    
    path('delete_discipline_mod/<int:discipline_id>/', delete_discipline_mod, name='delete_discipline_mod'),
    
    path('delete_faculty/<int:faculty_id>/', delete_faculty, name='delete_faculty'),
    
    path('settings_university_mod/<int:university_id>/', settings_university_mod, name='settings_university_mod'),
    
    path('edit_university_mod/<int:university_id>/', edit_university_mod, name='edit_university_mod'),

    path('others_central_mod/', others_central_mod, name='others_central_mod'),

    path('requested_for_prev_coins/', requested_for_prev_coins, name='requested_for_prev_coins'),

    path('given_prev_coin/<int:profile_id>/', given_prev_coin, name='given_prev_coin'),

    path('notification_base_mod/', notification_base_mod, name='notification_base_mod'),
    
    path('quick_buttons_mod/', quick_buttons_mod, name='quick_buttons_mod'),

# MODERATOR REQUESTS-----------------------
    path('request_for_moderator/', request_for_moderator, name='request_for_moderator'),
    
    path('retire_from_moderator/', retire_from_moderator, name='retire_from_moderator'),
    
    path('delete_prev_moderator_req/', delete_prev_moderator_req, name='delete_prev_moderator_req'),
    
    path('moderator_request_sent/', moderator_request_sent, name='moderator_request_sent'),
    
    path('moderator_request_list_initial/', moderator_request_list_initial, name='moderator_request_list_initial'),
    
    path('moderator_request_list_final/', moderator_request_list_final, name='moderator_request_list_final'),
    
    path('approve_moderator_initial/<int:request_id>/', approve_moderator_initial, name='approve_moderator_initial'),
    
    path('reject_moderator_initial/<int:request_id>/', reject_moderator_initial, name='reject_moderator_initial'),
    
    path('approve_moderator_final/<int:request_id>/', approve_moderator_final, name='approve_moderator_final'),



    # path('approved_moderator_list', approved_moderator_list, name='approved_moderator_list'),
    # path('university_info/', university_info, name='university_info'),
    
    # path('moderator_department_info/', moderator_department_info, name='department_info'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)