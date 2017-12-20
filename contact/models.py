import uuid
from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse



# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	message = models.TextField(max_length=600)
	date_added = models.DateTimeField(auto_now_add=True)
	verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

	def __str__(self):
		return "{} at {}".format(self.name, self.email)

	def get_absolute_url(self):
		return reverse('contact:contact_message', args=[self.pk])