from	django	import	forms
from	courses.models	import	Course
class	CourseEnrollForm(forms.Form):
    course	=	forms.ModelChoiceField(queryset=Course.objects.all(),
                                          widget=forms.HiddenInput)



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    class Meta:
        model=User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']
