from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField(auto_now_add=False)
    body = models.TextField(max_length=700)
    image = models.ImageField(upload_to='images/')


# Create your blog models
## Title
## Pub_date
## Body
## Image

# Add the blog app to the settings

# Create a migration

# Migrate

# Add to the admin
