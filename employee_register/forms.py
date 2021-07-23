from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    #creating a form by importing model
    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code'
        }

    #for editing form.
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        #for adding empty label select in start of select position.
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False


