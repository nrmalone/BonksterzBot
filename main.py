from twitchio.ext import commands
import credentials

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=credentials.oauthToken, prefix='!', initial_channels=credentials.twitchChannel)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        
        print(message.content)
        await self.handle_commands(message)

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'Type ![command]\nCommands:\nhelp')

bot = Bot()
bot.run()