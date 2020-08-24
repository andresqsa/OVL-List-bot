import os
import wptools
import discord
import wikipedia
import discogs_client
import requests

from extraction import extraction
from dotenv import load_dotenv



max_submissions=2
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
ADMIN = int(os.getenv('ADMIN'))
CHANNEL = int(os.getenv('CHANNEL'))
DISCOGSTOKEN = os.getenv('DISCOGSTOKEN')

client =  discord.Client()

@client.event 
async def on_ready(): 
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    if '.sub' in message.content.lower():
        
        mes=extraction(message)
        
        if mes.get("format")==0:
            channel=message.channel()
            response="There's (at least) a missing item in your submission. Please use the format: \n.sub Album // Artist // Year // Genre"
            await channel.send(response)
            return
        
        channel = client.get_channel(CHANNEL)
        
        title=mes.get("title")
        artist=mes.get("artist")
        
        genre=
        
        result=wikipedia.search(title+" "+artist)
        
        if not result:
            
            
            d=discogs_client.Client('Discordlist',user_token=DISCOGSTOKEN)
            results=d.search(x[0],type='release')
            id=str(results[0].id)
                
            params = (('', DISCOGSTOKEN),)
            ab = requests.get('https://api.discogs.com/releases/'+id, params=params)
            
            y=ab.text.lower()
            ind1=y.find("rock")
            ind2=y.find("metal") 
            ind3=y.find("punk") 
            ind4=y.find("thrash")
            ind5=y.find("blues")
            
            if (ind1+ind2+ind3+ind4+ind5+5>0):
                await channel.send(response)
            
            return
        
        ab = wptools.page(result[0]).get_parse()
        infobox = ab.data['infobox']
        
        y= infobox.get("genre")
        if not y:
            d=discogs_client.Client('Discordlist',user_token=DISCOGSTOKEN)
            results=d.search(x[0],type='release')
            print(results[0].title)
            id=str(results[0].id)
            print(id)
            params = (('', 'rGnUvRXwxRqwrHrNGLHTmqTQYbHnCLAefiFhWQpA'),)
            ab = requests.get('https://api.discogs.com/releases/'+id, params=params)
            
            y=ab.text.lower()
            ind1=y.find("rock")
            ind2=y.find("metal")
            ind3=y.find("punk") 
            ind4=y.find("thrash")
            ind5=y.find("blues")
            if (ind1+ind2+ind3+ind4+ind5+5>0):
                await channel.send(response) 
            else:
                user = client.get_user(ADMIN)
                await user.send('Non rock album submitted. Please check.') 
            return        
        y= y.lower()         
        
        ind1=y.find("rock")
        ind2=y.find("metal")
        ind3=y.find("punk") 
        ind4=y.find("thrash")
        ind5=y.find("blues")
 
        if (ind1+ind2+ind3+ind4+ind5+5>0):
            await channel.send(response)
        else: 
            user = client.get_user(ADMIN)
            await user.send('Non rock album submitted. Please check.')
        
client.run(TOKEN)   
