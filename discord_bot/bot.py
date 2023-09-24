import discord
import responses
import waifu

async def send_message(message, userMessage, isPrivate):
    try:
        response = responses.handleResponse(userMessage)
        if response:  # Check if response is not empty
            # print(response)
            if response == "encare":
                await message.channel.send(file=discord.File('./midia/encare.jpg'))
            
            elif response == "uwu":
                await message.channel.send(file=discord.File('./midia/uwu.jpg'))
                
            elif response == "analise":
                await message.channel.send(file=discord.File('./midia/analise.jpg'))
            
            elif response == "waifu":
                await message.channel.send(waifu.getWaifu("waifu"))
                
            elif response == "waifu_maid":
                await message.channel.send(waifu.getWaifu("maid"))
                
            elif response == "waifu_uniform":
                await message.channel.send(waifu.getWaifu("uniform"))
                
            
            
            
            
            else:
                await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def runDiscordBot():
    
    # substitute the token with your own
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    
    
    
    @client.event
    async def on_ready():
        print(f"{client.user} has connected to Discord!")
        
        
    @client.event
    async def on_message(message):
        # print("Message received:", message.content)
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)
        
        # print(f"{username}: {user_message} ({channel})")
        
        if user_message.startswith("?"):
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)
        
        
    client.run(TOKEN)


        
        
    