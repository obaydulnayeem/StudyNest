from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask, name='ask'),
    path('solve/', views.solve_view, name='solve'),
    path('ask/university/', views.ask_university_view, name='ask_university'),
    path('mentors/', views.mentors_list, name='mentors_list'),
    path('book_session/<slug:slug>/', views.book_session, name='book_session'),
    path('payment/<int:session_id>/', views.payment_view, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('success/', views.success_view, name='success_url'),
]
