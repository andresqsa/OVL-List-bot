#bot.py
import os
import wptools
import discord
import wikipedia
from dotenv import load_dotenv

load_dotenv()

max_submissions=2

TOKEN = *BOT_TOKEN*
GUILD = *SERVER NAME*
CHANNEL = *LIST CHANNEL ID*
ADMIN = *ADMIN ID*

client =  discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '.sub' in message.content.lower():
        album = message.content.lower()[5:]
        x = album.split("//")
        for s in range(4):
            x[s]=x[s].lstrip()
            x[s]=x[s].capitalize()
        response = message.content[5:] 
        channel = client.get_channel(CHANNEL)
        
        result=wikipedia.search(x[0]+" "+x[1])
        
        ab = wptools.page(result[0]).get_parse()
        infobox = ab.data['infobox']

        y= infobox.get("genre").lower()
        ind1=y.find("rock")
        ind2=y.find("metal")
        ind3=y.find("punk") 
        ind4=y.find("thrash")
        ind5=y.find("blues")
        y= y.replace("\n"," ")
 
        if (ind1+ind2+ind3+ind4+ind5+5>0):
            await channel.send(response)
        else: 
            user = client.get_user(ADMIN)
            await user.send('Non rock album submitted. Please check.')
        
client.run(TOKEN)   
