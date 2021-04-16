from django.db import models

# Create your models here.

class Articles:
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  # add in thumbnail later
  # add in author later

