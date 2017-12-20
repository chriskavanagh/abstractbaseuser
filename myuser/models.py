import uuid
from django.db import models
from django.http import Http404

from django.urls import reverse
from django.conf import settings

from django.utils import timezone
from django.dispatch import receiver
from django.core.mail import send_mail

from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

#from django.contrib.auth import get_user_model
#User = get_user_model()

# Create your models here.
class MyUserAccountManager(BaseUserManager):
	"""Manager For MyUser Custom User Model."""

	def create_user(self, email=None, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(email=self.normalize_email(email),)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password=password,)
		user.is_admin = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser, PermissionsMixin):
	"""Custom User Model With Email As Username and Permissions Mixin."""

	email = models.EmailField(verbose_name='email', max_length=255, unique=True,)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	gender = models.CharField(max_length=140)	
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	#is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Designates whether the user can log into this admin site.'),)	
	is_active = models.BooleanField('active', default=True)
	is_admin = models.BooleanField(default=False)
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	is_verified = models.BooleanField('verified', default=False)
	verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)
	

	objects = MyUserAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email

	# def has_perm(self, perm, obj=None):    # provided in PermissionsMixin
	# 	return True

	# def has_module_perms(self, app_label): # provided in PermissionsMixin
	# 	return True

	@property
	def is_staff(self):
		return self.is_admin


@receiver(post_save, sender=MyUser)
def send_user_mail(sender, created, instance, **kwargs):
	if created:
		user = MyUser.objects.get(pk=instance.pk)
		#uuid64 = user.verification_uuid
		#domain = Site.objects.get_current().domain
		subject = "Welcome To Our Django Community!"
		from_email = settings.EMAIL_HOST_USER
		#to_email = user.email
		to_email = 'ckava3@gmail.com'
		uidb64 = urlsafe_base64_encode(force_bytes(user.pk)).decode()
		token = default_token_generator.make_token(user)
		message = 'http://localhost:8000%s' % reverse('verify', args=[uidb64, token])
		if not instance.is_verified:
			try:
				send_mail(subject, message, from_email, [to_email,], fail_silently=False)
			except BadHeaderError:
				raise Http404('Invalid Header Found.')
			



# @receiver(post_save, sender=MyUser)
# def send_user_mail(sender, created, instance, **kwargs):
# 	if created:
# 		user = MyUser.objects.get(pk=instance.pk)
# 		#uuid64 = user.verification_uuid
# 		#domain = Site.objects.get_current().domain
# 		subject = "Welcome To Our Django Community!"
# 		from_email = settings.EMAIL_HOST_USER
# 		#to_email = user.email
# 		to_email = 'ckava3@gmail.com'
# 		uidb64 = urlsafe_base64_encode(force_bytes(user.pk)).decode()
# 		token = default_token_generator.make_token(user)
# 		message = 'http://localhost:8000%s' % reverse('verify', args=[uidb64, token])
# 		if not instance.is_verified:
# 			send_mail(subject, message, from_email, [to_email,], fail_silently=False)
		
