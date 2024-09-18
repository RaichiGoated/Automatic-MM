import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord import app_commands
from datetime import datetime
from datetime import timedelta
import asyncio
from itertools import cycle
import os
import re
import emoji, random
import requests

BLOCKCHAIR_API_URL  = 'https://api.blockchair.com/litecoin/dashboards/address/'

# Was my first fully bot code ever

client = commands.Bot(command_prefix="*", intents = discord.Intents.all())

class welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

bot = client



@client.event
async def on_ready():
    global my_view_instance
    print("The bot is ready")
    print("----------------")

    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} command(s)")
        print("-------------------")
    except Exception as e:
        print(e)

    RepeatTicketChannelsend.start()
    channel_id = 1208501508325244978 
    channel = client.get_channel(channel_id)

    if channel:
        try:
            await channel.purge()
            embed = discord.Embed(
            title=f"Ticket Rules",
            description=f"idk",
            color=discord.Color.from_rgb(255, 0, 0)
                )
            my_view_instance = Automaticmmtestbrrrr()
            await channel.send(embed=embed, view=my_view_instance)
        except Exception as e:
            print(f"Error while doing automatic mm embed: {e}")
    else:
        print(f"channel with ID {channel_id} not found")






# member joins
@client.event
async def on_member_join(member):
    channel = client.get_channel(1187341048494690304)
    embed = discord.Embed(
        title = "Welcome to raichi's Middle Man Service.",
        description=f"{member.mention} has joined the Server. \n\n"
            f"{len(member.guild.members)} Members",
        color=discord.Color.dark_red())
       
    embed.set_thumbnail(url="https://i.pinimg.com/736x/ff/0a/0d/ff0a0d2e6fb080ba6edc5f8b0eb5c285.jpg")
    embed.set_footer(text=f'User ID: {member.id}')

    await channel.send(embed=embed)

# member leaves
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1199097000247971851)
    embed = discord.Embed(
        title = "User has left the server",
        description = f"{member.mention} has left the server. \n\n"
            f"{len(member.guild.members)} Members.",
        color=discord.Color.dark_red())
    
    embed.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")
    embed.set_footer(text=f"User ID: {member.id}")

    await channel.send(embed=embed)

# mm rules
@client.command()
@commands.has_permissions(ban_members=True)
async def GetMMRules(ctx):
    if (ctx):
        channel = client.get_channel(1199397121225412811)
        embed = discord.Embed(
            title = "raichi's Middle Man Rules",
            description = f"1. Do not mass ping Middle Mans/Staff. We have the rights to mm a Ticket when we want. \n"
                f"2. When something goes wrong in a Ticket. Please ping raichi. \n"
                f"3. Dont open tickets for any other stuff then mming. If you do you will be getting warned. \n"
                f"4. Use the correct Buttons for the price of your Trade \n"
                f"5. If the Ticket didn't start and you are Ghosting us the Ticket will be closed! \n"
                f"6. After Ticket is done you have 24 Hours to vouch. If not you will get MM Ban role",

            color = discord.Color.from_rgb(255,0,0))
        
        embed.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")

        await channel.send(embed=embed)

# rules
@client.command()
async def GetRules(ctx):
    if (ctx):
        channel = client.get_channel(1199397121225412811)
        embed = discord.Embed(
            title="raichi's Middle Man Rules",
            description=f"No Hard R. \n"
                f"The N word is allowed just not the Hard r"
                
        )
    await channel.send(embed=embed)

    
# kick
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    if ctx.author.guild_permissions.kick_members:
        if ctx.author.top_role > user.top_role:
            if ctx.author == user:
                kickfail = discord.Embed(
                    title=f"kick of {user.name} failed!",
                    description=f"{ctx.author.mention}, you cannot kick yourself.",
                    color=discord.Color.red()
                )
                await ctx.send(embed=kickfail)
            else:
                await user.kick(reason=reason)
                embed1 = discord.Embed(
                    title="kick Command",
                    description=f"{user.mention} has been kicked for the reason: {reason}",
                    color=discord.Color.dark_red()
                )
                embed1.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")
                embed1.set_footer(text=f"User ID: {user.id}")
                await ctx.send(embed=embed1)

                channel = client.get_channel(1199097000247971851)
                embed = discord.Embed(
                    title="User kick",
                    description=f"{user.mention} has been kicked from the server.\n\n"
                                f"Total Members: {len(ctx.guild.members)}",
                    color=discord.Color.from_rgb(255, 0, 0)
                )
                embed.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")
                embed.set_footer(text=f"User ID: {user.id}")
                await channel.send(embed=embed)
        else:
            embed5 = discord.Embed(
                title="Kick command failed",
                description=f"did bro really tried kicking himself or someone tried banning a higher staff.",
                color = discord.Color.from_rgb(255,0,0))
                
            embed5.set_footer(text=f"User ID: {user.id}")
            await ctx.send(embed=embed5)
    else:
        embed4 = discord.Embed(
            title="No kick perms",
            description=f"You dont have Kick perms.",
            color=discord.Color.from_rgb(255,0,0))
        embed4.set_footer(text=f"User ID: {user.id}")
        await ctx.send(embed=embed4)

@client.command()
async def gban(ctx, id: int, *, reason="No reason provided"):
    if ctx.author.guild_permissions.ban_members:
        if reason=="None":
            reason=reason
        
        user = await client.fetch_user(id)
        await ctx.guild.ban(user)
        embed = discord.Embed(
            title="Banned!",
            description=f"<@{id}> was banned for the reason: {reason}",
            color = discord.Color.from_rgb(255,0,0))
        embed.set_footer(text=f"User ID: {id}")
        await ctx.send(embed=embed)

