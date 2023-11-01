# Vocab2Lyrics
Listening to music and songs was a fun helpful way for me to get practice and immersion when I was studying a foreign language. This is a short program I made when I was learning Korean. Goal was to search for songs in a Spotify playlist for a specific vocab that I was learning at the time. This would allow for more easy real world examples and familiarity in my study material. 

<img src="https://i.imgur.com/d3MZydb.png" width="450" height="300" />

# Features
- Search through all songs in a Spotify playlist for the desired vocabulary or phrase
- Retrieve all lines that contains the word or phrase 
- The lines containing the word or phraseb will also be translated through Google Translate

# Requirements 
- Need Spotify API Key 
- Need Genius API Key 
- Spotify Playlist

# Setup
Configure `config.py` with the desired data

- Spotify API Key 
- Genius API Key
- Enter the Spotify playlist's uri that you want to search
- Redirect URI is set to local host by default

# Usage 
- Install dependencies: `pip install -r requirments.txt`
- Args:
    -v --vocab: vocab to search for
- Run: py main.py -v vocab

# Todo
- Add feature to take into account different forms for the same word. This is important for languages like Korean.
