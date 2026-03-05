import os
from django.conf import settings
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render, redirect 
from .models import Program, BrochureSubmission 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def program_list(request):
    all_programs = Program.objects.all().order_by('position') 
    context = {
        'programs': all_programs,
        'program_count': all_programs.count() 
    }
    return render(request, 'programs/index.html', context)

def download_brochure(request):
    # 1. Handle the Form Submission (POST)
    if request.method == "POST":
        full_name = request.POST.get('fullName') or request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobileNumber') or request.POST.get('mobile_number')
        qual = request.POST.get('qualification')
        prog = request.POST.get('program')

        if full_name and email:
            BrochureSubmission.objects.create(
                full_name=full_name,
                email=email,
                mobile_number=mobile,
                qualification=qual,
                program_name=prog
            )
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": "Missing data"}, status=400)

    # 2. Handle the Actual File Download (GET)
    # Corrected the filename to match your uploaded file: Main-Brochure-UGC (12)_compressed.pdf
    file_path = os.path.join(settings.BASE_DIR, 'static', 'Main-Brochure-UGC (12)_compressed.pdf')
    
    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, 'rb'), 
            as_attachment=True, 
            filename='Main-Brochure-UGC.pdf' # This is what the user sees as the saved name
        )
    
    raise Http404("Brochure file not found on server")

@login_required 
def staff_dashboard(request):
    if not request.user.is_staff:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
        
    submissions = BrochureSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'programs/dashboard.html', {'submissions': submissions})

@login_required
@require_POST
def bulk_delete_submissions(request):
    if not request.user.is_staff:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
        
    submission_ids = request.POST.getlist('submission_ids')
    if submission_ids:
        BrochureSubmission.objects.filter(id__in=submission_ids).delete()
    
    return redirect('staff_dashboard')

@login_required
def staff_profile(request):
    return render(request, 'programs/profile.html')