# ban
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    if ctx.author.guild_permissions.ban_members:
        if ctx.author.top_role > user.top_role:
            if ctx.author == user:
                kickfail = discord.Embed(
                    title=f"Ban of {user.name} failed!",
                    description=f"{ctx.author.mention}, you cannot ban yourself.",
                    color=discord.Color.from_rgb(255,0,0)
                )
                await ctx.send(embed=kickfail)
            else:
                await user.ban(reason=reason)
                embed1 = discord.Embed(
                    title="Ban Command",
                    description=f"{user.mention} has been banned for the reason: {reason}",
                    color=discord.Color.from_rgb(255,0,0)
                )
                embed1.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")
                embed1.set_footer(text=f"User ID: {user.id}")
                await ctx.send(embed=embed1)

                channel = client.get_channel(1199097000247971851)
                embed = discord.Embed(
                    title="User Banned",
                    description=f"{user.mention} has been banned from the server.\n\n"
                                f"Total Members: {len(ctx.guild.members)}",
                    color=discord.Color.from_rgb(255, 0, 0)
                )
                embed.set_thumbnail(url="https://i.pinimg.com/originals/3e/d1/a1/3ed1a18fb5e61a449cde6824109c5ef2.jpg")
                embed.set_footer(text=f"User ID: {user.id}")
                await channel.send(embed=embed)
        else:
            # await ctx.send("You don't have the permission to ban users with a higher or equal role.")
            embed5 = discord.Embed(
                title="Ban command failed",
                description=f"did bro really tried banning himself or someone tried banning a higher staff.",
                color = discord.Color.from_rgb(255,0,0))
                
            embed5.set_footer(text=f"User ID: {user.id}")
            await ctx.send(embed=embed5)
            
    else:
        embed4 = discord.Embed(
            title="No ban perms",
            description=f"You dont have ban perms.",
            color=discord.Color.from_rgb(255,0,0))
        embed5.set_footer(text=f"User ID: {user.id}")
        await ctx.send(embed=embed5)





@client.tree.command(name="add_role", description="Give a user a role")
@app_commands.describe(target_user_id="Who should get the Role?", target_role="What role should be given?")
async def gr0(interaction: discord.Interaction, target_user_id: str, target_role: discord.Role):
    try:
        target_user_id = int(target_user_id)
    except ValueError:
        await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
        return

    if interaction.user.guild_permissions.administrator:
     
        target_user = interaction.guild.get_member(target_user_id)
        if target_user:
            if target_role >= interaction.user.top_role:
                embed = discord.Embed(
                    title="You dont have the perms to give yourself a HIGHER Role",
                    color=discord.Color.from_rgb(255, 0, 0)
                )
                embed.set_footer(text=f"User ID of targeted person: {target_user.id}")
                await interaction.response.send_message(embed=embed)
                return

          
            await target_user.add_roles(target_role)

            embed1 = discord.Embed(
                title="Added role",
                description=f"Role {target_role.mention} was given to {target_user.mention}",
                color=discord.Color.from_rgb(255, 0, 0)
            )
            embed1.set_footer(text=f"User ID of targeted person: {target_user.id}")
            await interaction.response.send_message(embed=embed1)
        else:
            await interaction.response.send_message("User not found.")

    else:
        await interaction.response.send_message("You don't have the necessary permissions to use this command.")



@client.tree.command(name="create_your_own_embed", description="With this command you can create your OWN Embed.")
@app_commands.describe(title1="What should be the Title?", description1="What should be the description?", r="What should the R for RGB should be? 0-255", g="What should be the G for RGB should be? 0-255", b="What should the B for RGB should be? 0-255")
async def embed(interaction: discord.Interaction, title1: str, description1: str, r: str, g: str, b: str):

    if int(r) > 255 or int(g) > 255 or int(b) > 255:
        color = discord.Color.from_rgb(255, 0, 0)
    elif int(r) < 0 or int(g) < 0 or int(b) < 0:
        color = discord.Color.from_rgb(255, 0, 0)
    else:
        color = discord.Color.from_rgb(int(r), int(g), int(b))

    embed = discord.Embed(
        title=title1,
        description=description1,
        color=color
    )

    await interaction.response.send_message(embed=embed)


