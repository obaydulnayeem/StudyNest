from django.urls import path, include
from .views.my_profile_views import *
from .views.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

# OVERVIEW 
    path('my_profile_overview/', my_profile_overview, name='my_profile_overview'),
    
    path('view_profile_overview/<int:user_id>/', view_profile_overview, name='view_profile_overview'),
    
# PERSONAL INFO
    path('personal_info_my_profile/', personal_info_my_profile, name='personal_info_my_profile'),
    
    path('personal_info_view_profile/<int:user_id>/', personal_info_view_profile, name='personal_info_view_profile'),
    
    path('edit_personal_info_my_profile/', edit_personal_info_my_profile, name='edit_personal_info_my_profile'),
    
    
# EDUCATIONAL QUALIFICATIONS
    # path('add_edu_university_my_profile/', add_edu_university_my_profile, name='add_edu_university_my_profile'),
    
    path('add_edu_university_step1/', add_edu_university_step1, name='add_edu_university_step1'),
    
    path('add_edu_university_step2/<int:university_id>/', add_edu_university_step2, name='add_edu_university_step2'),
    
    path('add_edu_university_step3/', add_edu_university_step3, name='add_edu_university_step3'),
    
    path('edit_basic_personal_info/', edit_basic_personal_info, name='edit_basic_personal_info'),
    
    path('view_edu_university_my_profile/', view_edu_university_my_profile, name='view_edu_university_my_profile'),
    
    path('view_edu_university_view_profile/<int:user_id>/', view_edu_university_view_profile, name='view_edu_university_view_profile'),
    
    path('edit_edu_university_my_profile/<int:pk>/', edit_edu_university_my_profile, name='edit_edu_university_my_profile'),

# MY PROFILE: CONTRIBUTION SUMMARY
    path('contribution_summary/', contribution_summary, name='contribution_summary'),
    
    path('contribution_summary_view_profile/<int:user_id>/', contribution_summary_view_profile, name='contribution_summary_view_profile'),
    
# MY PROFILE: DETAILED CONTRIBUTION
    path('detailed_contribution/', detailed_contribution, name='detailed_contribution'),
    
    path('detailed_contribution_view_profile/<int:user_id>/', detailed_contribution_view_profile, name='detailed_contribution_view_profile'),



    path('coin_details/', coin_details, name='coin_details'),
# DISPLAY PROFILE: OVERVIEW
    # path('display_profile/<int:user_id>/', display_profile, name='display_profile'),
    
    
    
    # path('edit_edu_school/<int:pk>/', edit_edu_school, name='edit_edu_school'),
    
    # path('skills_university_courses/', skills_university_courses, name='skills_university_courses'),
    
    # path('address/', address, name='address'),
    
    # path('edit_skills/', edit_skills, name='edit_skills'),
    
    # path('contributions/', contributions, name='contributions'),
    
    
    
    # path('add-coin-transaction/', views.add_coin_transaction, name='add_coin_transaction'),
    
    # path('my_profile/', include('apps.account.urls.my_profile_urls')),
    
    # path('my_profile_d/', my_profile_d, name='my_profile_d'),
    
    # path('my_profile_d/<int:pk>/', my_profile_d, name='edit_edu_university'),
    
    
    
    
    
    path('login/', user_login, name='login'),
    
    path('logout/', user_logout, name='logout'),   
    
    path('social-auth/', include('social_django.urls', namespace='social')), # for google auth
    
    
    # path('personal_info/', views.personal_info, name='personal_info'),
    # path('address/', views.address, name='address'),
    # path('skills/', views.skills, name='skills'),
    
# REFERRAL
    path('generate_referral_link/', generate_referral_link, name='generate_referral_link'),
    
    path('handle_referral/', handle_referral, name='handle_referral'),
    
    path('check_referral/', check_referral, name='check_referral'),
]
