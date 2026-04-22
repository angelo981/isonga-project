from django import forms
from .models import ContactMessage, ProgramApplication


class ContactForm(forms.ModelForm):
    CONTACT_TYPES = [
        ('beneficiary', 'Beneficiary'),
        ('partner', 'Partner'),
        ('sponsor', 'Sponsor'),
        ('media', 'Media'),
        ('general', 'General Inquiry'),
    ]

    phone_number = forms.CharField(max_length=30, required=False, label="Phone Number (Optional)")
    contact_type = forms.ChoiceField(choices=CONTACT_TYPES, label="What's your interest?")

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'max_length': 100}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'max_length': 200}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Your message...'}),
        }


class ProgramApplicationForm(forms.ModelForm):
    PROGRAM_CHOICES = [
        ('', 'Select a Program'),
        ('youth_empowerment', 'Youth Empowerment & Skills Development'),
        ('digital_creative', 'Digital & Creative Skills'),
        ('media_broadcasting', 'Media & Broadcasting Basics'),
        ('talent_incubation', 'Talent Incubation'),
    ]
    
    program_interest = forms.ChoiceField(choices=PROGRAM_CHOICES, label="Which program are you interested in?")
    
    class Meta:
        model = ProgramApplication
        fields = ['full_name', 'email', 'phone', 'date_of_birth', 'program_interest', 'why_join', 'experience']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Full Name', 'max_length': 100}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'why_join': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us why you want to join this program...'}),
            'experience': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any relevant experience or skills? (Optional)'}),
        }
    
    def clean_date_of_birth(self):
        from datetime import date
        dob = self.cleaned_data.get('date_of_birth')
        if dob:
            age = (date.today() - dob).days // 365
            if age < 15:
                raise forms.ValidationError("You must be at least 15 years old to apply.")
            if age > 50:
                raise forms.ValidationError("Please contact us directly if you are over 50.")
        return dob
