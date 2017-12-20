from django.contrib import admin
from .models import Contact

# Register your models here.
class  ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'date_added', 'verification_uuid')
	search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)