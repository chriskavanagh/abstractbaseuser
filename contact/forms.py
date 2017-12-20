from .models import Contact
from django.forms import ModelForm, Textarea, TextInput, EmailInput



class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'message']
		widgets = {
					'name':TextInput(attrs={'class': 'form-control'}),
				    'email':EmailInput(attrs={'class': 'form-control'}),
				    'message':Textarea(attrs={'cols':25, 'rows':5, 'class': 'form-control'}),
			   }

