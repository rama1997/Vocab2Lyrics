import lyricsgenius
from config import (
    GENIUS_CLIENT_ID,
)

# Initialize Genius API
genius = lyricsgenius.Genius(GENIUS_CLIENT_ID)


def get_song_info(song_name: str, artists: str):
    """
    Search for the song info using the Genius API
    """
    song_info = genius.search_song(song_name, artists)
    return song_info
