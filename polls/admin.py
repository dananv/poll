from django.contrib import admin
from polls.models import Choice, Poll

# Tell Django Choice objects are edited on the Poll admin page.

class ChoiceInline(admin.TabularInline): #Tabular instead of Stacked saves space
	model = Choice
	extra = 3

# Register your models here.

class PollAdmin(admin.ModelAdmin):

	list_display = ('question', 'pub_date', 'was_published_recently')
	# Add a filter sidebar, Django gives automatic filter options with pub_date
	list_filter = ['pub_date']
	# Add search capability
	search_fields = ['question']
	# Split up the form into fieldsets.
	fieldsets = [	
		(None,					{'fields' : ['question']}),
		('Date information', 	{'fields' : ['pub_date'], 'classes': ['collapse']}),
	]	
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)