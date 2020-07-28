from django import forms 

class PollForm(forms.Form):
    title = forms.CharField(label='Title', required=True, max_length=250, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-4', 'placeholder' : 'Poll title'}))
    option01 = forms.CharField(label='Answers:', required=True, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll answer', 'id': 'option01'}))
    option02 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll answer', 'id': 'option02'}))
    option03 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll answer', 'id': 'option03'}))
    option04 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll answer', 'id': 'option04'}))
    option05 = forms.CharField(label='', required=False, max_length=100, 
        widget=forms.TextInput(
            attrs={'class' : 'form-control form-control-sm mb-2', 'placeholder' : 'Add poll answer', 'id': 'option05'}))