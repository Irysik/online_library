from django.db import models


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default='Default Genre Name')

    def __str__(self):
        return self.name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    birth_date = models.DateField()
    country = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=256)
    publication_year = models.IntegerField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    fragment = models.TextField(max_length=7000, blank=True, null=True)

    def __str__(self):
        return self.name