@client.command()
async def gr1(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        if ctx.author.top_role == role.name:
            embed=discord.Embed(
                title="Added role",
                description=f"The role {role.mention} was given to {user.mention}",
                color = discord.Color.from_rgb(255,0,0))
            embed.set_footer(text=f"User ID: {user.id}")
            await ctx.send(embed=embed)
            await user.add_roles(role)
        else:
            await ctx.send("Dont try adding an higher role")
    else:
        embed=discord.Embed(
            title="You dont have perms to do this",
            description=f"emberessing..",
            color = discord.Color.from_rgb(255,0,0))
        embed.set_footer(text=f"User ID: {user.id}")
        await ctx.send(embed=embed)


@client.command()
async def rr(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        if ctx.author.top_role == role.name:
            embed=discord.Embed(
                title="Removed role",
                description=f"The role {role.mention} was removed from {user.mention}",
                color = discord.Color.from_rgb(255,0,0))
            embed.set_footer(text=f"User ID: {user.id}")
            await ctx.send(embed=embed)
            await user.remove_roles(role)
        else:
            await ctx.send("Dont try removing ur role lol")
    else:
        embed=discord.Embed(
            title="You dont have perms to do this",
            description=f"emberessing..",
            color = discord.Color.from_rgb(255,0,0))
        embed.set_footer(text=f"User ID: {user.id}")
        await ctx.send(embed=embed)


@client.command()
async def mute(ctx, member: discord.Member, timelimit, *, reason="None"):
    if ctx.author.guild_permissions.ban_members:
        if ctx.author.top_role > member.top_role:
            if "s" in timelimit:
                gettime = int(timelimit.strip("s"))
                newtime = timedelta(seconds=gettime)
                await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

                embed = discord.Embed(
                    title="Muted!",
                    description=f"{member.mention} was muted/timeoutted for {gettime} seconds",
                    color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"User ID: {member.id}")

                await ctx.send(embed=embed)
            elif "m" in timelimit:
                gettime = int(timelimit.strip("m"))
                newtime = timedelta(minutes=gettime)
                await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

                embed = discord.Embed(
                    title="Muted!",
                    description=f"{member.mention} was muted/timeoutted for {gettime} minutes",
                    color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"User ID: {member.id}")

                await ctx.send(embed=embed)
            elif "h" in timelimit:
                gettime = int(timelimit.strip("h"))
                newtime = timedelta(hours=gettime)
                await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

                embed = discord.Embed(
                    title="Muted!",
                    description=f"{member.mention} was muted/timeoutted for {gettime} hours",
                    color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"User ID: {member.id}")

                await ctx.send(embed=embed)
            elif "d" in timelimit:
                gettime = int(timelimit.strip("d"))
                newtime = timedelta(days=gettime)
                await member.edit(timed_out_until=discord.utils.utcnow() + newtime)

                embed = discord.Embed(
                    title="Muted!",
                    description=f"{member.mention} was muted/timeoutted for {gettime} days",
                    color=discord.Color.from_rgb(255, 0, 0))
                embed.set_footer(text=f"User ID: {member.id}")

                await ctx.send(embed=embed)
            else:
                await ctx.send("Invalid time unit. Please use 's', 'm', 'h', or 'd' in the timelimit.")
        else:
            embed = discord.Embed(
                title="Muting failed!",
                description=f"You cant mute {member.mention} since they are an higher staff.",
                color = discord.Color.from_rgb(255,0,0))
            embed.set_footer(text=f"User ID: {member.id}")
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="No perms",
            description=f"You dont have timeout perms",
            color = discord.Color.from_rgb(255,0,0))
        embed.set_footer(text=f"User ID: {member.id}")
        await ctx.send(embed=embed)

@client.command()
async def unmute(ctx, member: discord.Member):
    
    await member.edit(timed_out_until=discord.utils.utcnow())
    embed = discord.Embed(
        title="Unmmuted!",
        description=f"{member.mention} was unmuted!",
        color = discord.Color.from_rgb(255,0,0))
    embed.set_footer(text=f"User ID: {member.id}")
    await ctx.send(embed=embed)


@client.command()
async def unban(ctx, id: int, *, reason="No reason provided"):
    if reason=="None":
        reason=reason
    
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    embed = discord.Embed(
        title="Unbanned!",
        description=f"<@{id}> was unbanned for the reason: {reason}",
        color = discord.Color.from_rgb(255,0,0))
    embed.set_footer(text=f"User ID: {id}")
    await ctx.send(embed=embed)



class ModalTicketSystem(discord.ui.Modal, title="raichi's Ticket System MM"):
    user_id8 = discord.ui.TextInput(label="User Id of other person", placeholder="The USERID of the other person, make sure u have developer mode on to copy User ID's", required=True, max_length=101, style=discord.TextStyle.short)
    what_will_be_traded = discord.ui.TextInput(label="What will be traded? (INGAME ITEMS ONLY)", placeholder="eg. 100m Gems, 1 Huge (name), 1 Titanic (name)", required=True, max_length=101, style=discord.TextStyle.short)
    for_what_will_be_traded = discord.ui.TextInput(label="Currency and how much?", placeholder="eg. 10$ LTC, 10$ PP", required=True, max_length=101, style=discord.TextStyle.short)

    global opened_tickets
    opened_tickets = {}
    print(opened_tickets)   
    async def on_submit(self, interaction):
        category_id = 1202942245557510195
        category = interaction.guild.get_channel(category_id)
        name = f"ticket-{interaction.user}"

        user_id99 = int(self.user_id8.value)

        member2 = interaction.guild.get_member(user_id99) 
        ingameItems = str(self.what_will_be_traded)
        currencyaa = str(self.for_what_will_be_traded)


        if interaction.user.id in opened_tickets:
            ticket_channel = opened_tickets[interaction.user.id]
            await interaction.response.send_message(f"You already have a ticket opened at {ticket_channel.mention}", ephemeral=True)
        elif interaction.user.id not in opened_tickets:
       
            channel = await category.create_text_channel(name)
            await channel.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True) # interaction user
            await channel.set_permissions(interaction.guild.get_role(1187094626457354360), view_channel = False) # everyone
            opened_tickets[interaction.user.id] = channel 
            await interaction.response.send_message(f"Ticket created at {channel.mention}", ephemeral=True)

            await channel.send(f"Ticket created for {interaction.user.mention}. PLEASE WAIT SOME SECONDS FOR CHANNEL PERMS, ETC...")
            
            await channel.set_permissions(interaction.guild.get_role(1199371978369405079), view_channel = True, send_messages = True, attach_files = True) # raichi bot
            await channel.set_permissions(interaction.guild.get_role(1187339878288080987), view_channel = True, send_messages = True, attach_files = True) # admin
            await channel.set_permissions(interaction.guild.get_role(1187094654269784225), view_channel = True, send_messages = True, attach_files = True) # owner 
            await channel.set_permissions(interaction.guild.get_role(1189602606386008114), view_channel = True, send_messages = True, attach_files = True) # head mm
            await channel.set_permissions(interaction.guild.get_role(1187339949901619240), view_channel = True, send_messages = True, attach_files = True) # middle man
            await channel.set_permissions(interaction.guild.get_role(1189602732462583941), view_channel = True, send_messages = True, attach_files = True) # trial mm
            await channel.set_permissions(interaction.guild.get_role(1187343988735348767), view_channel = True, send_messages = True, attach_files = True) # Bots
            await channel.set_permissions(member2, view_channel=True, send_messages=True, attach_files=True)
            await channel.set_permissions(interaction.guild.default_role, view_channel = False)
            await channel.send(embed=discord.Embed(
                title=f"Ticket created!",
                description=f"user_id: <@{user_id99}>\n"
                            f"Ingame Items: {ingameItems}\n"
                            f"For which Currency?: {currencyaa}",
                color=discord.Color.from_rgb(255,0,0)
                ))
            await channel.send(f"<@{self.user_id8.value}> got added to the ticket.")
            await channel.send(f"<@&1189602606386008114> <@&1187339949901619240> <@&1189602732462583941>")
            await channel.send(f"FOR THE MM's ONLY: use the command '/helpmm' if you need help for specific commands. If you think there is something missing, ping raichi and tell him the problem.")
            await channel.send(f"Be careful if someone is IMPERSONATING a MM. Always check if the MM has a MM role.")
        else:
            await self.ctx.send("You do not have the necessary permissions to create a ticket. If you think this is wrong PING raichi", ephemeral=True)


class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        

    @discord.ui.button(label="Create a mm Ticket ✉️", style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction, button):
        await interaction.response.send_modal(ModalTicketSystem())

