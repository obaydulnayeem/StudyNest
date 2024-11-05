from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from utils.permissions import *
from django.contrib import messages

@user_passes_test(is_team_member, login_url='home')
def add_job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.profile = request.user.profile
            job_application.save()
            return redirect('job_application_list')
    else:
        form = JobApplicationForm()
    
    return render(request, 'add_job_application.html', {'form': form})


@user_passes_test(is_team_member, login_url='home')
def edit_job_application(request, job_id):
    job_application = get_object_or_404(JobApplication, id=job_id)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=job_application)
        if form.is_valid():
            form.save()
            return redirect('job_application_list')  # Redirect to a suitable page after saving
    else:
        form = JobApplicationForm(instance=job_application)

    return render(request, 'edit_job_application.html', {'form': form, 'job_application': job_application})


@user_passes_test(is_team_member, login_url='home')
def delete_job_application(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    job.delete()
    messages.success(request, 'The job deleted successfully!')
    return redirect('job_application_list')  # Redirect to job list after deletion


@user_passes_test(is_team_member, login_url='home')
def view_job_details(request, job_id):
    job_application = get_object_or_404(JobApplication, id=job_id)
    return render(request, 'view_job_details.html', {'job_application': job_application})

@user_passes_test(is_team_member, login_url='home')
def job_application_list(request):
    job_applications = JobApplication.objects.filter(profile=request.user.profile).order_by('-date_applied', '-id')
    
    saved_jobs = SavedJobs.objects.filter(profile=request.user.profile, is_applied = False).order_by('deadline')
    
    total_applied_jobs = JobApplication.objects.filter(profile=request.user.profile).count()
    total_in_task_jobs = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).count()
    total_saved_jobs = SavedJobs.objects.filter(profile=request.user.profile).count()
    total_companies = CompanyList.objects.filter(profile=request.user.profile).count()
    total_followees = Followee.objects.filter(profile=request.user.profile).count()
    
    context = {
        'job_applications': job_applications,
        'saved_jobs': saved_jobs,
        'is_job_tracking': True,
        
        'total_applied_jobs': total_applied_jobs,
        'total_in_task_jobs': total_in_task_jobs,
        'total_saved_jobs': total_saved_jobs,
        'total_companies': total_companies,
        'total_followees': total_followees,
    }
    
    return render(request, 'job_application_list.html', context)


@user_passes_test(is_team_member, login_url='home')
def job_list_in_task(request):
    job_applications = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).order_by('-date_applied', '-id')
    
    # saved_jobs = SavedJobs.objects.filter(profile=request.user.profile, is_applied = False).order_by('deadline')
    
    total_applied_jobs = JobApplication.objects.filter(profile=request.user.profile).count()
    total_in_task_jobs = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).count()
    total_saved_jobs = SavedJobs.objects.filter(profile=request.user.profile).count()
    total_companies = CompanyList.objects.filter(profile=request.user.profile).count()
    total_followees = Followee.objects.filter(profile=request.user.profile).count()
    
    context = {
        'job_applications': job_applications,
        # 'saved_jobs': saved_jobs,
        'is_job_tracking': True,
        
        'total_applied_jobs': total_applied_jobs,
        'total_in_task_jobs': total_in_task_jobs,
        'total_saved_jobs': total_saved_jobs,
        'total_companies': total_companies,
        'total_followees': total_followees,
    }
    
    return render(request, 'job_list_in_task.html', context)


@user_passes_test(is_team_member, login_url='home')
def company_list(request):
    companies = CompanyList.objects.filter(profile=request.user.profile).order_by('company_name')
    
    total_applied_jobs = JobApplication.objects.filter(profile=request.user.profile).count()
    total_in_task_jobs = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).count()
    total_saved_jobs = SavedJobs.objects.filter(profile=request.user.profile).count()
    total_companies = CompanyList.objects.filter(profile=request.user.profile).count()
    total_followees = Followee.objects.filter(profile=request.user.profile).count()
    
    context = {
        'companies': companies,
        'is_job_tracking': True,
        
        'total_applied_jobs': total_applied_jobs,
        'total_in_task_jobs': total_in_task_jobs,
        'total_saved_jobs': total_saved_jobs,
        'total_companies': total_companies,
        'total_followees': total_followees,
    }
    
    return render(request, 'company_list.html', context)


@user_passes_test(is_team_member, login_url='home')
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.profile = request.user.profile  # Assuming the user has a related profile
            company.save()
            return redirect('company_list')  # Replace with the URL of the page to redirect after success
    else:
        form = CompanyForm()

    return render(request, 'add_company.html', {'form': form})

@user_passes_test(is_team_member, login_url='home')
def edit_company(request, pk):
    company = get_object_or_404(CompanyList, pk=pk)  # Get the company by ID (primary key)
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Redirect to company list page after saving
    else:
        form = CompanyForm(instance=company)
    
    context = {
        'form': form,
        'company': company
    }
    return render(request, 'edit_company.html', context)

