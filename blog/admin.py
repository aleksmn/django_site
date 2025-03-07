from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("tags", "date")
    list_display = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)