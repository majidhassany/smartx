from django.shortcuts import render
from register.models import Device
from django.views.generic import TemplateView,ListView,DetailView
from django.utils import timezone
from register import forms
# Create your views here.


class DeviceListView(ListView):
    context_object_name = 'devices'
    model = Device
    template_name = 'register/device_list.html'

class DeviceDetailView(DetailView):
    context_object_name = 'device_detail'
    model = Device
    template_name = 'register/device_detail.html'

def index(request):
    return render(request,'register/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES.get('profile_pics')

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'register/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})



def form_device_view(request):
    form = forms.FormModelName()
    if request.method == 'POST':
        form = forms.FormModelName(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR')

    return render(request,'register/form_device.html',{'form': form})

def form_master_view(request):
    form1 = forms.FormModelMaster()
    if request.method == 'POST':
        form1 = forms.FormModelMaster(request.POST)

        if form.is_valid:
            form1.save(commit=True)
            return index(request)
        else:
            print('ERROR')

    return render(request,'register/form_master.html',{'form1': form1})
