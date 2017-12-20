from django.http import Http404
from django.conf import settings
from .forms import UserCreationForm
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
#from .models import MyUser


# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.save()
			return redirect('home_view')
	else:
		form = UserCreationForm()
	context = {'form':form}
	return render(request, 'register.html', context)


def verify(request, uidb64=None, token=None):
	UserModel = get_user_model()
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = UserModel.objects.get(pk=uid)
	except (TypeError, ValueError, UserModel.DoesNotExist):
		user = None

	if user == None:
		raise Http404("User does not exist or is already verified")

	if user is not None and default_token_generator.check_token(user, token):		
		user.is_verified = True
		user.save()
	return redirect('home_view')


# def verify(request, uuid64=None, token=None):
# 	UserModel = get_user_model()
# 	try:
# 		user = UserModel.objects.get(verification_uuid=uuid64, is_verified=False)
# 	except UserModel.DoesNotExist:
# 		raise Http404("User does not exist or is already verified")

# 	if user is not None and default_token_generator.check_token(user, token):		
# 		user.is_verified = True
# 		user.save()
# 		return redirect('home_view')