@client.tree.command(name="create_ticket", description="ONLY FOR RAICHI WHEN BOT IS UPDATED")
async def ticketcreating(interaction):
    channel = client.get_channel(1187342624013697154)

    if interaction.user.guild_permissions.ban_members:
        embed = discord.Embed(
            title=f"Ticket Rules",
            description=f"**1. Create Ticket **\n"
                            f"  - Click the `Create a mm Ticket ✉️` Button if you need a Middle Man\n"
                        f"**2. After Creating Ticket**\n"
                            f"  - Please wait until a Middle Man is with you. It normally doesn't take much time for a MM to come in the channel. If still no one comes ping a mm.\n"
                        f"**3. Fees**\n"
                            f"  - Under $40 - Free\n"
                            f"  - $40 to $100 - Depends on the MM\n"
                            f"  - $100 to $1000 - Depends on the MM\n"
                            f"  - Anything above $1000 - Depends on the MM\n"
                        f"**4. Info**\n"
                            f"Here at raichi's Middle Man service you are safe. Raichi is a known Middle Man in known servers such as Milk Up and Huge MM. Hes a mm in other small servers too but that isnt important. The MM's here are Trusted too and have lots of vouches. If something goes wrong DM <@1064170243745906688> and explain what was wrong (also if you got scammed by a mm). ",
            color=discord.Color.from_rgb(255, 0, 0)
        )
        my_view_instance = MyView(ctx=interaction)
        await channel.send(embed=embed, view=my_view_instance)
        await interaction.response.send_message("SENT!", ephemeral=True)
    else:
        await interaction.response.send_message("You don't have the required permissions to use this command.")




@client.command()
async def ticket(ctx):
    if ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title=f"Ticket Rules",
            description=f"**1. Create Ticket **\n"
                            f"  - Click the `Create a mm Ticket ✉️` Button if you need a Middle Man\n"
                        f"**2. After Creating Ticket**\n"
                            f"  - Please wait until a Middle Man is with you. It normally doesnt take much time for a MM to come in the channel. If still no one comes ping a mm.\n"
                        f"**3. Fees**\n"
                            f"  - Under $40 - Free\n"
                            f"  - $40 to $100 - Depends on the MM\n"
                            f"  - $100 to $1000 - Depends on the MM\n"
                            f"  - Anything above $1000 - Depends on the MM\n"
                        f"**4. Info**\n"
                            f"Here at raichi's Middle Man service you are safe. Raichi is a known Middle Man in known servers such as Milk Up and Huge MM. Hes a mm in other small servers too but that isnt important. The MM's here are Trusted too and have lots of vouches. If something goes wrong DM <@1064170243745906688> and explain what was wrong (also if you got scammed by a mm). ",
            color=discord.Color.from_rgb(255, 0, 0)
        )
        my_view_instance = MyView(ctx=ctx)
        await ctx.send(embed=embed, view=my_view_instance)
    else:
        pass


class CloseButton(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=None)

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.red)
    async def Close(self, interaction, button):
        
        await interaction.response.send_message(content="Closing now.")
        await interaction.channel.delete()

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.blurple)
    async def Cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.message.delete()
        await interaction.channel.send(content="Canceled deleting Ticket")



@client.tree.command(name="remove_user", description="Use this command on the PERSON who CREATED the TICKET. IMPORTANT!!!!!")
@app_commands.describe(userid="The userid of the person who created the ticket.")
async def removesauser(interaction, userid: str):
    if interaction.user.get_role(1189602732462583941): 
            
        try:
            userid = int(userid)
        except ValueError:
            await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
            return
        

        if userid in opened_tickets:
            del opened_tickets[userid]
            await interaction.response.send_message(f"Ticket for USERID <@{userid}> has been removed.")
        else:
            await interaction.response.send_message("USERID was not found in opened_tickets. Please check if the USERID is correct. If so and it doesn't work, contact raichi")
    if interaction.user.get_role(1187339949901619240): 
            
        try:
            userid = int(userid)
        except ValueError:
            await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
            return
        

        if userid in opened_tickets:
            del opened_tickets[userid]
            await interaction.response.send_message(f"Ticket for USERID <@{userid}> has been removed.")
        else:
            await interaction.response.send_message("USERID was not found in opened_tickets. Please check if the USERID is correct. If so and it doesn't work, contact raichi")
    if interaction.user.get_role(1189602606386008114): 
            
        try:
            userid = int(userid)
        except ValueError:
            await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
            return
        

        if userid in opened_tickets:
            del opened_tickets[userid]
            await interaction.response.send_message(f"Ticket for USERID <@{userid}> has been removed.")
        else:
            await interaction.response.send_message("USERID was not found in opened_tickets. Please check if the USERID is correct. If so and it doesn't work, contact raichi")




async def AM(ctx):


    await ctx.send("Automatic MM :D")
    embed=discord.Embed(
        title="Automatic MM (test)",
        description="Thank you for opening a Ticket. Your Middle Man will be me, a Bot.",
        color=discord.Color.from_rgb(0,0,255)
    )
    await ctx.send(embed=embed)
    embed2=discord.Embed(
        title="How will this work?",
        description="Only Crypto (LTC) transcactions work. I only hold LTC meaning the person with LTC has to send me the LTC. Ill wait than till 3/6 Confirmations and will give you an OK to give the LTC person the stuff. After he approves it the Bot will send the LTC to the other user (including fee's). After that both of you are vouching and the Ticket is done.",
        color=discord.Color.from_rgb(0,0,255)
    )
    await ctx.send(embed=embed2)

    embed3= discord.Embed(
        title="Please click on the Buttons",
        description="What Receiver and Sender is for. \n"
            f"The Button **SENDER** is for the person who has the Crypto (LTC) \n"
            f"The Button **RECEIVER** is for the person who has the other stuff (ps99 gems, ps99 titanic or smth else)",
            color=discord.Color.from_rgb(0,0,255)
    )

    await ctx.send(embed=embed3)
    

