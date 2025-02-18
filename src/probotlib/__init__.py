import discord
import math
import datetime

class Transfer:

    def __init__(self, owner_id, probot_id, amount, server_id):
        self.owner_id = owner_id
        self.probot_id = probot_id
        self.amount = amount
        self.server_id = server_id
        
    def trans_embed(self, bot):
        try:
            self.bot = bot
            self.mention = f"<@!{self.owner_id}>"
            self.guild = bot.get_guild(self.server_id)
            tax_price = math.floor(self.amount * 20 / 19 + 1)
            self.commad = f"c {self.owner_id} {tax_price}"
            embed = discord.Embed(title=f"يرجى تسليم المبلغ إلى {self.mention}", description=f"```txt\n{self.commad}\n```", color=000000, timestamp=datetime.datetime.utcnow())
            if self.guild and self.guild.icon:
                embed.set_author(name=f"{self.guild.name} transfer", icon_url=self.guild.icon)
            else:
                embed.set_author(name=f"{self.guild.name} transfer")
            embed.set_footer(text=self.guild.name)
            return embed
        except Exception as e:
            return e
        
    async def trans_amount(self, ctx):
        
        try:
            user = getattr(ctx, 'user') or getattr(ctx, 'author')
            await self.bot.wait_for(
                "message",
                timeout=15,
                check=lambda m: (
                    m.author == user and 
                    m.channel == ctx.channel and 
                    m.content.lower() == self.commad
                )
            )
        except:
            return False
        
        try:
            confirm = f":moneybag: | {user.name}, has transferred `${self.amount}` to {self.mention}"
            await self.bot.wait_for(
                "message", 
                timeout=15, 
                check=lambda m : (
                    m.author.id == self.probot_id and 
                    m.channel == ctx.channel and 
                    confirm in m.content
                )
            )
            return True
        except:
            return False
