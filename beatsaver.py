from typing import Dict
import breakCloudflare as bc

class Beatmap:
    #The attributes of the map that are shown in game:
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
    #BeatSaver Specific attributes
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



    def __init__(self, key : str):
        #Try to make an api request when creating the map
        try:
            response = bc.scrape_url("https://beatsaver.com/api/maps/detail/"+key)
        except:
            print("Something went wrong making the API call for map: "+key)
            return

        # Set the attributes accordingly
        self.hash = response["hash"]
        self.gameSongName = response["metadata"]["songName"]
        self.gameSubname = response["metadata"]["songSubName"]
        self.gameArtistName = response["metadata"]["songAuthorName"]
        self.gameMapperName = response["metadata"]["levelAuthorName"]
        self.bpm = response["metadata"]["bpm"]
        self.difficulties = response["metadata"]["difficulties"]
        self.duration = response["metadata"]["duration"]

        
        self.easy = response["metadata"]["characteristics"][0]["difficulties"]["easy"]
        self.normal = response["metadata"]["characteristics"][0]["difficulties"]["normal"]
        self.hard = response["metadata"]["characteristics"][0]["difficulties"]["hard"]
        self.expert = response["metadata"]["characteristics"][0]["difficulties"]["expert"]
        self.superexpert = response["metadata"]["characteristics"][0]["difficulties"]["expertPlus"]

        #BeatSaver Specific attributes
        self.key = response["key"]
        self.description = response["description"]
        self.name = response["name"]
        self.uploader = response["uploader"]
        self.uploaded = response["uploaded"]
        self.hash = response["hash"]
        self.directDownload = response["directDownload"]
        self.apiDownload = response["downloadURL"]
        self.coverURL = response["coverURL"]

        #Stats on beatsaver
        self.downloads = response["stats"]["downloads"]
        self.plays = response["stats"]["plays"]
        self.downvotes = response["stats"]["downVotes"]
        self.upvotes = response["stats"]["upVotes"]
        self.heat = response["stats"]["heat"]
        self.rating = response["stats"]["rating"]    
    
class Search:
    resultNames = []
    resultKeys = []
    totalResults = None
    lastPage = None
    prevPage = None
    nextPage = None

    
    def __init__(self, query, page = 0):
        response = bc.scrape_url("https://beatsaver.com/api/search/text/"+str(page)+"?q="+str(query))

        self.totalResults = response["totalDocs"]
        self.lastPage = response["lastPage"]
        self.nextPage = response["nextPage"]
        self.prevPage = response["prevPage"]

        for map in response["docs"]:
            self.resultNames.append(map["name"])
            self.resultKeys.append(map["key"])
            
        




        
        
        

        


