from django.contrib import admin
from django.urls import path
from portapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.AboutView.as_view()),
    path('education/', views.EducationView.as_view()),
    path('project/',views.ProjectView.as_view()),
    path('skill/',views.SkillView.as_view()),
    path('experience/',views.ExperienceView.as_view()),
    path('certificate/',views.certificateView.as_view()),
    path('services/',views.ServiceView.as_view()),
   # path('contact/',views.ContactView.as_view()),
]