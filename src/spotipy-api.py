import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

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

displayName = user['display_name']

while True:

    print()
    print(">>> Welcome to Spotify!" + displayName + "!")
    print()
    print("0 - Search for an artist")
    print("1 - Exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
        # print(json.dumps(searchResults, sort_keys=True, indent=4))

        tracks = searchResults['tracks']['items'][0]
        print(json.dumps(tracks, sort_keys=True, indent=4))
        webbrowser.open(tracks['preview_url'])

    # End the program
    if choice == "1":
        break

# Below will print out json data we can read
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
