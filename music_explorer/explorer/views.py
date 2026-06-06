import json
import os

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def load_music_data():
    path = os.path.join(
        os.path.dirname(__file__), "data", "data.json"
    )

    with open(path, encoding="utf-8") as file:
        return json.load(file)
    
def home(request):
    return render(request, "explorer/index.html")


def search_music(request):
    query = request.GET.get('q', '').lower()

    data = load_music_data()

    artists = []
    albums = []
    songs = []

    for artist in data:
        if query in artist["name"].lower():
            artists.append({
                "name": artist["name"],
                "album_count": len(artist["albums"])
            })

        for album in artist["albums"]:
            if query in album["title"].lower():
                albums.append({
                    "artist": artist["name"],
                    "title": album["title"],
                    "description": album["description"]
                })

            for song in album["songs"]:
                if query in song["title"].lower():
                    songs.append({
                        "artist": artist["name"],
                        "album": album["title"],
                        "title": song["title"],
                        "length": song["length"]
                    })

    return JsonResponse({
        "artists": artists,
        "albums": albums,
        "songs": songs
    })
