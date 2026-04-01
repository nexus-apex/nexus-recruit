from django.contrib import admin
from .models import JobPosting, Candidate, Interview

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ["title", "department", "location", "job_type", "salary_range", "created_at"]
    list_filter = ["job_type", "status"]
    search_fields = ["title", "department", "location"]

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "current_company", "experience_years", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "email", "phone"]

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ["candidate_name", "job_title", "interviewer", "date", "mode", "created_at"]
    list_filter = ["mode", "status"]
    search_fields = ["candidate_name", "job_title", "interviewer"]
