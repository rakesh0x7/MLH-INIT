import discord
import random
TOKEN=" "

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message} ({channel})')

    if message.author== client.user:
        return 
    
    if message.channel == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f'hello {username} !')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'see u later {username} !')
            return
        elif user_message.lower() == "init":
            await message.channel.send(f'init 🐬 {username} !')
            return

    if user_message.lower() == "!anywhere":
         await message.channel.send("this can be used anywhere")
         return  


client.run(TOKEN)
