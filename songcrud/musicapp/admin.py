from django.contrib import admin
from musicapp.models import Artiste,Lyric,Song

# Register your models here.

'''
admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)

'''

@admin.register(Artiste)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'age')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title','date_released', 'Artiste','artiste_id')

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ('Content','Song','song_id')