#import forms
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Stage1Form(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name", required=True)
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.SelectDateWidget(years=range(1900, 2025)), required=True)
    nationality = forms.CharField(max_length=50, label="Nationality", required=True)
    email = forms.EmailField(label="Email", required=True)
    phone = PhoneNumberField(region="CA", label="Phone Number", required=True)

class Stage2Form(forms.Form):
    departure_date = forms.DateField(label="Departure Date", widget=forms.SelectDateWidget(), required=True)
    return_date = (forms.DateField(label="Return Date", widget=forms.SelectDateWidget(), required=True))
    accommodation_preference = forms.ChoiceField(choices=[('space_hotel', 'Space Hotel'), ('martian_base', 'Martian Base')], label="Accommodation Preference", required=True)
    special_requests = forms.CharField(widget=forms.Textarea, required=False, label="Special Requests or Preferences")

class Stage3Form(forms.Form):
    health_declaration = forms.BooleanField(label="Health Declaration", required=True)
    emergency_contact = forms.CharField(max_length=100, label="Emergency Contact Information", required=True)
    medical_conditions = forms.CharField(widget=forms.Textarea, required=False, label="Any Medical Conditions")