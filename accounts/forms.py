# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()




from .models import MyFormData, Item
from .models import ExpenseReport, ExpenseDetail



class MyFormDataForm(forms.ModelForm):


    class Meta:
        model = MyFormData
        fields = [
            'company', 'your_name', 'company_gstin', 'company_address',
            'city', 'state', 'country', 'client_company', 'client_gstin',
            'client_address', 'client_city', 'client_state', 'client_country',
            'invoice', 'datetime_field1', 'datetime_field2','logo', 'notes', 'terms_conditions'
        ]
        widgets = {
            'logo': forms.ClearableFileInput(attrs={ 'placeholder': 'Upload logo' ,'style':'width: 30%'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name'}),
            'your_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your name'}),
            'company_gstin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' company GSTIN'}),
            'company_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' company address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' state'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' country'}),
            'client_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' client company'}),
            'client_gstin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'client GSTIN'}),
            'client_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' client address'}),
            'client_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' client city'}),
            'client_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' client state'}),
            'client_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' client country'}),
            'invoice': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' invoice details'}),
            'datetime_field1': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Select date and time'}),
            'datetime_field2': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Select date and time'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes', 'rows': 3}),
            'terms_conditions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Terms and Conditions', 'rows': 3}),

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        
      
class ItemForm(forms.ModelForm):
    GST_RATE_CHOICES = [
        (0, '0%'),
        (5, '5%'),
        (12, '12%'),
        (18, '18%'),
        (28, '28%'),
    ]
    
    gst_rate = forms.ChoiceField(choices=GST_RATE_CHOICES, initial=0, label='GST Rate (%)')
    class Meta:
        model = Item
        fields = ['item_desc', 'qty', 'rate','gst_rate','sgst', 'cgst', 'cess']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control','style': 'width:100% ; margin-left:20px; '})
        if 'gst_rate' in self.fields:
            self.fields['gst_rate'].widget.attrs.update({'style': 'width:80%; margin-left:20px; '})  # Adjust the width as needed
           
        self.fields['sgst'].required = False
        self.fields['cgst'].required = False
       




class ExpenseReportForm(forms.ModelForm):

    class Meta:
        model = ExpenseReport
        fields = ['company_name', 'your_name', 'company_address', 'city', 'state', 'country', 'report_from', 'report_to', 'date_from', 'date_to']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': ' Company', 'class': 'form-control'}),
            'your_name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'company_address': forms.TextInput(attrs={'placeholder': 'Enter company address', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter state', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'form-control'}),
            'report_from': forms.TextInput(attrs={'placeholder': 'Enter report from', 'class': 'form-control'}),
            'report_to': forms.TextInput(attrs={'placeholder': 'Enter report to', 'class': 'form-control'}),
            'date_from': forms.DateTimeInput(attrs={'placeholder': 'Select date from', 'class': 'form-control'}),
            'date_to': forms.DateTimeInput(attrs={'placeholder': 'Select date to', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].initial is None:
                self.fields[field].initial = ''

 

    

class ExpenseDetailForm(forms.ModelForm):
    class Meta:
        model = ExpenseDetail
        fields = ['date', 'expense_description', 'merchant', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].initial is None:
                self.fields[field].initial = ''




from .models import PackageReport, PackageDetail  # Adjust the import based on your project structure

class PackageReportForm(forms.ModelForm):
    class Meta:
        model = PackageReport
        fields = [
            'company_name', 'your_name','city','state','country','client_name', 
            'client_city', 'client_state', 'client_country', 
            'package', 'order_date', 'package_date', 
            'sales_order', 'notes'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Company Name', 'class': 'form-control'}),
            'your_name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter state', 'class': 'form-control'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country', 'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'placeholder': 'Enter client name', 'class': 'form-control'}),
            'client_city': forms.TextInput(attrs={'placeholder': 'Enter client city', 'class': 'form-control'}),
            'client_state': forms.TextInput(attrs={'placeholder': 'Enter client state', 'class': 'form-control'}),
            'client_country': forms.TextInput(attrs={'placeholder': 'Enter client country', 'class': 'form-control'}),
            'package': forms.TextInput(attrs={'placeholder': 'Enter package details', 'class': 'form-control'}),
            'order_date': forms.DateTimeInput(attrs={'placeholder': 'Select order date', 'class': 'form-control'}),
            'package_date': forms.DateTimeInput(attrs={'placeholder': 'Select package date', 'class': 'form-control'}),
            'sales_order': forms.TextInput(attrs={'placeholder': 'Sales Order (optional)', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Enter any notes', 'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].initial is None:
                self.fields[field].initial = ''


class PackageDetailForm(forms.ModelForm):
    class Meta:
        model = PackageDetail
        fields = ['item_description', 'order_quantity', 'shipped_quantity']
        widgets = {
            'item_description': forms.TextInput(attrs={'placeholder': 'Item Description', 'class': 'form-control'}),
            'order_quantity': forms.NumberInput(attrs={'placeholder': 'Order Quantity', 'class': 'form-control'}),
            'shipped_quantity': forms.NumberInput(attrs={'placeholder': 'Shipped Quantity', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].initial is None:
                self.fields[field].initial = ''