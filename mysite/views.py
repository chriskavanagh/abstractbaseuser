from django.core.mail import send_mail
from contact.forms import ContactForm
#from .forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
import django


def home_view(request):
	v = django.get_version()
	if v >= str(2.0):
		print("I'm 2.0 django!")
	print(django.get_version())
	contact_form = ContactForm()
	return render(request, 'home.html', {'contact_form':contact_form})