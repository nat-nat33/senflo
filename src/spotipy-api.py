import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# FLASK
from flask import Flask
app = Flask(__name__)

# Get the username from terminal
username = sys.argv[1]

# Erase cache and prompt for user permmission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
displayName = user['display_name'] or user['id']

# Terminal Command Input
searchQuery = input("Enter Artist Name: ")


@app.route("/")
def index():
    searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
    tracks = searchResults['tracks']['items'][0]
    trackStr = tracks['preview_url']
    return trackStr


if __name__ == "__main__":
    app.run(debug=True)

# Below will print out json data we can read
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
