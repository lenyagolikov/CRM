from django.contrib import admin
from django.db.models.deletion import CASCADE

from .models import User, Lead, Agent, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)
