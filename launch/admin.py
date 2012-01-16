from django.contrib import admin
from sindeo.launch.models import UserEmails

class UserEmailsAdmin(admin.ModelAdmin):
	list_display = ('email', 'subscribed')
	search_fields = ('email',)
	list_filter = ('subscribed',)
	ordering = ('-email',)

admin.site.register(UserEmails, UserEmailsAdmin)
