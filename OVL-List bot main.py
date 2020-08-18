#bot.py
import os
import wptools
import discord
import wikipedia
from dotenv import load_dotenv
#bot.py
import os
import wptools
import discord
import wikipedia
from dotenv import load_dotenv#bot.py
import os
import wptools
import discord
import wikipedia
from dotenv import load_dotenv



max_submissions=2
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
ADMIN = int(os.getenv('ADMIN'))
CHANNEL = int(os.getenv('CHANNEL'))

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
        album = message.content.lower()[5:]
        x = album.split("//")
        if len(x)<4:
            response= """There's (at least) a missing item in your submission. Please use the format: 
.sub Album // Artist // Year // Genre"""
            await message.channel.send(response)
            return
        for s in range(4):
            x[s]=x[s].lstrip()
            x[s]=x[s].capitalize()
        
        channel = client.get_channel(CHANNEL)
        
        result=wikipedia.search(x[0]+" "+x[1])
        
        if not result:
            response = """The wikipedia search was unsuccessful. Please check your spelling. If the spelling is correct \
the album might not be in wikipedia. If this is the case please contact staff for a manual review"""
            await message.channel.send(response)
            return
        response = message.content[5:] 
        ab = wptools.page(result[0]).get_parse()
        infobox = ab.data['infobox']
        
        y= infobox.get("genre")
        if not y:
            response = """The wikipedia article does not include a genre for this album. I've messaged staff for a manual review"""
            await message.channel.send(response)
            user = client.get_user(ADMIN)
            await user.send('An album with no genre specified in wikipedia has been submitted. Please check.')
            return
        
        y= y.lower()        
        
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
