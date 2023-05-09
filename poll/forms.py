from django import forms
from django.contrib.auth.models import User

faculty=[
    ('FOS','FOS'),
    ('FOH','FOH'),
    ('FOED','FOED')
]
class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    phone_number=forms.CharField(max_length=100)

   # faculty=forms.ChoiceField(choices=faculty)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','phone_number','password']
        widgets = {
            'password': forms.PasswordInput,
        }
    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Registration number here!!!'})
        self.fields['first_name'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Firstname here!!!'})
        self.fields['last_name'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Lastname here!!!'})
        self.fields['email'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email here!!!'})
        self.fields['phone_number'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Phone number here!!!'})
        self.fields['password'].widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password here!!!'})
        self.fields['confirm_password'].widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm your password here!!!'})


class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
