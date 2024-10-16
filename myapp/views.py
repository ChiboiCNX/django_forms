
from django.shortcuts import render, redirect
from .form import RegistrationForm

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()  # Save form data to the database
            
            # Redirect to success page and pass the data via URL parameters
            return redirect(f'/success/?full_name={registration.full_name}&registration_number={registration.registration_number}'
                            f'&department={registration.department}&faculty={registration.faculty}'
                            f'&level={registration.level}&phone_number={registration.phone_number}&gender={registration.gender}')
        else:
            error = "Please correct the errors below."
    else:
        form = RegistrationForm()
        error = None

    return render(request, 'registration.html', {'form': form, 'error': error})

def success_view(request):
    # Retrieve the submitted data from the URL parameters
    full_name = request.GET.get('full_name')
    registration_number = request.GET.get('registration_number')
    department = request.GET.get('department')
    faculty = request.GET.get('faculty')
    level = request.GET.get('level')
    phone_number = request.GET.get('phone_number')
    gender = request.GET.get('gender')
    
    # Pass the data to the success template
    return render(request, 'success.html', {
        'full_name': full_name,
        'registration_number': registration_number,
        'department': department,
        'faculty': faculty,
        'level': level,
        'phone_number': phone_number,
        'gender': gender
    })


