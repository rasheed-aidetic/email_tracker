from django.contrib import admin
from .models import SendMail, TrackMail

# Register your models here.

admin.site.register(SendMail)
admin.site.register(TrackMail)