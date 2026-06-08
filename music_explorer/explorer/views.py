import json
import os

from django.http import JsonResponse
from django.shortcuts import render

# Load the music data from the JSON file. 
def load_music_data():
    # Get the path to the data file. 
    path = os.path.join(
        os.path.dirname(__file__), "data", "data.json"
    )
    # Open and read JSON file. 
    with open(path, encoding="utf-8") as file:
        return json.load(file)
    
# Show the homepage.
def home(request):
    return render(request, "explorer/index.html")

# Handle search requests. 
def search_music(request):
    # Get the search term from the URL.
    query = request.GET.get('q', '').lower()
    # Load all music data. 
    data = load_music_data()
    # Lists to store results. 
    artists = []
    albums = []
    songs = []

    # Go through each artist in the data.
    for artist in data:
        # Check if search matches the artist name. 
        if query in artist["name"].lower():
            artists.append({
                "name": artist["name"],
                "album_count": len(artist["albums"])
            })
        # Go through each album for the artist.
        for album in artist["albums"]:
            # Check if the search matches the album title. 
            if query in album["title"].lower():
                albums.append({
                    "artist": artist["name"],
                    "title": album["title"],
                    "description": album["description"]
                })
            # Go through each song in the album. 
            for song in album["songs"]:
                # Check if the search matches the song title. 
                if query in song["title"].lower():
                    songs.append({
                        "artist": artist["name"],
                        "album": album["title"],
                        "title": song["title"],
                        "length": song["length"]
                    })
    # Send results back as JSON. 
    return JsonResponse({
        "artists": artists,
        "albums": albums,
        "songs": songs
    })
