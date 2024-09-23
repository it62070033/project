from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from user.forms import RegistrationForm

# Create your views here.
def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            user= authenticate(email=email,password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            context['register_form']=form
    else:
        form=RegistrationForm()
        context['register_form']=form
    return render(request,'user/register.html',context)
