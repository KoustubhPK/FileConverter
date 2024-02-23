from django.contrib import admin
from .models import PdfTextModel, DeletedPdf
from .forms import PdfTextForm

class PdfTextAdmin(admin.ModelAdmin):
    form = PdfTextForm
admin.site.register(PdfTextModel, PdfTextAdmin)
admin.site.register(DeletedPdf)