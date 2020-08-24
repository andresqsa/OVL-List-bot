import os
import discogs_client
import requests
from dotenv import load_dotenv
from isolate import isolate

load_dotenv()
DISCOGSTOKEN = os.getenv('DISCOGSTOKEN')

def discogsearch(title,artist):
    d=discogs_client.Client('Discordlist',user_token=DISCOGSTOKEN)
    results=d.search(title+" "+artist,type='release')
    if not results:
        album="Failed"
        return(album)
    
    id=str(results[0].id)
    title=results[0].title
    artist=results[0].artists[0].name
    
    
    params = (('', DISCOGSTOKEN),)
    ab = requests.get('https://api.discogs.com/releases/'+id, params=params)        
    print(ab.text)
    y=isolate(ab.text.lower())
    if not y:
        album="Failed"
        return(album)
    
    ind1=1/y.find("rock")
    ind2=1/y.find("metal")
    ind3=1/y.find("punk") 
    ind4=1/y.find("thrash")
    ind5=1/y.find("blues")
    ind6=1/y.find("grunge")
    
    if (ind1+ind2+ind3+ind4+ind5+5==0):
        return([])
    
    allgenres={ind1:"Rock",ind2:"Metal",ind3:"Punk",ind4:"Thrash",ind5:"Blues",ind6:"Grunge"}
    genre=allgenres.get(max(allgenres))
    
    return({"title":title, "artist":artist, "genre":genre})
    
