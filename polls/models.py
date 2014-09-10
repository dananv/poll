from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
	"""
	Making a poll interface in the Django admin, through calling 
	models.Model. Defines a question, publication date and whether it 
	was pubished recently. 
	"""

	# Adding a custom method.
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	# Give some attributes to was_published_recently.
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_desription = 'Published recent'
	
	# Adding an unicode method to Poll.
	def __str__(self):
		return self.question
	
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')


class Choice(models.Model):
	"""
	Describes the choices for a poll and keeps track of the number of 
	votes. 
	"""

	# Adding an unicode method to Choice.
	def __str__(self):
		return self.choice_text
	
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

