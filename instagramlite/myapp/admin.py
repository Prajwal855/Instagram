from django.contrib import admin
from instagramlite.myapp import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
