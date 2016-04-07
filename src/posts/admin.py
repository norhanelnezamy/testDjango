from django.contrib import admin

# Register your models here.

from .models import Posts

class PostAdmin(admin.ModelAdmin):
	list_display = ["title","image","content","timestamp","update"]
	list_filter = ["timestamp"]
	search_fields = ["title"]
	list_editable = ["title"]

admin.site.register(Posts,PostAdmin)