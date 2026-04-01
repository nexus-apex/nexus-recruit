from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('jobpostings/', views.jobposting_list, name='jobposting_list'),
    path('jobpostings/create/', views.jobposting_create, name='jobposting_create'),
    path('jobpostings/<int:pk>/edit/', views.jobposting_edit, name='jobposting_edit'),
    path('jobpostings/<int:pk>/delete/', views.jobposting_delete, name='jobposting_delete'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/create/', views.candidate_create, name='candidate_create'),
    path('candidates/<int:pk>/edit/', views.candidate_edit, name='candidate_edit'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candidate_delete'),
    path('interviews/', views.interview_list, name='interview_list'),
    path('interviews/create/', views.interview_create, name='interview_create'),
    path('interviews/<int:pk>/edit/', views.interview_edit, name='interview_edit'),
    path('interviews/<int:pk>/delete/', views.interview_delete, name='interview_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
