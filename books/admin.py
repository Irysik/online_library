from django.contrib import admin

from books import models


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
