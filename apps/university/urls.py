from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from utils.permissions import *

urlpatterns = [
    # path('their_course/', views.their_course, name='their_course'),

    # path('university/<int:university_id>/', views.university_detail, name='university_detail'),

    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),

    path('university_list/', views.university_list, name='university_list'),

    
    path('university_info/<int:university_id>/', views.university_info, name='university_info'),
    
    
    path('my_department_s/<int:university_id>/<int:department_id>/', views.my_department_s, name='my_department_s'),
    
    path('show_all_universities/', views.show_all_universities, name='show_all_universities'),
    
    path('show_university/<int:university_id>/', views.show_university, name='show_university'),
    
    path('show_faculty/<int:faculty_id>/', views.show_faculty, name='show_faculty'),
    
    path('show_institute/<int:institute_id>/', views.show_institute, name='show_institute'),
    
    path('show_school/<int:school_id>/', views.show_school, name='show_school'),
    
    path('show_center/<int:center_id>/', views.show_center, name='show_center'),
    
    
    path('show_department/<int:department_id>/', views.show_department, name='show_department'),
    
    path('show_discipline/<int:discipline_id>/', views.show_discipline, name='show_discipline'),
    
    path('show_course/<int:course_id>/', views.show_course, name='show_course'),
    
    # path('layer2/', views.layer2, name='layer2'),
    
    # path('layer3/', views.layer3, name='layer3'),
    
    # path('layer4/', views.layer4, name='layer4'),
    
    # path('layer5/', views.layer5, name='layer5'),
    
    # path('layer6/', views.layer6, name='layer6'),
    
    path('update_department_order/', views.update_department_order, name='update_department_order'),
    
    # path('scrape/', views.scrape_data, name='scrape_data'),
    
    # path('pin_year_and_semester/<int:year>/<int:semester>/', views.pin_year_and_semester, name='pin_year_and_semester'),

    path('view_course/<int:course_id>/', views.view_course, name='view_course'),
    
    path('my_resources_s/<int:x_id>/<int:semester>/', views.my_resources_s, name='my_resources_s'),


    # QUESTIONS---------------------------------
    path('add_question/', views.add_question, name='add_question'),
    
    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),

    path('questions/edit/<int:question_id>/', views.edit_question, name='edit_question'),
    
    path('questions/delete/<int:question_id>/', views.delete_question, name='delete_question'),
    

    # BOOKS-------------------------------------
    path('add_book/', views.add_book, name='add_book'),
    
    path('view_books/<int:course_id>/', views.view_books, name='view_books'),
    
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    
    
     # NOTES-------------------------------------
    path('add_note/', views.add_note, name='add_note'),
    
    path('view_notes/<int:course_id>/', views.view_notes, name='view_notes'),
    
    path('notes/edit/<int:note_id>/', views.edit_note, name='edit_note'),
    
    path('notes/delete/<int:note_id>/', views.delete_note, name='delete_note'),
    


    # LECTURE SLIDES -------------------------------------
    path('add_lecture/', views.add_lecture, name='add_lecture'),
    
    path('view_lectures/<int:course_id>/', views.view_lectures, name='view_lectures'),
    
    path('lectures/edit/<int:lecture_id>/', views.edit_lecture, name='edit_lecture'),
    
    path('lectures/delete/<int:lecture_id>/', views.delete_lecture, name='delete_lecture'),


    # FEEDBACKS ============================================
    path('submit-feedback/<int:question_id>/', views.submit_feedback, name='submit_feedback'),
   
    path('success-feedback/', views.success_feedback, name='success_feedback'),
    
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    
    
    # path('handle_love_click/<int:question_id>/', views.handle_love_click, name='handle_love_click'),
    
    # path('update_love_count/', views.increment_love_count, name='increment_love_count'),
    
    path('share/<int:question_id>/', views.share_question, name='share_question'),

    # path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX

    # path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX

    # path('ajax/load-teachers/', views.load_teachers, name='ajax_load_teachers'), # AJAX
    
    # path('department_list/', views.nothing, name='nothing'),

    # path('moderators/', views.moderators, name='moderators'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),


    # SERVE PROTECTED FILES ===============================================
    path('protected_question/<int:resource_id>/', serve_protected_question, name='serve_protected_question'),
    
    path('protected_book/<int:resource_id>/', serve_protected_book, name='serve_protected_book'),
    
    path('protected_note/<int:resource_id>/', serve_protected_note, name='serve_protected_note'),
    
    path('protected_lecture/<int:resource_id>/', serve_protected_lecture, name='serve_protected_lecture'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
