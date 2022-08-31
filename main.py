from twitchio.ext import commands
import credentials
import random
import mushroom
import tkinter as tk

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=credentials.oauthToken, prefix='!', initial_channels=credentials.twitchChannels)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        
        #print(message.content)
        await self.handle_commands(message)

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'Type ![command]\nCommands: aladeen, bwl, charity, coinflip, discord, domserum, help, josh, mushroom, russianroulette, steam')

    @commands.command()
    async def aladeen(self, ctx: commands.Context):
        await ctx.send(f'you mad? LUL')

    @commands.command()
    async def bwl(self, ctx: commands.Context):
        await ctx.send(f'Check out the BWL bracket & predict here: https://challonge.com/687so9b3/')

    @commands.command()
    async def charity(self, ctx: commands.Context):
        await ctx.send(f'This month\'s charity is WRRAP; https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=JRWDB7QGEWH3U&source=url')

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        coin = random.randint(0,1)
        if (coin == 0):
            await ctx.send(f'Heads!')
            '''case 0:
                await ctx.send(f'Heads!')
            case 1:
                await ctx.send(f'Tails!')'''
        if (coin == 1):
            await ctx.send(f'Tails!')
    
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f'https://discord.gg/5E79jj9uSh')
    
    @commands.command()
    async def domserum(self, ctx: commands.Context):
        await ctx.send(f'🥛🥛🥛🥛🥛')

    @commands.command()
    async def josh(self, ctx: commands.Context):
        await ctx.send(f'BigPhish BigPhish BigPhish BigPhish')

    @commands.command()
    async def mushroom(self, ctx: commands.Context):
        await ctx.send(f'Your random mushroom is: ' + mushroom.getMushroom())

    @commands.command()
    async def russianroulette(self, ctx: commands.Context):
        userRoll = random.randint(1,6)
        bullet = random.randint(1,6)
        if userRoll != bullet:
            await ctx.send(f'🔫❌ you got lucky this time {ctx.author.name}')
        elif userRoll == bullet:
            await ctx.send(f'🔫💀 nice rng 5head {ctx.author.name}')
            await ctx.send(f'/timeout @{ctx.author.name} 1s russian roulette')

    @commands.command()
    async def steam(self, ctx: commands.Context):
        await ctx.send(f'https://steamcommunity.com/id/SergeantLeftHand/')

def startBot():
    if inputText.get() == credentials.botPassword:
        labelText.set("Correct password, bot is starting...")
        inputText.pack_forget()
        startButton.pack_forget()

        stopButton = tk.Button(frame, text="Stop Bot", command = stopBot)
        stopButton.configure(bg='#6c4a7e',fg='#ecebe1')
        stopButton.pack(pady=6,padx=6)

        bot = Bot()
        bot.run()
    else:
        labelText.set("Incorrect password, try again")

def stopBot():
    exit()

frame = tk.Tk()
frame.title("BonksterzBot")
frame.configure(bg='#383838')
frame.resizable(False,False)

labelText = tk.StringVar()
labelText.set("What's the secret password?")

inputLabel = tk.Label(frame, textvariable= labelText)
inputLabel.configure(bg='#383838',fg='#ecebe1')
inputLabel.pack(pady=3)

inputText = tk.Entry(frame, show="\u2022", width=17)
inputText.configure(bg='#c6b3d0',fg='#383838')
inputText.pack(pady=3)

startButton = tk.Button(frame,text="Start Bot", command = startBot)
startButton.configure(bg='#6c4a7e', fg='#ecebe1')
startButton.pack(pady=6,padx=6)

frame.protocol("WM_DELETE_WINDOW", stopBot)
frame.mainloop()