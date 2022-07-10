from django.db import models


class Movie(models.Model):

    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='movie')
    rating = models.FloatField(null=False)
    #genre = models.CharField(max_length=250)
    kinopoisk_id = models.IntegerField(null=False)
    magnet_link = models.CharField(max_length=10000)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return self.name
