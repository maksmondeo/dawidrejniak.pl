from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import *
from django.conf import settings
from .models import *

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            email_message = f'Wiadomość od: {name}\nEmail: {email}\Telefon: {phone}\n\n{message}'
            
            send_mail(
                f'[FORMULARZ] {name}',
                email_message,
                settings.EMAIL_HOST_USER,
                ['your-email@address.com'],
                fail_silently=False,
            )

            success_message = "Wiadomość została przesłana"
            return render(request, 'index.html', {'form': form, 'success_message': success_message})
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})


def opinie(request):
    return render(request, 'opinie.html')

def polityka_prywatnosci(request):
    return render(request, 'polityka_prywatnosci.html')

def odbierz(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            email_to = form.cleaned_data['email'] 
            sender_name = form.cleaned_data['name']
            pdf = PdfFile.objects.last()

            if not pdf:
                return HttpResponse("Brak dostępnych plików PDF.", status=400)

            OdbiorcyZestawu.objects.create(imie=sender_name, email=email_to)            

            email = EmailMessage(
                subject=f"💪 Cześć {sender_name}, Przesyłam Ci Darmowy Zestaw Ćwiczeń",
                body="""
                    <html>
                    <style>a:hover { cursor: pointer; }</style>
                    <body>
                        <p style="font-size: 20px; color: black;">Cześć!</p>
                        <p style="font-size: 16px; color: black;">Przesyłam darmowe zestawy ćwiczeń.<br>
                            Jeśli masz jakieś pytania, jestem dostępny pod tym mailem lub ig: <strong><a style="text-decoration: none; color: black;" href="https://www.instagram.com/dawid_rejniak">@dawid_rejniak</strong></p>
                        <p style="font-size: 16px; color: black;">Baw się dobrze 😊</p>
                    </body>
                    </html>
                    """,
                from_email="your-email@address.com",
                to=[email_to]
            )
            email.content_subtype = "html"
            email.attach_file(pdf.file.path)
            try:
                email.send()
                success_message = "Sprawdź skrzynkę pocztową 💪"
                return render(request, 'odbierz.html', {'form': form, 'success_message': success_message})
            except Exception as e:
                success_message = "Coś poszło nie tak..."
                return render(request, 'odbierz.html', {'form': form, 'success_message': success_message})
    form = SendMailForm()
    return render(request, 'odbierz.html', {'form': form})