class MMbuttonsam(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        global sendervariable
        sendervariable = {}
        global receivervariable
        receivervariable = {}

    @discord.ui.button(label="Sender", style=discord.ButtonStyle.blurple)
    async def sender(self, interaction, button):

    

        if interaction.user.id in sendervariable:
            await interaction.response.send_message(f"{interaction.user.mention} You already claimed sender")

        elif interaction.user.id in receivervariable:
            await interaction.response.send_message(f"{interaction.user.mention} You can't claim sender because you already claimed receiver.")
        
        else:
            channel = interaction.channel
            sendervariable[interaction.user.id] = channel
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send(f"{interaction.user.mention} has claimed sender")
            print(sendervariable)

            

    @discord.ui.button(label="Receiver", style=discord.ButtonStyle.blurple)
    async def receiver(self, interaction, button):

    

        if interaction.user.id in receivervariable:
            await interaction.response.send_message(f"{interaction.user.name} You already claimed receiver")

        elif interaction.user.id in sendervariable:
            await interaction.response.send_message(f"{interaction.user.mention} You cant claim receiver because you already claimed sender.")

        else:
            channel = interaction.channel
            receivervariable[interaction.user.id] = channel
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await interaction.followup.send(f"{interaction.user.mention} has claimed receiver")
            print(receivervariable)

    @discord.ui.button(label="Report a Problem", style=discord.ButtonStyle.grey)
    async def ReportAProblem(self, interaction, button):
    
        class YesImSureClass(discord.ui.View):

            @discord.ui.button(label="Yes I'm sure", style=discord.ButtonStyle.blurple)
            async def YesimSure(self, interaction, button):
                await interaction.response.send_message(f"<@1064170243745906688> user {interaction.user.mention} has a problem.")

        embed = discord.Embed(
            title="Are you sure there is a Problem?",
            description=f"This only pings <@1064170243745906688>. Please, after clicking the `Yes I'm sure` Button, explain to Raichi what the problem is. Maybe you miss clicked or so. Raichi will remove you from the button you clicked on.",
            color=discord.Color.from_rgb(255, 0, 0)
        )
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(embed=embed, view=YesImSureClass())




        
@client.tree.command(name="remove_sender", description="Removes a user who missclicked for Automatic MM. removes him from 'Sender'")
@app_commands.describe(userid="The userid of who should get removed")
async def RemoveSender(interaction, userid: str):
    try:
        userid = int(userid)
    except ValueError:
        await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
        return
    

    if userid in sendervariable:
        del sendervariable[userid]
        await interaction.response.send_message(f"User: <@{userid}> has been removed from sender.")
    else:
        await interaction.response.send_message("USERID was not found in Sender variable. Please check if the USERID is correct. If so and it doesn't work, contact raichi")

    
  
@client.tree.command(name="remove_receiver", description="Removes a user who missclicked for Automatic MM. removes him from 'Receiver'")
@app_commands.describe(userid="The userid of who should get removed")
async def RemoveReceiver(interaction, userid: str):
    try:
        userid = int(userid)
    except ValueError:
        await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
        return
    

    if userid in receivervariable:
        del receivervariable[userid]
        await interaction.response.send_message(f"User: <@{userid}> has been removed from Receiver.")
    else:
        await interaction.response.send_message("USERID was not found in Sender variable. Please check if the USERID is correct. If so and it doesn't work, contact raichi")

                

    

@client.command()
async def test123(ctx):
    await AM(ctx)
    await ctx.send(view=MMbuttonsam())



@client.tree.command(name="helpmm", description="Only for the MM's. Shows all Commands")
async def helpmm(interaction: discord.Interaction):
    if interaction.user.get_role(1189602732462583941):
        embed = discord.Embed(
            title="All Ticket Commands and what they do.",
            description=f"**/add** \n"
                            f"  - Adds a User to the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/remove** \n"
                    f"  - Removes a User from the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/transcript**\n"
                    f"  - If the Ticket is done PLEASE do /transcript, download the file and send the file in <#1187341940858044466>. After that you can close the Ticket. \n"
                f"**/close**\n"
                    f"  - Closes a Ticket. Only close when the Ticket is done or they cancelled the deal.\n"
                f"**/remove_user**\n"
                    f"  - USE THIS TO THE PERSON ON WHO CREATED THE TICKET SO THEY CAN OPEN ONE AGAIN. ONLY USE THIS COMMAND WHEN TICKET IS DONE OR DEAL IS CANCELED!",

            color=discord.Color.from_rgb(255,0,0)

            )
        embed.set_footer(text=f"User ID: {interaction.id}")
        await interaction.response.send_message(embed=embed)
    elif interaction.user.get_role(1187339949901619240):
        embed = discord.Embed(
            title="All Ticket Commands and what they do.",
            description=f"**/add** \n"
                            f"  - Adds a User to the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/remove** \n"
                    f"  - Removes a User from the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/transcript**\n"
                    f"  - If the Ticket is done PLEASE do /transcript, download the file and send the file in <#1187341940858044466>. After that you can close the Ticket. \n"
                f"**/close**\n"
                    f"  - Closes a Ticket. Only close when the Ticket is done or they cancelled the deal.\n"
                f"**/remove_user**\n"
                    f"  - USE THIS TO THE PERSON ON WHO CREATED THE TICKET SO THEY CAN OPEN ONE AGAIN. ONLY USE THIS COMMAND WHEN TICKET IS DONE OR DEAL IS CANCELED!",

            color=discord.Color.from_rgb(255,0,0)

            )
        embed.set_footer(text=f"User ID: {interaction.id}")
        await interaction.response.send_message(embed=embed)
    elif interaction.user.get_role(1189602606386008114):
        embed = discord.Embed(
            title="All Ticket Commands and what they do.",
            description=f"**/add** \n"
                            f"  - Adds a User to the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/remove** \n"
                    f"  - Removes a User from the Ticket. Only USERID works so copy their UserID and paste it in the target_user_id box. \n"
                f"**/transcript**\n"
                    f"  - If the Ticket is done PLEASE do /transcript, download the file and send the file in <#1187341940858044466>. After that you can close the Ticket. \n"
                f"**/close**\n"
                    f"  - Closes a Ticket. Only close when the Ticket is done or they cancelled the deal.\n"
                f"**/remove_user**\n"
                    f"  - USE THIS TO THE PERSON ON WHO CREATED THE TICKET SO THEY CAN OPEN ONE AGAIN. ONLY USE THIS COMMAND WHEN TICKET IS DONE OR DEAL IS CANCELED!",

            color=discord.Color.from_rgb(255,0,0)

            )
        embed.set_footer(text=f"User ID: {interaction.id}")
        await interaction.response.send_message(embed=embed)
    
    else:
        await interaction.response.send_message("You dont have any MM roles.")


@client.tree.command(name="transcript", description="Generates a Transcript for this Channel")
async def transcript(interaction: discord.Interaction):
    if "ticket-" in interaction.channel.name:
        if interaction.user.guild_permissions.ban_members:
            await interaction.response.defer()
            if os.path.exists(f"{interaction.channel.name}.md"):
                pass
            with open(f"{interaction.channel.name}.md", 'a', encoding='utf-8') as f:
                f.write(f"# Transcript of {interaction.channel.name}:\n\n")
                async for message in interaction.channel.history(limit=None, oldest_first=True):
                    created = datetime.strftime(message.created_at, "%m/%d/%Y at %H:%M:%S")
                    
                    if message.attachments:
                        image_links = "\n".join(attachment.url for attachment in message.attachments)
                        f.write(f"{message.author} on {created}: Sent image(s) or Video(s):\n{image_links}\n")
                    else:
                        if message.edited_at:
                            edited = datetime.strftime(message.created_at, "%m/%d/%Y at %H:%M:%S")
                            content = replace_emojis(message.clean_content)
                            f.write(f"{message.author} on {created}: {content} (Edited at {edited})\n")
                        else:
                            content = replace_emojis(message.clean_content)
                            f.write(f"{message.author} on {created}: {content}\n")

                generated = datetime.now().strftime("%m/%d/%Y at %H:%M:%S")
                f.write(f"\n*Generated at {generated} by {client.user}*\nDate Formatting: MM/DD/YY*\n*Time Zone: UTC*")
            with open(f"{interaction.channel.name}.md", 'rb') as f:
                await interaction.followup.send(file=discord.File(f, f"{interaction.channel.name}.md"))
            os.remove(f"{interaction.channel.name}.md")
        else:
            await interaction.response.send_message("You don't have permission to do this.")
    else:
        await interaction.response.send_message("This isn't a ticket!", ephemeral=True)

def replace_emojis(text):
    def replace(match):
        emoji_unicode = match.group()
        try:
            emoji_name = emoji.demojize(emoji_unicode).replace(":", "")
            if emoji_unicode.startswith("<a:"):  # Animated custom emoji
                emoji_unicode = f"\\U{emoji_name.split(':')[2]}"
            elif emoji_unicode.startswith("<:"):  # Regular custom emoji
                emoji_unicode = f"\\U{emoji_name.split(':')[1]}"
            else:
                emoji_unicode = emoji.emojize(f":{emoji_name}:", use_aliases=True)
                emoji_unicode = emoji_unicode.encode('unicode-escape').decode('utf-8')
        except:
            pass
        return emoji_unicode

    return re.sub(r"<a?:[a-zA-Z0-9_]+:[0-9]+>|:[a-zA-Z0-9_]+:", replace, text)

@client.command()
async def Selling(ctx):
    pass


@client.tree.command(name="add", description="Adds a User in a Ticket")
@app_commands.describe(target_user_id="Who should be added? USERID ONLY")
async def add(interaction: discord.Interaction, target_user_id: str):
    try:
        target_user_id = int(target_user_id)
    except ValueError:
        await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
        return
    
    await interaction.channel.set_permissions(interaction.guild.get_member(target_user_id), view_channel = True, send_messages = True, attach_files = True)
    
    embed = discord.Embed(
        title=f"Member has been added",
        description=f"The Member <@{target_user_id}> was added.",
        color = discord.Color.from_rgb(255,0,0)
    )
    embed.set_footer(text=f"User ID: {target_user_id}")
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="remove", description="removes a User in a Ticket")
@app_commands.describe(target_user_id="Who should be removed? USERID ONLY")
async def remove(interaction: discord.Interaction, target_user_id: str):
    try:
        target_user_id = int(target_user_id)
    except ValueError:
        await interaction.response.send_message("Invalid user ID. Please provide a valid number.")
        return
    
    await interaction.channel.set_permissions(interaction.guild.get_member(target_user_id), view_channel = False, send_messages = False, attach_files = False)
    
    embed = discord.Embed(
        title=f"Member has been removed",
        description=f"The Member <@{target_user_id}> was removed.",
        color = discord.Color.from_rgb(255,0,0)
    )
    embed.set_footer(text=f"User ID: {target_user_id}")
    await interaction.response.send_message(embed=embed)



