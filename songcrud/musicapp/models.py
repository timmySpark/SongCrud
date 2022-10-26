from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    

    class Meta:
        verbose_name = ("Artiste")
        verbose_name_plural = ("Artistes")

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id = models.ForeignKey('Artiste',on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField()
    

    class Meta:
        verbose_name = ("Song")
        verbose_name_plural = ("Songs")

    def __str__(self):
        return f'{self.artiste_id} ----- {self.title}'



class Lyric(models.Model):
    song_id = models.ForeignKey('Song',on_delete=models.CASCADE)
    content= models.TextField()
    
    

    class Meta:
        verbose_name = ("Lyric")
        verbose_name_plural = ("Lyrics")

    def __str__(self):
        return f'{self.song_id} :- {self.content}'