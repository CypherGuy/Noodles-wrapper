Noodles API wrapper
===================
##### Created by Kabir Ghai (CypherGuy)

A wrapper for [Noodles API](www.frenchnoodles.xyz/api) used as a meme-editor and welcome banners.

Notices:
-------

* This module was designed for [discord.py](https://pypi.org/project/discord.py/ "discord.py PyPi page") 1.7+ but may work with older versions, use at your own risk however.

Installation:
-------------

###### Install with pip:
```
pip install noodleswrapper
```

Code examples:
-------------

###### Sample code with `lisastage` (Main file):
```
#Headers (Authentication) is optional.. for now.
import discord
from discord.ext import commands
import noodleswrapper
from noodleswrapper import noodle

intents = discord.Intents.all() #Allow all the intents
client = commands.Bot(command_prefix = '!', intents=intents)

@client.command()
async def lisastage(ctx):
    text = noodle.lisastage('test') #'test' is what you want it to say
    await ctx.send(file = text) #This should return a neat image.
```

###### Sample code with `lisastage` (Cog):
```
#Headers (Authentication) is optional.. for now.
import discord
from discord.ext import commands
import noodleswrapper
from noodleswrapper import noodle

class Noodle(commands.Cog):
    """Commands using Noodles wrapper."""

    def __init__(self, client):
      self.client = client

    @commands.command()
    async def lisastage(self, ctx):
        reply = noodle.lisastage('test') #'test' is what you want it to say
        await ctx.send(file = reply) #This should return a neat image.

def setup(client):
  client.add_cog(Noodle(client)) #Must be the same as the class name
```
Endpoints:
-------------
You can get a complete list [here](https://www.frenchnoodles.xyz/api/endpoints), but for now, the following are valid endpoints for this wrapper, with their inputs:

* worthless (text)
* drake (Top text, bottom text)
* presidential (Text)
* spongebobburnpaper (Text)
* lisastage (Text)
* changemind (Text)
* awkwardmokey (Text)
* blur (Image link)
* circle (Image link)
* invert (Image link)
* edge (Image link)
* wide (Image link)
* uglyupclose (Image link)
* clown (Image link)
* restpeace (Image link)
* affectbaby (Image link)
* trash (Image link)
* welcomebanner (background, avatar, title, subtitle, textcolor)
* boostercard(Image link)
* balancecard(background, avatar, title, top, bottom, textcolor)

Quota:
------
Due to recent spamming incidents, quotas were added to stop the API from going down. The free tier is below.

**Default free tier**
* 1 request per second
* 50 requests per hour
* 250 requests per day

If you need more requests per day, contact French Noodles#6046 on Discord or click [here](https://discord.gg/hWjRaxfu5V) to join the official server.

Links:
------

* [My website](https://frenchnoodles.xyz)
* [Noodles API](www.frenchnoodles.xyz/api)
* [Endpoint list](https://www.frenchnoodles.xyz/api/endpoints)
* [Support server invite](https://discord.gg/hWjRaxfu5V)