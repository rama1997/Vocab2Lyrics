import spotify_api
import genius_api
import translate


def get_songs_from_playlist(playlist_uri):
    """
    Given Spotify playlist uri, return all the songs in playlist
    """
    songs = spotify_api.get_playlist_songs(playlist_uri)
    return songs["items"]


def get_song_name(song):
    """
    Given Spotify song, return song name
    """
    return song["track"]["name"]


def get_song_artists(song):
    """
    Given Spotify song, return song artist
    """
    artists = [artist["name"] for artist in song["track"]["artists"]]
    artist_names = ", ".join(artists)
    return artist_names


def get_song_spotify_url(song):
    """
    Given Spotify song, return song uri
    """
    return song["track"]["uri"].split(":")[-1]


def get_song_lyrics(song_name, artists):
    """
    Given song name and artist, call Genius API to retrieve song lyrics and uri to genius's lyric page
    """
    song_info = genius_api.get_song_info(song_name, artists)
    if song_info:
        song_lyrics = song_info.lyrics
        song_lyrics_url = song_info.url
        return [song_lyrics, song_lyrics_url]
    else:
        return [None, None]


def get_lines_with_vocab(vocab, lyrics) -> list:
    """
    Given a song lines, return list of lines that contains the desired vocab
    """
    lines = lyrics.splitlines()
    matched_lines = []
    for line in lines:
        # Track and store each new line that contains vocab
        if vocab in line and line not in matched_lines:
            matched_lines.append(line)

    return matched_lines


def get_songs_with_vocab(vocab, playlist_uri) -> list:
    """
    Given a Spotify playlist, returns all songs from the playlist that contains the desired vocab
    """
    songs = get_songs_from_playlist(playlist_uri)

    songs_with_vocab = []
    for song in songs:
        song_name = get_song_name(song)
        artists = get_song_artists(song)
        song_spotify_uri = get_song_spotify_url(song)

        song_lyrics, song_lyrics_url = get_song_lyrics(song_name, artists)

        if song_lyrics:
            lines_with_vocab = get_lines_with_vocab(vocab, song_lyrics)

            if lines_with_vocab:
                songs_with_vocab.append(
                    [
                        song_name,
                        artists,
                        lines_with_vocab,
                        song_lyrics_url,
                        song_spotify_uri,
                    ]
                )
        else:
            print(f"No lyrics found for {song_name} by {artists}")

    return songs_with_vocab


def get_translation(line):
    """
    Translate given line into English
    """
    return translate.translator.translate(line, dest="en")
