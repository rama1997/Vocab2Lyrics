import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REDIRECT_URI,
)

# Initialize the Spotify API client
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-read-private",
    )
)


def get_playlist_songs(playlist_uri) -> list:
    """
    Retrieve the playlist tracks from Spotify Playlist
    """
    playlist_songs = spotify.playlist_tracks(playlist_uri)
    return playlist_songs
