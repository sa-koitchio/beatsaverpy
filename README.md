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

## beatsaver.Search("Query:string",(optional: result page, default = 0))

has 2 lists: one list saves the keys of the resulting maps (0 is first), the other list saves the preview names from beatsaver