@user_passes_test(is_team_member, login_url='home')
def delete_company(request, pk):
    company = get_object_or_404(CompanyList, pk=pk)
    company.delete()
    messages.success(request, 'Company deleted successfully!')
    return redirect('company_list')  # Redirect to company list after deletion



@user_passes_test(is_team_member, login_url='home')
def followees(request):
    followees_list = Followee.objects.filter(profile=request.user.profile).order_by('name')  # Retrieve all Followee instances
    
    total_applied_jobs = JobApplication.objects.filter(profile=request.user.profile).count()
    total_in_task_jobs = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).count()
    total_saved_jobs = SavedJobs.objects.filter(profile=request.user.profile).count()
    total_companies = CompanyList.objects.filter(profile=request.user.profile).count()
    total_followees = Followee.objects.filter(profile=request.user.profile).count()
    
    context = {
        'is_job_tracking': True,
        'followees': followees_list,
        
        'total_applied_jobs': total_applied_jobs,
        'total_in_task_jobs': total_in_task_jobs,
        'total_saved_jobs': total_saved_jobs,
        'total_companies': total_companies,
        'total_followees': total_followees,
    }
    
    return render(request, 'followees.html', context)

@user_passes_test(is_team_member, login_url='home')
def add_followee(request):
    if request.method == 'POST':
        form = FolloweeForm(request.POST)
        if form.is_valid():
            followee = form.save(commit=False)
            followee.profile = request.user.profile  # Assuming the user has a related profile
            followee.save()
            return redirect('followees')  # Redirect to the followees list after adding
    else:
        form = FolloweeForm()

    return render(request, 'add_followee.html', {'form': form})


def edit_followee(request, followee_id):
    followee = get_object_or_404(Followee, id=followee_id)  # Retrieve the Followee instance or 404

    if request.method == 'POST':
        form = FolloweeForm(request.POST, instance=followee)  # Bind form to the existing instance
        if form.is_valid():
            form.save()  # Save changes to the followee
            return redirect('followees')  # Redirect to followee list
    else:
        form = FolloweeForm(instance=followee)  # Load existing data into the form

    return render(request, 'edit_followee.html', {'form': form, 'followee': followee})

    
@user_passes_test(is_team_member, login_url='home')
def delete_followee(request, pk):
    followee = get_object_or_404(Followee, pk=pk)
    if request.method == "POST":
        followee.delete()
        messages.success(request, "Followee deleted successfully.")
        return redirect('followees')
    else:
        messages.error(request, "Invalid delete request.")
        return redirect('followees')


@user_passes_test(is_team_member, login_url='home')
def save_job(request):
    # Ensure that the user is logged in
    if request.method == 'POST':
        form = SaveJobForm(request.POST)
        if form.is_valid():
            # Create the SavedJob object without saving it yet
            saved_job = form.save(commit=False)
            # Assign the current user's profile to the saved_job instance
            saved_job.profile = request.user.profile
            saved_job.save()
            return redirect('job_application_list')  # Redirect to a page that lists all saved jobs
    else:
        form = SaveJobForm()

    return render(request, 'save_job.html', {'form': form})

@user_passes_test(is_team_member, login_url='home')
def saved_jobs_list(request):
    saved_jobs = SavedJobs.objects.filter(profile=request.user.profile, is_applied=False).order_by('-added_at')  # Show only non-applied jobs

    total_applied_jobs = JobApplication.objects.filter(profile=request.user.profile).count()
    total_in_task_jobs = JobApplication.objects.filter(profile=request.user.profile, is_in_task=True).count()
    total_saved_jobs = SavedJobs.objects.filter(profile=request.user.profile).count()
    total_companies = CompanyList.objects.filter(profile=request.user.profile).count()
    total_followees = Followee.objects.filter(profile=request.user.profile).count()
    
    
    context = {
        'saved_jobs': saved_jobs,
        'is_job_tracking': True,
        
        'total_applied_jobs': total_applied_jobs,
        'total_in_task_jobs': total_in_task_jobs,
        'total_saved_jobs': total_saved_jobs,
        'total_companies': total_companies,
        'total_followees': total_followees,
    }
    return render(request, 'saved_jobs_list.html', context)


@user_passes_test(is_team_member, login_url='home')
def edit_saved_job(request, job_id):
    job = get_object_or_404(SavedJobs, id=job_id, profile=request.user.profile)
    
    if request.method == 'POST':
        form = SaveJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_application_list')  # Replace with the actual view that lists saved jobs
    else:
        form = SaveJobForm(instance=job)
    
    return render(request, 'edit_saved_job.html', {'form': form, 'job': job})

@login_required
def mark_as_applied(request, job_id):
    # Get the saved job by ID and mark it as applied
    saved_job = get_object_or_404(SavedJobs, id=job_id, profile=request.user.profile)
    saved_job.is_applied = True
    saved_job.save()
    return redirect('job_application_list')


# @login_required
# def saved_jobs_list(request):
#     # Fetch the saved jobs for the current user's profile
#     saved_jobs = SavedJobs.objects.filter(profile=request.user.profile)
#     return render(request, 'saved_jobs_list.html', {'saved_jobs': saved_jobs})
