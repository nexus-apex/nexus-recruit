from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import JobPosting, Candidate, Interview
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusRecruit with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusrecruit.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if JobPosting.objects.count() == 0:
            for i in range(10):
                JobPosting.objects.create(
                    title=f"Sample JobPosting {i+1}",
                    department=f"Sample {i+1}",
                    location=f"Sample {i+1}",
                    job_type=random.choice(["full_time", "part_time", "contract", "internship"]),
                    salary_range=f"Sample {i+1}",
                    status=random.choice(["open", "closed", "on_hold"]),
                    applications=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 JobPosting records created'))

        if Candidate.objects.count() == 0:
            for i in range(10):
                Candidate.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    current_company=["TechVision Pvt Ltd","Global Solutions","Pinnacle Systems","Nova Enterprises","CloudNine Solutions","MetaForge Inc","DataPulse Analytics","QuantumLeap Tech","SkyBridge Corp","Zenith Innovations"][i],
                    experience_years=random.randint(1, 100),
                    status=random.choice(["new", "screening", "interview", "offer", "hired", "rejected"]),
                    resume_url=f"https://example.com/{i+1}",
                    notes=f"Sample notes for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Candidate records created'))

        if Interview.objects.count() == 0:
            for i in range(10):
                Interview.objects.create(
                    candidate_name=f"Sample Interview {i+1}",
                    job_title=f"Sample Interview {i+1}",
                    interviewer=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    mode=random.choice(["in_person", "video", "phone"]),
                    status=random.choice(["scheduled", "completed", "cancelled"]),
                    rating=random.randint(1, 100),
                    feedback=f"Sample feedback for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Interview records created'))
