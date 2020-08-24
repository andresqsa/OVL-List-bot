import wikipedia
import wptools
from discogsearch import discogsearch
def genre(title,artist):
    result=wikipedia.search(title+" "+artist)
        
    if not result:
        genre=discogssearch(title,artist)
        return(genre)
        
    ab = wptools.page(result[0]).get_parse()
    infobox = ab.data['infobox']
        
    y= infobox.get("genre")
    if not y:
        genre=discogsearch(title,artist)
        return(genre)        
    y= y.lower()         
        
    ind1=1/y.find("rock")
    ind2=1/y.find("metal")
    ind3=1/y.find("punk") 
    ind4=1/y.find("thrash")
    ind5=1/y.find("blues")
    ind6=1/y.find("grunge")
    
    if (ind1+ind2+ind3+ind4+ind5+5==0):
        genre=[]
        return(genre)
    
    allgenres={ind1:"Rock",ind2:"Metal",ind3:"Punk",ind4:"Thrash",ind5:"Blues",ind6:"Grunge"}
    genre=allgenres.get(max(allgenres))

    return(genre)