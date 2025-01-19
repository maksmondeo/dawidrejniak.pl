from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

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
                ['dawidrejniak3@gmail.com'],
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