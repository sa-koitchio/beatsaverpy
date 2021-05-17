
import beatsaver # Import beatsaver

theMap = beatsaver.Beatmap("1") # Get info on a map: parameter is the map key

theSearch = beatsaver.Search("USAO",0) # you can also search for maps by queue

# These lines are because some people put funny unicode in their map names, windows cmd does not like that.
result = ""
for map in theSearch.resultNames:
    result += map

result = result.encode("ascii","ignore") # Get rid of unicode only chars
result = result.decode()

print(result)