@client.tree.command(name="close", description="Close a Ticket")
async def buttontest(interaction: discord.Interaction):
    if "ticket-" in interaction.channel.name:
        if interaction.user.get_role(1189602732462583941):
            embed = discord.Embed(
                title="Are you sure to close this Ticket?",
                description=f"Please make sure to do **/transcript** and save the file in <#{1187341940858044466}>. If not please do that before closing this ticket.",
                color=discord.Color.from_rgb(255,0,0)
            )
            embed.set_footer(text=f"User ID: {interaction.id}")
            view = CloseButton(interaction.id)
            await interaction.response.send_message(embed=embed, view=view)
        elif interaction.user.get_role(1187339949901619240):
            embed = discord.Embed(
                title="Are you sure to close this Ticket?",
                description=f"Please make sure to do **/transcript** and save the file in <#{1187341940858044466}>. If not please do that before closing this ticket.",
                color=discord.Color.from_rgb(255,0,0)
            )
            embed.set_footer(text=f"User ID: {interaction.id}")
            view = CloseButton(interaction.id)
            await interaction.response.send_message(embed=embed, view=view)
        elif interaction.user.get_role(1189602606386008114):
            embed = discord.Embed(
                title="Are you sure to close this Ticket?",
                description=f"Please make sure to do **/transcript** and save the file in <#{1187341940858044466}>. If not please do that before closing this ticket.",
                color=discord.Color.from_rgb(255,0,0)
            )
            embed.set_footer(text=f"User ID: {interaction.id}")
            view = CloseButton(interaction.id)
            await interaction.response.send_message(embed=embed, view=view)
        else:
            await interaction.response.send_message("You dont have any MM roles.")
    else: 
        await interaction.response.send_message("This is not a Ticket")

    









@client.tree.command(name="echo", description="Copies what you say")
@app_commands.describe(message="What should I say")
async def echo(interaction: discord.Interaction, *, message: str):
    await interaction.response.send_message("SENT", ephemeral=True)
    await interaction.channel.send(message)


