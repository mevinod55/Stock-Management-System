from django import forms

from Device.models import Laptops, Desktops, Mobiles


class LaptopForm(forms.ModelForm):
    type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    status=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    issues=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Laptops
        fields = ('type', 'price', 'status', 'issues')


class DesktopForm(forms.ModelForm):
    type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    status=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    issues=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'status', 'issues')


class MobileForm(forms.ModelForm):
    type=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    status=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    issues=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'status', 'issues')
