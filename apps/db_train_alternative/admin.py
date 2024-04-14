from django.contrib import admin
from .models import Blog, Author, Entry, Tag, AuthorProfile, favourite_author

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Tag)
admin.site.register(AuthorProfile)
admin.site.register(favourite_author)
