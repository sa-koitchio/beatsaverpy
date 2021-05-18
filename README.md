# beatsaverpy
Python implementation of beatsaver's API

# Contains functionality to get info on beatmaps and request searches by query.

main.py is to show basic usage.
 
# Requirements: 
- cloudscraper (To bypass cloudflare)

# Usage: 

beatsaver has 2 classes:

## beatsaver.Beatmap("key:string")

Beatmap constructor takes the map key from beatsaver for constructor, then gets all attributes.

## The attributes of the beatmap
    gameSongName = None
    gameSubname = None
    gameArtistName = None
    gameMapperName = None
    bpm = None
    difficulties = None
    duration = None
    automapper = None
    easy = None
    normal = None
    hard = None
    expert = None
    superexpert = None
    ## BeatSaver Specific attributes
    key = None
    description = None
    name = None
    uploader = None
    uploaded = None
    hash = None
    directDownload = None
    apiDownload = None
    coverURL = None
    deletedAt = None
    #Stats on beatsaver
    downloads = None
    plays = None
    downvotes = None
    upvotes = None
    heat = None
    rating = None

## beatsaver.Search("Query:string",(optional: result page, default = 0))

has 2 lists: one list saves the keys of the resulting maps (0 is first), the other list saves the preview names from beatsaver





