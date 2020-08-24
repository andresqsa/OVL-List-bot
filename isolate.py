def isolate(text):
    index=text.find('"genres":')
    index2=text[index:].find("],")
    
    index3=text.find('"styles":')
    index4=text[index3:].find("],")
    
    if (index3<0):
        if (index<0):
            return([])
        return(text[index:index+index2+1])
    return(text[index:index3+index4+1])
    