from django import forms
from .models import Client
from programs.models import Program
from .models import Enrollment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'age', 'gender', 'contact_info']


class EnrollmentForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    programs = forms.ModelMultipleChoiceField(queryset=Program.objects.all(), widget=forms.CheckboxSelectMultiple)
    


class ClientSearchForm(forms.Form):
    query = forms.CharField(required=False, label="Search by Name", max_length=100)
    min_age = forms.IntegerField(required=False, label="Min Age")
    max_age = forms.IntegerField(required=False, label="Max Age")
    gender = forms.ChoiceField(
        required=False,
        choices=[('', 'Any')] + Client.GENDER_CHOICES,
        label="Gender"
    )
    program = forms.ModelChoiceField(
        required=False,
        queryset=Program.objects.all(),
        label="Program"
    )

