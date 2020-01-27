from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# ckeditor.fields import RichTextField

class Post(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	body = RichTextUploadingField(blank=True, null=True)
	category = models.TextField(blank=True, null=True)
	order = models.IntegerField(blank=True, null=True)
	slug = models.SlugField(default='',max_length=255, blank=True)
	
	def save(self):
		self.slug = slugify(self.title)
		super(Post, self).save()

	def __str__(self):
		return "{}".format(self.id, self.title)