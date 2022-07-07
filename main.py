from twitchio.ext import commands
import credentials
import random

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
        await ctx.send(f'Type ![command]\nCommands: bwl, charity, coinflip, help, ihatealadeen, josh, putafingerdown, toxic')

    @commands.command()
    async def coinflip(self, ctx: commands.Context):
        coin = random.randint(0,1)
        if coin == 0:
            await ctx.send(f'Heads!')
        if coin == 1:
            await ctx.send(f'Tails!')

    @commands.command()
    async def putafingerdown(self, ctx: commands.Context):
        coin = random.randint(0,1)
        if coin == 0:
            await ctx.send(f'if you can squirt PogChamp')
        if coin == 1:
            await ctx.send(f'if you can queef in my face StinkyCheese')

    @commands.command()
    async def toxic(self, ctx: commands.Context):
        randomResponse = random.randint(0,4)
        match randomResponse:
            case 0:
                await ctx.send(f'{ctx.author.name} looks like a fish')
            case 1:
                await ctx.send(f'{ctx.author.name} got a big ass forehead. Big forehead having ass')
            case 2:
                await ctx.send(f'{ctx.author.name} is bouncing on their thumb rn')
            case 3:
                await ctx.send(f'{ctx.author.name} gets no bitches ')
            case 4:
                await ctx.send(f'I got nothing to say to you {ctx.author.name}. Just look in the mirror')

    @commands.command()
    async def charity(self, ctx: commands.Context):
        await ctx.send(f'This month\'s charity is WRRAP; https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=JRWDB7QGEWH3U&source=url')
    
    @commands.command()
    async def josh(self, ctx: commands.Context):
        await ctx.send(f'BigPhish')
    
    @commands.command()
    async def ihatealadeen(self, ctx: commands.Context):
        await ctx.send(f'you mad? LUL')

    @commands.command()
    async def bwl(self, ctx: commands.Context):
        await ctx.send(f'Check out the BWL bracket & predict here: https://challonge.com/687so9b3/')

bot = Bot()
bot.run()