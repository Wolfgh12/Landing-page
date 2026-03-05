from django.db import models

class Program(models.Model):
    program_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='programs/') 
    apply_url = models.URLField()
    position = models.PositiveIntegerField(default=0, help_text="Lower numbers (e.g., 1) appear first")

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"
        ordering = ['position', 'id']

    def __str__(self):
        return self.title

class BrochureSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    # Increased max_length slightly to prevent overflow errors
    program_name = models.CharField(max_length=500) 
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Brochure Submission"
        verbose_name_plural = "Brochure Submissions"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.full_name} - {self.program_name}"