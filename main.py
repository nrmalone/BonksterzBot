from twitchio.ext import commands
import credentials
import random
import mushroom

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
        await ctx.send(f'Type ![command]\nCommands: aladeen, bwl, charity, coinflip, discord, help, josh, mushroom, steam')

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
        match coin:
            case 0:
                await ctx.send(f'Heads!')
            case 1:
                await ctx.send(f'Tails!')
    
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f'https://discord.gg/5E79jj9uSh')

    @commands.command()
    async def josh(self, ctx: commands.Context):
        await ctx.send(f'BigPhish BigPhish BigPhish BigPhish')

    @commands.command()
    async def mushroom(self, ctx: commands.Context):
        await ctx.send(f'Your random mushroom is: ' + mushroom.getMushroom())

    @commands.command()
    async def steam(self, ctx: commands.Context):
        await ctx.send(f'https://steamcommunity.com/id/SergeantLeftHand/')
        
bot = Bot()
bot.run()