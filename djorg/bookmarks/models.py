from uuid import uuid4
from django.db import models

# Create your models here.
class Bookmark(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	url = models.URLField('URL', unique=True) #constraint to restrict
	name = models.CharField(max_length=200)
	notes = models.TextField(blank=True)