import json
import discord
from discord.ext import commands

with open('config.json') as e:
    infos = json.load  (e)
    TOKEN = infos['token']
    prefixo = infos['prefix']
    owner_id = infos['owner_id']


Client = commands.Bot(command_prefix=prefixo, intents=discord.Intents.all())
Client.remove_command("help")


    #Eventos
  
#Menssagem de inicio do bot
@Client.event
async def on_ready():
    print(f'\n________________________________'
          f'\nOnline! :D!'
          f'\nID: {Client.user.id}'
          f'\nNome: {Client.user}'
          f'\nAuthor: (Seu nome aqui)'  
          f'\n________________________________')
          
    #Commands
    
@Client.command()
asynd def print(ctx):
  await ctx.send("Olá, Mundo!")


Client.run(TOKEN)
