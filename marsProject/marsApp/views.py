from django.shortcuts import render, redirect
from .forms import Stage1Form, Stage2Form, Stage3Form

def index(request):
    return render(request, 'landing/index.html')

def application_stage1(request):
    # Retrieve session data if it exists
    session_data = request.session.get('stage1', {})

    if request.method == "POST":
        form = Stage1Form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['date_of_birth'] = form_data['date_of_birth'].isoformat()  # Convert date to ISO format string
            # Save data to session and move to the next stage
            form_data['phone'] = str(form_data['phone'])  # Convert phone number to string
            request.session['stage1'] = form_data
            return redirect('application_stage2')
    else: #handle GET request
        form = Stage1Form(initial=session_data)

    return render(request, 'application_form/stage1.html', {'form': form})

def application_stage2(request):
    if 'stage1' not in request.session:
        return redirect('application_stage1')
    
    # Retrieve session data if it exists
    session_data = request.session.get('stage2', {})

    if request.method == "POST":
        form = Stage2Form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['departure_date'] = form_data['departure_date'].isoformat()  # Convert date to ISO format string
            form_data['return_date'] = form_data['return_date'].isoformat()
            # Save data to session and move to the next stage
            request.session['stage2'] = form_data
            return redirect('application_stage3')
    else:
        form = Stage2Form(initial = session_data)

    return render(request, 'application_form/stage2.html', {'form': form})

def application_stage3(request):
    if 'stage1' not in request.session or 'stage2' not in request.session:
        return redirect('application_stage1')
    
    # Retrieve session data if it exists
    session_data = request.session.get('stage3', {})

    if request.method == "POST":
        form = Stage3Form(request.POST)
        if form.is_valid():
            # Save the data
            stage1_data = request.session['stage1']
            stage2_data = request.session['stage2']
            stage3_data = form.cleaned_data
            # Here, you could save to the database or handle data as needed
            # For now, let's clear the session and show success message
            request.session.flush()
            return render(request, 'application_form/success.html')
    else:
        form = Stage3Form(initial = session_data)

    return render(request, 'application_form/stage3.html', {'form': form})
