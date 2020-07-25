from django import forms 

class PollForm(forms.Form):
    option01 = forms.CharField(label='', required=True, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll option'}))
    option02 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll option'}))
    option03 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll option'}))
    option04 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll option'}))
    option05 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll option'}))