@client.command()
async def LTCraichi(ctx):
    if ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title="This is the fee addy. LTC ONLY",
            description=f"```ltc1qgtrmd242lmaxp837mvd2q74rfl5myps0ethzyh``` \n"
                f"make sure to copy all correct!",
            color=discord.Color.from_rgb(255,0,0)
        )
        await ctx.send(embed=embed)
    else:
        pass

@client.command()
async def LTCescanor(ctx):
    if ctx.author.guild_permissions.change_nickname:
        embed = discord.Embed(
            title="This is the fee of escanors addy. LTC ONLY",
            description=f"```LeF2Jn1gMhSa1KvzV7nKTgNRsDJCn5iaBm``` \n"
                f"make sure to copy all correct!",
            color=discord.Color.from_rgb(255,0,0)
        )
        await ctx.send(embed=embed)
    else:
        pass

@client.command()
async def LTCkaiser(ctx):
    if ctx.author.guild_permissions.change_nickname:
        embed = discord.Embed(
            title="This is the fee of kaiser's addy. LTC ONLY",
            description=f"```LfnS6dm82zA3tsww3W3jrqX3cCvTCjY9LE``` \n"
                f"make sure to copy all correct!",
            color=discord.Color.from_rgb(255,0,0)
        )
        await ctx.send(embed=embed)
    else:
        pass



@client.command()
async def SELLING(ctx):
    pass


@client.command()
async def userinticket(ctx):
    await ctx.send(opened_tickets)


class ModalcheckSendersLTCaddy(discord.ui.Modal, title="Sender should write here his LTC Address"):
    LTC_addy_of_sender = discord.ui.TextInput(label="LTC ADDRESS of Sender.", placeholder="LTC address", required=True, max_length=101, style=discord.TextStyle.short)

    async def on_submit(self, interaction):
        if interaction.user.id not in sendervariable:
            await interaction.response.send_message(f"{interaction.user.mention} you are `NOT` the SENDER. If you think this is wrong click the Report Button.")
        else:
            LTC_addy_of_sender = str(self.LTC_addy_of_sender.value)
            await interaction.send_message(embed=discord.Embed(
                title="Sender's LTC Address",
                description=f"{interaction.user.mention}'s LTC address is {LTC_addy_of_sender}",
                color=discord.Color.from_rgb(255,0,0)
            ))

class ModalTest(discord.ui.Modal, title="raichi's Automatic Middle Man Modal"):
    user_id = discord.ui.TextInput(label="User Id of other person", placeholder="The USERID of the other person, make sure u have developer mode on to copy User ID's", required=True, max_length=101, style=discord.TextStyle.short)
    Crypto = discord.ui.TextInput(label="How much LTC in $", placeholder="eg. 40", required=True, max_length=101, style=discord.TextStyle.short)

    async def on_submit(self, interaction):

        global personccreatedticket
        personccreatedticket = interaction.user

        category_id = 1202942245557510195
        category = interaction.guild.get_channel(category_id)
        name = f"ticket-{interaction.user}"

        user_id = int(self.user_id.value) 

        try:
            crypto_amount = float(self.Crypto.value)
        except ValueError:
            await interaction.response.send_message("Please enter a valid number for the Crypto amount.", ephemeral=True)
            return

        global member
        member = interaction.guild.get_member(user_id)

        if member is not None:
            if crypto_amount >= 1001:
                await interaction.response.send_message(f"lmao nice try. If you do want {crypto_amount} Ticket please use raichi as your MM or wait till raichi fixes that you can make above 1001$ tickets.", ephemeral=True)
            else:
                if interaction.user.id in opened_tickets:
                    ticket_channel = opened_tickets[interaction.user.id]
                    await interaction.response.send_message(f"You already have a ticket opened at {ticket_channel.mention}", ephemeral=True)
                else:
                    channel = await category.create_text_channel(name)
                    opened_tickets[interaction.user.id] = channel
                    

                    await channel.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True)
                    await channel.send(f"{interaction.user.mention} has created a Ticket. Please wait for Channel perms, etc...")
                    await channel.set_permissions(member, view_channel=True, send_messages=True, attach_files=True)
                    await channel.set_permissions(interaction.guild.get_role(1187094626457354360), view_channel=False)  # everyone
                    await channel.set_permissions(interaction.guild.get_role(1199371978369405079), view_channel=True, send_messages=True, attach_files=True)  # raichi bot
                    await channel.set_permissions(interaction.guild.get_role(1187339878288080987), view_channel=True, send_messages=True, attach_files=True)  # admin
                    await channel.set_permissions(interaction.guild.get_role(1187094654269784225), view_channel=True, send_messages=True, attach_files=True)  # owner
                    await channel.set_permissions(interaction.guild.get_role(1189602606386008114), view_channel=True, send_messages=True, attach_files=True)  # head mm
                    await channel.set_permissions(interaction.guild.get_role(1187339949901619240), view_channel=True, send_messages=True, attach_files=True)  # middle man
                    await channel.set_permissions(interaction.guild.get_role(1189602732462583941), view_channel=True, send_messages=True, attach_files=True)  # trial mm
                    await channel.set_permissions(interaction.guild.get_role(1187343988735348767), view_channel=True, send_messages=True, attach_files=True)  # Bots

                    embed = discord.Embed(
                        title="AUTOMATIC MM EMBED",
                        color=discord.Color.from_rgb(255, 0, 0)
                    )
                    embed.add_field(name="UserId of other person", value=self.user_id.value)
                    embed.add_field(name="Deal value in $", value=self.Crypto.value)
                    await channel.send(embed=embed)

                    await channel.send(f"<@{self.user_id.value}> got added to the ticket.")

                                
                    await channel.send(embed=discord.Embed(
                        title="Automatic MM (test)",
                        description="Thank you for opening a Ticket. Your Middle Man will be me, a Bot.",
                        color=discord.Color.from_rgb(0,0,255)
                    ))
                    await channel.send(embed=discord.Embed(
                        title="How will this work?",
                        description="Only Crypto (LTC) transcactions work. I only hold LTC meaning the person with LTC has to send me the LTC. Ill wait then till 3/6 Confirmations and will give you an OK to give the LTC person the stuff. After he approves it the Bot will send the LTC to the other user (including fee's). After that both of you are vouching and the Ticket is done.",
                        color=discord.Color.from_rgb(0,0,255)
                    ))
                    await channel.send(embed=discord.Embed(
                        title="Please click on the Buttons",
                        description="What Receiver and Sender is for. \n"
                            f"The Button **SENDER** is for the person who has the Crypto (LTC) \n"
                            f"The Button **RECEIVER** is for the person who has the other stuff (ps99 gems, ps99 titanic or smth else)\n"
                            f"**INFO**: Sometimes the first button click does not work. Just wait some seconds if it says 'Interaction failed please try again' and click the button again.",
                            color=discord.Color.from_rgb(0,0,255)
                    ))
                    await channel.send(view=MMbuttonsam())

                    @tasks.loop(seconds=5)
                    async def loopingtocheckforbothbuttensclaimed():
                        if member.id in receivervariable:
                            if personccreatedticket.id in sendervariable:
                                await channel.send(embed=discord.Embed(
                                    title=f"Sender {personccreatedticket} has to send the LTC to bot now.",
                                    description=f"{personccreatedticket.mention} please sent the LTC ({crypto_amount} $) to `LMqBvtGQniCqdVYAURttTE9NAXxy1q8Wf9`",
                                    color=discord.Color.from_rgb(0,0,255)
                                ))
                                loopingtocheckforbothbuttensclaimed.stop()
                            else:
                                pass

                        elif member.id in sendervariable:
                            if personccreatedticket.id in receivervariable:
                                await channel.send(embed=discord.Embed(
                                    title=f"Sender {member} has to send the LTC to bot now.",
                                    description=f"{member.mention} please sent the LTC ({crypto_amount} $) to `LMqBvtGQniCqdVYAURttTE9NAXxy1q8Wf9`",
                                    color=discord.Color.from_rgb(0,0,255)
                                ))
                                loopingtocheckforbothbuttensclaimed.stop()
                            else:
                                pass


                    loopingtocheckforbothbuttensclaimed.start()
                    
        else:
            await interaction.response.send_message("The User(Id) you wrote is not in the server.", ephemeral=True)

    

