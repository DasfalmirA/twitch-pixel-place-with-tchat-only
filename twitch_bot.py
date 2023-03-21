from twitchio.ext import commands

class TwitchBot(commands.Bot):
    def __init__(self, screen):
        self.screen = screen
        super().__init__(token=token, prefix='!', initial_channels=[channel_name])

    # Event handler for when the bot is ready
    async def event_ready(self):
        print(f'Logged in as | {self.nick} id : {self.user_id}')

    # Event handler for processing chat messages
    async def event_message(self, message):
        if message.echo:
            return
        asyncio.create_task(process_messages(message.content, self.screen))
        await self.handle_commands(message)

    # Command for explaining pixel usage
    @commands.command()
    async def pixel(self, ctx: commands.Context):
        await ctx.send("Ex: #FFFFFF;11;17 -> color_hex;x position;y position"
                       " 1 message : 1 pixel ; x0 y0 = top left pixel")
