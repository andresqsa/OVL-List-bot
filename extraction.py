def extraction(message):  
    x = message.content.lower()[5:].split("//")
    if len(x)<4:
        return({"format":0})
    for s in range(4):
        x[s]=x[s].lstrip()
        x[s]=x[s].capitalize()
    return({"format":1, "title":x[0], "artist":x[1], "year":x[2], "proposed genre": x[3]})