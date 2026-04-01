from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, default="")
    location = models.CharField(max_length=255, blank=True, default="")
    job_type = models.CharField(max_length=50, choices=[("full_time", "Full Time"), ("part_time", "Part Time"), ("contract", "Contract"), ("internship", "Internship")], default="full_time")
    salary_range = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("open", "Open"), ("closed", "Closed"), ("on_hold", "On Hold")], default="open")
    applications = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    current_company = models.CharField(max_length=255, blank=True, default="")
    experience_years = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("new", "New"), ("screening", "Screening"), ("interview", "Interview"), ("offer", "Offer"), ("hired", "Hired"), ("rejected", "Rejected")], default="new")
    resume_url = models.URLField(blank=True, default="")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Interview(models.Model):
    candidate_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255, blank=True, default="")
    interviewer = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    mode = models.CharField(max_length=50, choices=[("in_person", "In Person"), ("video", "Video"), ("phone", "Phone")], default="in_person")
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="scheduled")
    rating = models.IntegerField(default=0)
    feedback = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.candidate_name
