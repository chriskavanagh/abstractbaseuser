from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def message(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			f = contact_form.save(commit=True)
			send_mail(f.name, f.message ,"djangorocks@snedgrid.com", ["ckava3@gmail.com"])
			return redirect(f.get_absolute_url())
		else:
			contact_form = ContactForm()
	return redirect('home_view')


def contact_message(request, pk=None):
	message = get_object_or_404(Contact, pk=pk)
	return render(request, 'contact_message.html', {'message':message})



# def message(request):
# 	if request.method == 'POST':
# 		contact_form = ContactForm(request.POST)
# 		if contact_form.is_valid():
# 			f = contact_form.save(commit=True)
# 			return redirect(f.get_absolute_url())
# 		else:
# 			contact_form = ContactForm()
# 	return redirect('home_view')