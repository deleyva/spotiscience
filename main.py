from spotiscience.credentials import CREDENTIALS
import spotiscience.downloader as downloader
import json

sd = downloader.SpotiScienceDownloader(credentials=CREDENTIALS)
song_copy_link = (
    "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b?si=369f90167c9d48fb"
)
song = sd.get_song_features(song_id=song_copy_link)
print(json.dumps(song, indent=4))

lyrics = sd.get_song_lyrics(songname=song["name"], artistname=song["artist"])
print(lyrics)

genre = sd.get_song_music_genre(song_id=song["id"])
print(genre)