from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# # Create your models here.

class PdfTextModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line to relate the model to the User model
    name = models.CharField(max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    # def content_as_html(self):
    #     return mark_safe(self.content)
    
    def __str__(self):
         return self.name
    
# Create a model to store deleted PDFs
class DeletedPdf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_pdf_id = models.IntegerField()  # Store the ID of the original PdfTextModel
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()  # Automatically set to the current timestamp on creation
    deleted_at = models.DateTimeField(auto_now=True)  # Allow null and blank values for deleted_at

    def __str__(self):
        return self.name