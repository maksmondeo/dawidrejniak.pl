from django.db import models

class PdfFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class OdbiorcyZestawu(models.Model):
    imie = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)