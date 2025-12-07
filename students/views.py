from django.shortcuts import render
from .forms import StudentForm
from .serializers import CustomUserSerializer
from .utils import telegram_send
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from rest_framework.generics import ListAPIView

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            user = CustomUser.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
            )

            message = f'New user registered: {full_name}, {email}, {phone}'
            telegram_send(message)

            send_mail(
                subject='New user created',
                message=f'Welcome {full_name}! You have successfully registered!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            context = {
                'full_name': full_name,
            }
            return render(request, 'success.html', context)

    else:
        form = StudentForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

class StudentList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
