from django import forms


class ContactForm(forms.Form):
    CONTACT_TYPES = [
        ('beneficiary', 'Beneficiary'),
        ('partner', 'Partner'),
        ('sponsor', 'Sponsor'),
        ('media', 'Media'),
        ('general', 'General Inquiry'),
    ]

    full_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=30, required=False)
    contact_type = forms.ChoiceField(choices=CONTACT_TYPES)
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
