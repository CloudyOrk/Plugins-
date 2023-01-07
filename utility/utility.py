import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import revChatGPT
import selenium
import undetected_chromedriver as uc
from revChatGPT.ChatGPT import Chatbot
import random
import asyncio
import time
import os

class UtilityCommands(commands.Cog):
    """Fun commands for members to use!!"""
    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.plugin_db.get_partition(self)
     

    @checks.has_permissions(PermissionLevel.MODERATOR)
    @commands.command()
    async def ranklog(self, ctx, member: discord.Member, gamertag = None, purchase = None , amount = None):
        """
        logs smp ranks
        """
        if member == None:
            await ctx.send_help(ctx.command)
        channel = member.guild.get_channel(960482007379497040) 
        embed = discord.Embed(title="Rank Purchase",
                color=self.bot.main_color,
                description =(
                    f"Discord Tag : {member.mention}\n"
                     f"Discord User ID : {member.id}\n"
                     f"Gamer Tag : {gamertag}\n"
                     f"Amount : {amount}\n"
                     f"Purchase type : {purchase}\n")
                )
        embed.set_footer(text="Utility Plugin v1.10")

        await channel.send(embed=embed) 
        amethyst = "amethyst" 
        ruby = "ruby"
        obsidian = "obsidian"
        carneline = "carneline"
        epidote = "epidote"
        amazonite = "amazonite"
        smprank = member.guild.get_role(1003196550220099654)       
        if purchase == amethyst.lower():                 
            purchase = member.guild.get_role(1034474426902794321)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == ruby.lower():                 
            purchase = member.guild.get_role(1034474078754570353)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == obsidian.lower():                 
            purchase = member.guild.get_role(1034474068998631454)
            await member.add_roles(purchase)
            await member.add_roles(smprank)            
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)            
        elif purchase == epidote.lower():                 
            purchase = member.guild.get_role(1034474059645329481)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == carneline.lower():                 
            purchase = member.guild.get_role(1034473986211467271)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)
        elif purchase == amazonite.lower():                 
            purchase = member.guild.get_role(1034473906863607889)
            await member.add_roles(purchase)
            await member.add_roles(smprank)
            embed = discord.Embed(
                    description = (f" Successfully added {purchase.mention} to {member.mention} for 30 days\n"))
            embed2 = discord.Embed(
                     description = (f" Successfully added {smprank.mention} to {member.mention} for 30days\n"))
            await channel.send(embed=embed)
            await channel.send(embed=embed2)
            await asyncio.sleep(2592000)
            await member.remove_roles(purchase)
            await member.remove_roles(smprank)                  
        else:
            embed = discord.Embed(
                    description = (
                       f"Couldn’t add roles to {member.mention} due to incorrect log format!\n"
                       f"Please give them roles manually"))
            await channel.send(embed=embed)
     
    @checks.has_permissions(PermissionLevel.MODERATOR)       
    @commands.command()
    async def say2(self, ctx, *, message):
        """ModMail says what you want it to say."""
        await ctx.message.delete()
        await ctx.send(message.replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere"))


    @checks.has_permissions(PermissionLevel.SUPPORTER)
    @commands.command()
    async def userid(self, ctx, member: discord.Member = None):
        thread = ctx.thread   
        if member:
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await asyncio.sleep(15)
            await ctx.message.delete()
        elif thread == None:
            member = ctx.author
            await ctx.send(f"{member.mention}'s ID is {member.id}",delete_after=15)
            await ctx.message.delete()
        else:
            member = thread.recipient
            await ctx.message.delete()
            await ctx.send(f"{member.mention}'s ID is {member.id}")

    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def ip(self, ctx, member:discord.Member = None):
        """
        IP address for Blackclue's SMP server
        """
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f"**Port :** 19132\n"
                       f"**Java IP :** java.blackclue.in"))
            await ctx.send(f"{ctx.author.mention}", embed=embed, delete_after=60)
        else:
           embed = discord.Embed(
               title = "Surviving Sheep SMP IP",
               color=self.bot.error_color,
               description = (f"**Bedrock IP :** play.blackclue.in\n"
                       f" **Port :** 19132\n"
                       f" **Java IP :** java.blackclue.in"))
           await ctx.send(f"{member.mention}", embed=embed ,delete_after=60)
        await ctx.message.delete()
 
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command()
    async def vote(self, ctx, member:discord.Member=None):
        if member == None:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{ctx.author.mention}\n", embed=embed, delete_after=60)
        else:
            embed = discord.Embed(
               title = "Surviving Sheep SMP Vote Link",
               color = self.bot.error_color,
               description = (f"[Click Here](https://minecraftpocket-servers.com/server/119868/vote/) to vote for smp server!"))
            await ctx.send(f"{member.mention}\n", embed=embed, delete_after=60)
        await ctx.message.delete()

    @commands.command()
    async def nuke(self, message):
        if message.author.id == 667378631336525824:
            await message.send("are you sure you want to nuke this server?")
            time.sleep(3)
            await message.send("nuking this server in 5 seconds")
            time.sleep(5)
            await message.send("deleting channels and roles")
        else:
            await message.send("Lol")
 
    @commands.command(aliases=['ask','chat'])
    async def gpt(self, ctx: commands.context, *, argument):
        chatbot = Chatbot({"session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..eaZsQoy30YPKXQyt.s4xuGTb-QqQxdfeSYw6tpGXfh05tvj-AHdyjoHVd43HqxKLUWDeklEVW3bHCzbcu4N-SxcaQV8wZ08HFBfcSwDT3TPu97ik2WL4dpszyaM7SDXlpx6CUo0Nk5bghq9Ie8bLJ3cIvPUVF4ZSnWjdDyx73NrPvOpMOA2PTKbag7zFpu2krTBKbqXwyrKdyqww-JwfZcoAmw_1laUJKp8dPvukXvGPu__FrPtNJ0BBI9JPuRtz8X5pV3FReO7Rh60B7-UEWkGvFJRctEEkfLTvC9l_62YXhPPYfGgarG_ZJotvGNbBIXMbpniaWy3SfwWnQ8paxGQWbEyarM9RzwSyGusSUp7SP1XW2eVUS5TFbNThs2w2Hwdn0ipUxpNyop6rJQh3qyeNHGS91ezvJEYISK1sh34H64mTCc_OagDjU6FNbFm_NrlJ3skeUE4juwa6LsnzyA4jCB5xtBy8lXfLH5IgtvIUBqXXl5mz25ZotmqF7yMi8Z0XnE5ixXAC_tr3L-FsPi1rsTzpwCiCgw3MFVq9Q5KnlQNN0pFJ_qXp53-1VyodZTWi8RGNi95a7GLZ_D_Z9N79D9zJvBlQdCTOguhH4fm51xC3bhEnM1e6Igebp2MWOe01DyVKt06nYMrp7mM67wuQhwnPwtIJIc7P1Pwho5OCRdwEAm-yuqktmYhY8J5-vkV1wohv13qIu01h1l6-uouMr13I-nVRmG4yrqzsArQncsdkERP4TrWcI0_xJBeLngDuxOvGCVt2IcvE8MDBMehUSc--hZH61_wrFPJOEv7M5NsPVCr0MrzeaX9TodjUJaiP9WhjQnHzXXY7ZUmuf0sgY8L6qZCU15l0qFn87TuYnXWRIxsG7_rRffm1T71PNMfbW5zXIWB8lGF835g0V9Z3GHSASdehBCkExQl3UzZg3AZaHiKNpT9KZ3rfWFXHQKkwfqK7CUz4ay8G6jYwOm-t5cCo7lDMdlfS9JiBoDy_M4G335V9YBGqEotJAb2T6z4JLW4oh92iupBiMTyQD8fVI9qqSMOi5to_WAWH8cIQRw7fnTKScRbLU74SMEBmRkfwL1gB4cA7oE4GNv_2TccxejNJ4lOUXeQQUS2bom_FpybonTcA6X6pGdzbsWW_y54XtByHQCn_DFqEkQlN6Q43V7SkSEo0sGWrK0-wwh1MI7rNuTwZTXNKTSo4TtVG0p9EEvlL_uZcNkayfktvS_892AtAtTVP74lupUxH7oP65JgkV3XJqY12UIflL4bVpJuyE3tZOonRsiqMQjLwb2akfiklx24s0jJgFSGHh3NZqfyqACptMX9k7geeztXBjxXqeQAwf8qzco0ktgtqPMqrorQSvyChlF702zk578-GSv_EvjOEhD_h3UAfbvWHwzryN87gaQJHJCqGEToZGjr_Yv4Mqk8Rn5RB0m5sdTzkoqwaSshUzdd1Wxxxq25OwInalXiMagDaFzzA0HAmIltcYTa7Ndar7YVvbdLX65EZuQXRjxbG_eaIzi-BAkWZC6n9ZPwHJ4nrFC9GEyL1n_esR_grtSiPgAwxby0Z_Ofti6muYcn8oC8ticEGlVt8saMTn1HnIGtBIeArcfi4xJ_DNv-rMfIH5-J5W_3_XnJmMwOrW6UkUI_s7grZ31GkcPcJy2SWxrbOk81ZkvBCTcrZV0hgCgmr3WmPfJMNwE6crejB3n0DycBKIdnUr3RkWv_zbZDZq_rIF-qZjn050YuDmhjsroK4kPfXaCPh5o0poGNayxGgxA5t1xGsHxW4n1neCORQenq3UpWQ5uQ5RZuB0LU6JAtJ2aLNl2wgit-_SliTQu1_9E9cAJr4CqFsTE2SnnZKUO9J5XGd9DlCQlLVEX54E-rBM7eavxeB9V5yzihQnjg9ZYedT5Ml3aojGNjYKAv4NOGW2H22fkpGlQ3SpEF7EF5rHVTHZletjHWRJe6C2mXmdQVKDi-qT-odwZ-KiaF4aHq6L-8jY7jqtIF_yD152xLuiCaemWeL8iyGl6XMqh0FFLjlB2zyF5ETRjH6U4BSfxCYHL_RaUWF98vCeN65c3lzkbViQ_jRKkWU8F1zPMfcYMgKzB1yE3ARRWyoOodiJ4PGFg1YTqhorhrj0UOUVNTROmJBOBAxdh3vmWX61FyZIBn7guNxsPhFOcJlx8k_MVkS65VBJc1HdzZ9Gsf1euMlIprpLrlKlQgsBS1XDJ7cWy409SvNsgNrQ6m5S2KFuPdxgCtCRJkZifym9aesRHpMhYJVj6hH0gQtbkjz-YeuY2MNx5-xN7wTNcd821gHUOcA.TfeIWkD3EUkaBB1hGPlztQ"}, conversation_id=None, parent_id=None)
        response = chatbot.ask(argument, conversation_id=None, parent_id=None) 
        await ctx.reply(response['message'])

    @checks.has_permissions(PermissionLevel.OWNER)
    @commands.group()
    async def settings(self, ctx):
        """
        Contains subcommands
        |_ show ( shows the settings )
        |_ channel ( sets the channel )
        |_ chat ( sets the Active Chat role )
        |_ voice ( sets the Active Voice role )
        |_ clear ( clears the set roles and channel)
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @settings.command(name="show")
    async def show_settings(self, ctx, *, setting: str):
        """
        |_ channel ( shows the stored channel value )
        |_ chat ( shows the stored role value )
        |_ voice ( shows the stored role value )
        |_ all ( shows all the stored value ) 
        """
        if setting == None:
            await ctx.send_help(ctx.command)
        doc = self.db.find_one()
        elif doc:
            channel_id = doc.get("channel_id")
            chat_role_id = doc.get("chat_role_id")
            voice_role_id = doc.get("voice_role_id")
            channel = self.get_channel(channel_id)
            chat_role = discord.utils.get(ctx.guild.roles, id=chat_role_id)
            voice_role = discord.utils.get(ctx.guild.roles, id=voice_role_id)
            if setting == "channel":
                await ctx.send(f"Channel: {channel.mention}")
            elif setting == "chat":
                await ctx.send(f"Chat role: {chat_role.mention}")
            elif setting == "voice":
                await ctx.send(f"Voice role: {voice_role.mention}")
            elif setting == "all":
                await ctx.send(f"Channel: {channel.mention}\nChat role: {chat_role.mention}\nVoice role: {voice_role.mention}")
        else:
            await ctx.send("Roles and channel have not been set. Use the `settings` command to set them.")

    @settings.command(name="channel")
    async def settings_channel(self, ctx, channel: discord.TextChannel=None):
        """
        Stores a channel where embed is to be sent
        """
        if channel == None:
            await ctx.send_help(ctx.command)
        self.db.find_one_and_update({"_id": "config"}, {"$set": {"channel_id": channel.id}})
        await ctx.send(f"Channel set to {channel.mention}.")

    @settings.command(name="chat")
    async def settings_chat(self, ctx, role: discord.Role):
        self.db.find_one_and_update({"_id": "config"}, {"$set": {"chat_role_id": role.id}})
        await ctx.send(f"Chat role set to {role.mention}.")

    @settings.command(name="voice")
    async def settings_voice(self, ctx, role: discord.Role):
        self.db.find_one_and_update({"_id": "config"}, {"$set": {"voice_role_id": role.id}})
        await ctx.send(f"Voice role set to {role.mention}.")

    @settings.command(name="clear")
    async def clear_settings(self, ctx, *, setting: str):
        """
        |_ channel ( clears the stored channel value )
        |_ chat ( clears the stored role value )
        |_ voice ( clears the stored role value )
        |_ all ( clears all the stored value )
        """
        if setting == None:
            await ctx.send_help(ctx.command)
        if setting == "channel":
            self.db.find_one_and_update({"_id": "config"}, {"$unset": {"channel_id": ""}})
            await ctx.send("Channel cleared.")
        elif setting == "chat":
            self.db.find_one_and_update({"_id": "config"}, {"$unset": {"chat_role_id": ""}})
            await ctx.send("Chat role cleared.")
        elif setting == "voice":
            self.db.find_one_and_update({"_id": "config"}, {"$unset": {"voice_role_id": ""}})
            await ctx.send("Voice role cleared.")
        elif setting == "all":
            self.db.find_one_and_update({"_id": "config"}, {"$unset": {"channel_id": "", "chat_role_id": "", "voice_role_id": ""}})
            await ctx.send("All roles and the channel cleared.")

    @commands.command()
    async def active_members(self, ctx, *, args):
        # Split the arguments into "chat" and "voice" groups
        chat_members, voice_members = [], []
        current_group = None
        for arg in args.split():
            if arg == "--chat":
                current_group = chat_members
            elif arg == "--voice":
                current_group = voice_members
            elif arg.startswith("@"):
                current_group.append(arg)

        # Get the roles and channel from the database
        doc = self.db.find_one()
        if not doc:
            return await ctx.send("Roles and channel have not been set. Use the `settings` command to set them.")
        chat_role_id = doc.get("chat_role_id")
        voice_role_id = doc.get("voice_role_id")
        channel_id = doc.get("channel_id")

        # Add the roles to the members
        for member in chat_members:
            user = await commands.UserConverter().convert(ctx, member)
            role = discord.utils.get(ctx.guild.roles, id=chat_role_id)
            if role:
                await user.add_roles(role, reason="Active chat member")
        for member in voice_members:
            user = await commands.UserConverter().convert(ctx, member)
            role = discord.utils.get(ctx.guild.roles, id=voice_role_id)
            if role:
                await user.add_roles(role, reason="Active voice member")

        # Create the embed message
        active_chat_members = "\n".join(chat_members)
        active_voice_members = "\n".join(voice_members)
        description = (f"**Active Chat Members:**\n{active_chat_members}\n\n"
                       f"**Active Voice Members:**\n{active_voice_members}\n\n"
                        "Congratulations on being selected as an active member! As an active member, you are expected to be active and engaging in our chat and voice channels. We encourage you to participate in discussions and contribute to the community. Thank you for being an active member!")
        embed = discord.Embed(title="Active Members", description=description, color=0x00FF00)

        # Send the embed message to the channel
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            await ctx.send("Could not find specified channel.")

async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
