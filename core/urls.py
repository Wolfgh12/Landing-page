"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# Added bulk_delete_submissions to the import list
from programs.views import (
    program_list, 
    download_brochure, 
    staff_dashboard, 
    staff_profile, 
    bulk_delete_submissions
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', program_list, name='home'), 
    
    # Custom Login URL
    path('login/', auth_views.LoginView.as_view(template_name='programs/login.html'), name='login'),    
    
    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('download-brochure/', download_brochure, name='download_brochure'),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    
    # NEW: Added the profile path
    path('staff/profile/', staff_profile, name='staff_profile'),

    # BULK DELETE: Added the path to handle multi-row deletion
    path('staff/bulk-delete/', bulk_delete_submissions, name='bulk_delete_submissions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)