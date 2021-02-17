from django.db import models
from django.utils import timezone
import random
# Create your models here.


class Memo(models.Model):
	title = models.CharField(max_length=65)
	slug = models.SlugField(max_length=65, unique=True, null=True, blank=True)
	full_name = models.CharField(max_length=65)
	position = models.CharField(max_length=65)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)


	""" Generate Slug """
	def _generate_unique_slug(self):
		unique_slug = random.randrange(1000, 4000)
		while Memo.objects.filter(slug=unique_slug).exists():
			unique_slug = random.randrange(1000, 4000)
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._generate_unique_slug()
		super().save(*args, **kwargs)


	def __str__(self):
		return self.title + ' - ' + self.full_name + '('+self.position+')'


	class Meta:
    		ordering = ['-date_posted']
