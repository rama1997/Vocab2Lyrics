import argparse
import song_helpers
from config import PLAYLIST_URI

# Create an argument parser
ap = argparse.ArgumentParser()

# Add arguments options
ap.add_argument("-v", "--vocab", required=True, type=str, help="Enter vocab")

if __name__ == "__main__":
    args = ap.parse_args()
    if args:
        vocab = args.vocab

    songs_with_vocab = song_helpers.get_songs_with_vocab(vocab, PLAYLIST_URI)

    if songs_with_vocab:
        for song in songs_with_vocab:
            song_name = song[0]
            artists = song[1]
            lines_with_vocab = song[2]
            song_lyrics_url = song[3]
            song_spotify_uri = song[4]

            print("\n--------------------------\n")
            print(f"{song_name} - {artists}:")
            for i, line in enumerate(lines_with_vocab):
                print(f"\n{i+1}: {line}")
                translated_text = song_helpers.get_translation(line)
                print(f"Translation: {translated_text.text}")

            print(f"\nGenius Lyrics: {song_lyrics_url}")
            print(f"Spotify: https://open.spotify.com/track/{song_spotify_uri}")
    else:
        print(f'No song contains "{vocab}"')
