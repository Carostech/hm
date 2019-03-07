from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import facilityViews

urlpatterns = [
    # Facility types
    path('facility/types/add/', facilityViews.add_facility_type, name='add_facility_type'),
    path('facility/types/all/', facilityViews.all_facility_types, name='all_facility_types'),
    path('facility/types/update/<str:facility_type_id>/', facilityViews.update_facility_type, name='update_facility_type'),
    path('facility/types/deactivate/<str:facility_type_id>/', facilityViews.deactivate_facility_type, name='deactivate_facility_type'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)