class Automaticmmtestbrrrr(discord.ui.View):
    @discord.ui.button(label="Automatic Middle Man Ticket", style=discord.ButtonStyle.blurple)
    async def automatisudhsid(self,interaction,button):
        await interaction.response.send_modal(ModalTest())

@client.command()
async def amt(ctx):
    embed = discord.Embed(
            title=f"Ticket Rules",
            description=f"idk",
            color=discord.Color.from_rgb(255, 0, 0)
        )
    my_view_instance = Automaticmmtestbrrrr()
    await ctx.send(embed=embed, view=my_view_instance)


@client.command()
async def GetCurrentLTCRate(ctx):
    url = "https://rest.coinapi.io/v1/exchangerate/LTC/USD"
    headers= {"X-CoinAPI-Key" : "A598CB21-7EE2-431D-B63E-C39D68CE3697"}
    response = requests.get(url, headers=headers)

    current_rate = response.json()["rate"]

    await ctx.send(current_rate)

@tasks.loop(minutes=5)
async def RepeatTicketChannelsend():

    channel_id = 1187342624013697154 
    channel = client.get_channel(channel_id)

    await channel.purge()
    embed = discord.Embed(
        title=f"Ticket Rules",
        description=f"**1. Create Ticket **\n"
            f"  - Click the `Create a mm Ticket ✉️` Button if you need a Middle Man\n"
                f"**2. After Creating Ticket**\n"
            f"  - Please wait until a Middle Man is with you. It normally doesnt take much time for a MM to come in the channel. If still no one comes ping a mm.\n"
                f"**3. Fees**\n"
                        f"  - Under $40 - Free\n"
                        f"  - $40 to $100 - Depends on the MM\n"
                        f"  - $100 to $1000 - Depends on the MM\n"
                        f"  - Anything above $1000 - Depends on the MM\n"
                f"**4. Info**\n"
                        f"Here at raichi's Middle Man service you are safe. Raichi is a known Middle Man in known servers such as Milk Up and Huge MM. Hes a mm in other small servers too but that isnt important. The MM's here are Trusted too and have lots of vouches. If something goes wrong DM <@1064170243745906688> and explain what was wrong (also if you got scammed by a mm). ",
        color=discord.Color.from_rgb(255, 0, 0)
    )
    my_view_instance = MyView()
    await channel.send(embed=embed, view=my_view_instance)
    await channel.send("If you cannot open a TICKET dm raichi")
    await channel.send("Message is getting deleted every **5** Minutes so that Ticket System works again.")

@client.tree.command(name="guess", description="Guess a number between 1 and 100")
@app_commands.describe(number="The number you want to guess")
async def numbergenerator(interaction, number: int):
    guild = bot.get_guild(interaction.guild_id)
    role = discord.utils.get(guild.roles, name="GuessTheNumberMute")
    
    global member123
    member123 = guild.get_member(interaction.user.id)
    await member123.add_roles(role)
    number1 = random.randint(1,100)

    
    
    if role in interaction.user.roles:
        await interaction.response.send_message("You cant do that. Please wait till your Timer is off.")
    else:
        if number > 101:
            await interaction.response.send_message("You cant guess a number above 100.")
        elif number < 1:
            await interaction.response.send_message("You cant guess a number under 1.")
        else:
            if number == number1:
                await interaction.response.send_message(embed=discord.Embed(
                    title="You guessed the number correctly",
                    description=f"{interaction.user.mention} has guessed the number {number1}\n"
                                f"The number you guessed was {number}",
                    color = discord.Color.from_rgb(0,255,0)
                ))
            else:
                await interaction.response.send_message(embed=discord.Embed(
                    title="You didn't guessed the number correctly",
                    description=f"{interaction.user.mention} has **NOT** guessed the number correctly. The right number was {number1}\n"
                                f"The number you guessed was {number}",
                    color = discord.Color.from_rgb(255,0,0)
                ))
                await interaction.followup.send(f"Gave {member123.mention} the role {role}")
                await asyncio.sleep(1800)
                await member123.remove_roles(role)
                await interaction.followup.send(f"Removed {member123.mention} the role {role}")



client.run("BOT TOKEN")
