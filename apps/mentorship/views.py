from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from . models import *
from apps.university.models import *
from apps.account.models.profile_models import Profile
from django.contrib.auth.decorators import login_required
from utils.permissions import *
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_batch_or_central_moderator, login_url='home')
def ask(request):
    return render(request, 'ask.html')

# def solve(request):
#     return render(request, 'solve.html')

@user_passes_test(is_batch_or_central_moderator, login_url='home')
def ask_university_view(request):
    if request.method == 'POST':
        form = AskUniversityForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            ask_model_instance = form.save(commit=False)
            ask_model_instance.asked_by = request.user.profile  # Assign the logged-in user
            ask_model_instance.save()
            return redirect('ask')  # Adjust the redirect as needed
    else:
        form = AskUniversityForm()
    return render(request, 'ask_forms/ask_university.html', {'form': form})

@user_passes_test(is_batch_or_central_moderator, login_url='home')
def solve_view(request):
    # asked_questions = AskModel.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)
    courses = profile.courses.all()  # Get the courses associated with the profile
    asked_questions = AskModel.objects.filter(course__in=courses) 
    
    return render(request, 'solve.html', {'asked_questions': asked_questions})

@user_passes_test(is_batch_or_central_moderator, login_url='home')
def mentors_list(request):
    mentors = Profile.objects.filter(user_type='mentor')
    return render(request, 'mentors_list.html', {'mentors': mentors})

@user_passes_test(is_batch_or_central_moderator, login_url='home')
def book_session(request, slug):
    # mentor = get_object_or_404(Profile, slug=slug)
    mentor = Profile.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = SessionDetailsForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.asked_by = mentor
            session.save()
            # Redirect to the payment page with session id
            return redirect('payment', session_id=session.id)
    else:
        form = SessionDetailsForm()

    context = {
        'mentor': mentor,
        'form': form,
    }
    return render(request, 'book_session.html', context)


@user_passes_test(is_batch_or_central_moderator, login_url='home')
def payment_view(request, session_id):
    session = get_object_or_404(SessionDetails, id=session_id)

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.user = request.user.profile
            payment.save()
            return redirect('payment_success')
    else:
        payment_form = PaymentForm()

    context = {
        'session': session,
        'payment_form': payment_form,
    }
    return render(request, 'payment.html', context)


@user_passes_test(is_batch_or_central_moderator, login_url='home')
def payment_success(request):
    return render(request, 'payment_success.html')


@user_passes_test(is_batch_or_central_moderator, login_url='home')
def success_view(request):
    return render(request, 'success.html')
