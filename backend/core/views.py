import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import JobPosting, Candidate, Interview


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['jobposting_count'] = JobPosting.objects.count()
    ctx['jobposting_full_time'] = JobPosting.objects.filter(job_type='full_time').count()
    ctx['jobposting_part_time'] = JobPosting.objects.filter(job_type='part_time').count()
    ctx['jobposting_contract'] = JobPosting.objects.filter(job_type='contract').count()
    ctx['candidate_count'] = Candidate.objects.count()
    ctx['candidate_new'] = Candidate.objects.filter(status='new').count()
    ctx['candidate_screening'] = Candidate.objects.filter(status='screening').count()
    ctx['candidate_interview'] = Candidate.objects.filter(status='interview').count()
    ctx['interview_count'] = Interview.objects.count()
    ctx['interview_in_person'] = Interview.objects.filter(mode='in_person').count()
    ctx['interview_video'] = Interview.objects.filter(mode='video').count()
    ctx['interview_phone'] = Interview.objects.filter(mode='phone').count()
    ctx['recent'] = JobPosting.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def jobposting_list(request):
    qs = JobPosting.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(job_type=status_filter)
    return render(request, 'jobposting_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def jobposting_create(request):
    if request.method == 'POST':
        obj = JobPosting()
        obj.title = request.POST.get('title', '')
        obj.department = request.POST.get('department', '')
        obj.location = request.POST.get('location', '')
        obj.job_type = request.POST.get('job_type', '')
        obj.salary_range = request.POST.get('salary_range', '')
        obj.status = request.POST.get('status', '')
        obj.applications = request.POST.get('applications') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/jobpostings/')
    return render(request, 'jobposting_form.html', {'editing': False})


@login_required
def jobposting_edit(request, pk):
    obj = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.department = request.POST.get('department', '')
        obj.location = request.POST.get('location', '')
        obj.job_type = request.POST.get('job_type', '')
        obj.salary_range = request.POST.get('salary_range', '')
        obj.status = request.POST.get('status', '')
        obj.applications = request.POST.get('applications') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/jobpostings/')
    return render(request, 'jobposting_form.html', {'record': obj, 'editing': True})


@login_required
def jobposting_delete(request, pk):
    obj = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/jobpostings/')


@login_required
def candidate_list(request):
    qs = Candidate.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'candidate_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def candidate_create(request):
    if request.method == 'POST':
        obj = Candidate()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.current_company = request.POST.get('current_company', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.status = request.POST.get('status', '')
        obj.resume_url = request.POST.get('resume_url', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/candidates/')
    return render(request, 'candidate_form.html', {'editing': False})


@login_required
def candidate_edit(request, pk):
    obj = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.current_company = request.POST.get('current_company', '')
        obj.experience_years = request.POST.get('experience_years') or 0
        obj.status = request.POST.get('status', '')
        obj.resume_url = request.POST.get('resume_url', '')
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/candidates/')
    return render(request, 'candidate_form.html', {'record': obj, 'editing': True})


@login_required
def candidate_delete(request, pk):
    obj = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/candidates/')


@login_required
def interview_list(request):
    qs = Interview.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(candidate_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(mode=status_filter)
    return render(request, 'interview_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def interview_create(request):
    if request.method == 'POST':
        obj = Interview()
        obj.candidate_name = request.POST.get('candidate_name', '')
        obj.job_title = request.POST.get('job_title', '')
        obj.interviewer = request.POST.get('interviewer', '')
        obj.date = request.POST.get('date') or None
        obj.mode = request.POST.get('mode', '')
        obj.status = request.POST.get('status', '')
        obj.rating = request.POST.get('rating') or 0
        obj.feedback = request.POST.get('feedback', '')
        obj.save()
        return redirect('/interviews/')
    return render(request, 'interview_form.html', {'editing': False})


@login_required
def interview_edit(request, pk):
    obj = get_object_or_404(Interview, pk=pk)
    if request.method == 'POST':
        obj.candidate_name = request.POST.get('candidate_name', '')
        obj.job_title = request.POST.get('job_title', '')
        obj.interviewer = request.POST.get('interviewer', '')
        obj.date = request.POST.get('date') or None
        obj.mode = request.POST.get('mode', '')
        obj.status = request.POST.get('status', '')
        obj.rating = request.POST.get('rating') or 0
        obj.feedback = request.POST.get('feedback', '')
        obj.save()
        return redirect('/interviews/')
    return render(request, 'interview_form.html', {'record': obj, 'editing': True})


@login_required
def interview_delete(request, pk):
    obj = get_object_or_404(Interview, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/interviews/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['jobposting_count'] = JobPosting.objects.count()
    data['candidate_count'] = Candidate.objects.count()
    data['interview_count'] = Interview.objects.count()
    return JsonResponse(data)
