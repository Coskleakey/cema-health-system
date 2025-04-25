from django.shortcuts import render
from .models import Client
from django.shortcuts import redirect
from .forms import ClientForm
from .forms import EnrollmentForm
from .models import Enrollment
from django.shortcuts import get_object_or_404
from .forms import ClientSearchForm
from programs.models import Program

# Create your views here.
def client_list(request):
    form = ClientSearchForm(request.GET)
    clients = Client.objects.all()

    if form.is_valid():
        # Handle search by name
        query = form.cleaned_data.get('query')
        if query:
            clients = clients.filter(full_name__icontains=query)

        # Handle filters for age
        min_age = form.cleaned_data.get('min_age')
        max_age = form.cleaned_data.get('max_age')
        if min_age:
            clients = clients.filter(age__gte=min_age)
        if max_age:
            clients = clients.filter(age__lte=max_age)

        # Handle gender filter
        gender = form.cleaned_data.get('gender')
        if gender:
            clients = clients.filter(gender=gender)

        # Handle program filter
        program = form.cleaned_data.get('program')
        if program:
            clients = clients.filter(enrollments__program=program)

    return render(request, 'clients/client_list.html', {'form': form, 'clients': clients})

def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-list')
    else:
        form = ClientForm()
    return render(request, 'clients/register_client.html', {'form': form})

def enroll_client(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            programs = form.cleaned_data['programs']
            for program in programs:
                Enrollment.objects.create(client=client, program=program)
            return redirect('client-list')
    else:
        form = EnrollmentForm()
    return render(request, 'clients/enroll_client.html', {'form': form})

def client_profile(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    enrollments = client.enrollments.all()
    return render(request, 'clients/client_profile.html', {'client': client, 'enrollments': enrollments})
