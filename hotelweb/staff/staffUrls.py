from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import staffViews

urlpatterns = [
    # Job titles
    path('job/titles/add/', staffViews.add_job_title, name='add_job_title'),
    path('job/titles/all/', staffViews.all_job_title, name='all_job_titles'),
    path('job/titles/view/<str:job_title_id>', staffViews.job_title_details, name='job_title_details'),
    path('job/titles/update/<str:job_title_id>', staffViews.update_job_title, name='update_job_title'),
    path('job/titles/remove/<str:job_title_id>', staffViews.deactivate_job_title, name='deactivate_job_title'),

    # Job shifts
    path('job/shifts/add/', staffViews.add_job_shift, name='add_job_shift'),
    path('job/shifts/all/', staffViews.all_job_shifts, name='all_job_shifts'),
    path('job/shifts/update/<str:job_shift_id>', staffViews.update_job_shift, name='update_job_shift'),
    path('job/shifts/deactivate/<str:job_shift_id>', staffViews.deactivate_job_shift, name='deactivate_job_shift'),

    # Staff
    path('staff/add/', staffViews.add_staff, name='add_staff'),
    path('staff/current/', staffViews.current_staff, name='current_staff'),
    path('staff/past/', staffViews.past_staff, name='past_staff'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)