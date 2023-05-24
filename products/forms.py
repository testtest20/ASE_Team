from django import forms
from .models import medicines,category
class medicineform(forms.ModelForm):
       class Meta:
            model= medicines
            fields=['name','price','medicine_photo']




            widgets={
       
                  'name':forms.TextInput(attrs={'class':'form-control'}),
                  'price':forms.NumberInput(attrs={'class':'form-control'}),
                  'medicine_photo':forms.FileInput(attrs={'class':'form-control'}),
            }








