from django.contrib import admin

# Register your models here.
from books.models import Book, Section

admin.site.register(Book)
admin.site.register(Section)
