from django.urls import path, include
from apps.core.views.varsity.dependant_dropdown.dependant_dropdown_views import *
from apps.core.views.others_views import search_results



urlpatterns = [
path('search/', search_results, name='search_results'),

path('ajax/load-universities/', load_universities, name='ajax_load_universities'), # AJAX

path('ajax/load-faculties/', load_faculties, name='ajax_load_faculties'), # AJAX

path('ajax/load-departments/', load_departments, name='ajax_load_departments'), # AJAX

path('ajax/load-courses/', load_courses, name='ajax_load_courses'), # AJAX

]