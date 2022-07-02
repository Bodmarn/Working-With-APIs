from django.contrib import admin
from .models import target_url, description, identifier, author, created_date, active

# Register your models here.

admin.site.register(target_url)
admin.site.register(description)
admin.site.register(identifier)
admin.site.register(author)
admin.site.register(created_date)
admin.site.register(active)
