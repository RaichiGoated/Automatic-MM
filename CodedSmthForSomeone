import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
from discord import app_commands
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True  # Enable the GUILD_MEMBERS intent

class ViewPersistence(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.all(), description="Your best Exchange supporter 💜")

    async def setup_hook(self):
        self.add_view(Ticket())

client = ViewPersistence()
bot = client

info = {}


# Was a project for someone. He asked for those things and I coded it for 7$

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@bot.command()
async def send(ctx):
    await ctx.send(view=Ticket())

class Ticket(View):
    def __init__(self):
        super().__init__(timeout=None) 

    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.blurple, custom_id="OpenTicket")
    async def OpensATicket(self, interaction: discord.Interaction, button):
        await interaction.response.send_message(embed=discord.Embed(
            title="Choose what you want to buy",
            color = discord.Color.from_rgb(0,255,0)

        ), view=WhatYouWantToBuy(), ephemeral=True)


class WhatYouWantToBuy(View):
    def __init__(self):
        super().__init__(timeout=None) 

    @discord.ui.button(label="Gems", style=discord.ButtonStyle.blurple, custom_id="GemsID")
    async def GemsButton(self, interaction: discord.Interaction, button):
        info[interaction.user.id] = {"Buying": "Gems"}
        await interaction.response.send_message(embed=discord.Embed(
            title="How do you want to pay",
            color = discord.Color.from_rgb(0,255,0)
        ),view=HowYouWantToPay(), ephemeral=True)
        print(info)

    @discord.ui.button(label="Huges", style=discord.ButtonStyle.blurple, custom_id="RapID")
    async def RapButton(self, interaction: discord.Interaction, button):
        info[interaction.user.id] = {"Buying": "Huges"}
        await interaction.response.send_message(embed=discord.Embed(
            title="How do you want to pay",
            color = discord.Color.from_rgb(0,255,0)
        ),view=HowYouWantToPay(), ephemeral=True)
        print(info)


class HowYouWantToPay(View):
    def __init__(self):
        super().__init__(timeout=None) 

    @discord.ui.button(label="LTC", style=discord.ButtonStyle.blurple, custom_id="LTCID")
    async def LTCButton(self, interaction: discord.Interaction, button):
        info[interaction.user.id].update({"Payment": "LTC"})

        if "Buying" in info[interaction.user.id]:
            stuff = info[interaction.user.id]["Buying"]

            if info.get(interaction.user.id, {}).get("Buying") == "Gems":

                await interaction.response.send_message(embed=discord.Embed(
                    title=f"How much {stuff} do you want to buy?",
                    description=f"Each 500m Gems costs 12.5€\n\nPlease only write how much you wanna buy in BILLIONS. If you want to buy 5 Billion gems, please write 5 in the Modal.",
                    color=discord.Color.from_rgb(0,255,0)
                ),view=OpenModal(), ephemeral=True)
            elif info.get(interaction.user.id, {}).get("Buying") == "Huges":
                await interaction.response.send_message(embed=discord.Embed(
                    title=f"How much {stuff} do you want to buy?",
                    description=f"One Huge costs 2€. Please write in the Modal how many Huges you wanna buy.",
                    color=discord.Color.from_rgb(0,255,0)
                ),view=OpenModal(), ephemeral=True)

    @discord.ui.button(label="PayPal", style=discord.ButtonStyle.blurple, custom_id="PPID")
    async def PayPalButton(self, interaction: discord.Interaction, button):
        info[interaction.user.id].update({"Payment": "PayPal"})

        if "Buying" in info[interaction.user.id]:
            stuff = info[interaction.user.id]["Buying"]

            if info.get(interaction.user.id, {}).get("Buying") == "Gems":

                await interaction.response.send_message(embed=discord.Embed(
                    title=f"How much {stuff} do you want to buy?",
                    description=f"Each 500m Gems costs 12.5€\n\nPlease only write how much you wanna buy in BILLIONS. If you want to buy 5 Billion gems, please write ``5`` in the Modal.",
                    color=discord.Color.from_rgb(0,255,0)
                ),view=OpenModal(), ephemeral=True)
            elif info.get(interaction.user.id, {}).get("Buying") == "Huges":
                await interaction.response.send_message(embed=discord.Embed(
                    title=f"How much {stuff} do you want to buy?",
                    description=f"One Huge costs 2€. Please write in the Modal how many Huges you wanna buy.",
                    color=discord.Color.from_rgb(0,255,0)
                ),view=OpenModal(), ephemeral=True)

class OpenModal(View):
    def __init__(self):
        super().__init__(timeout=None) 

    @discord.ui.button(label="Open Modal", style=discord.ButtonStyle.blurple, custom_id="OpenModalID")
    async def ModalButtonOpen(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(HowMuchYouWantToBuy())


class HowMuchYouWantToBuy(discord.ui.Modal, title="Please write how much you want to buy"):
    Amount = discord.ui.TextInput(label="How much you want to buy?", placeholder="Please read the Embed above the button you opened this window so you know what to write", required=True, max_length=10, style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        amount = self.Amount.value

        try:
            try:
                if info.get(interaction.user.id, {}).get("Buying") == "Huges":
                    amount = int(amount)
                elif info.get(interaction.user.id, {}).get("Buying") == "Gems":
                    amount = int(amount)
            except ValueError:
                try:
                    if info.get(interaction.user.id, {}).get("Buying") == "Huges":
                        amount = int(amount)
                    else:
                        amount = float(amount)
                except ValueError:
                  
                    await interaction.response.send_message("Please write a valid number.", ephemeral=True)
                    return
            
            

            if info.get(interaction.user.id, {}).get("Buying") == "Gems":
                FinalPrice = 25 * amount
            elif info.get(interaction.user.id, {}).get("Buying") == "Huges":
                FinalPrice = 2 * amount

            info[interaction.user.id].update({"amount": amount})
            info[interaction.user.id].update({"Price": FinalPrice})
            
            await interaction.response.send_message(embed=discord.Embed(
                title="Confirm",
                description=f"Please confirm every detail before opening the Ticket.\n\nWhat you want to buy: **{info.get(interaction.user.id, {}).get('Buying')}**\nHow you want to pay: **{info.get(interaction.user.id, {}).get('Payment')}**\nHow many you want to buy: **{info.get(interaction.user.id, {}).get('amount')}**\nPrice: **{FinalPrice}**",
                color=discord.Color.from_rgb(0, 255, 0)
            ),view=OpenAChannelTicket() , ephemeral=True)
        except ValueError:
            await interaction.response.send_message("Please write a valid number.", ephemeral=True)

class OpenAChannelTicket(View):
    def __init__(self):
        super().__init__(timeout=None) 

    @discord.ui.button(label="Create Ticket", style=discord.ButtonStyle.blurple, custom_id="CreateTicketID")
    async def CreateTicketID(self, interaction: discord.Interaction, button):
        
        category_id = 1274777877660831764  # Replace with your category ID
        category = discord.utils.get(interaction.guild.categories, id=category_id)
        
        if not category:
            await interaction.response.send_message("The specified category does not exist.", ephemeral=True)
            return

        channel_name = f"ticket-{interaction.user.name.lower()}"

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),  # @everyone cannot view
            interaction.user: discord.PermissionOverwrite(view_channel=True),  # User who pressed the button can view
            interaction.guild.me: discord.PermissionOverwrite(view_channel=True)  # Bot can view
        }

        channel = await category.create_text_channel(name=channel_name, overwrites=overwrites)
        await interaction.response.send_message(f"Your ticket has been created: {channel.mention}", ephemeral=True)
        await channel.send(f"<@&WRITE YOUR ROLE ID HERE>, {interaction.user.mention} has opened a Ticket!") # IF you want to get a ROle pinged, chage the ID. If you want to get a user pinged, remove the & and add the userid of the person.

        await channel.send(embed=discord.Embed(
            title="Information",
            description=f"This is the information from the user\n\nWhat he wants to buy: **{info.get(interaction.user.id, {}).get('Buying')}**\nHow he wants to pay: **{info.get(interaction.user.id, {}).get('Payment')}**\nHow many he wants to buy: **{info.get(interaction.user.id, {}).get('amount')}**\nPrice: **{info.get(interaction.user.id, {}).get('Price')}**",
            color=discord.Color.from_rgb(0,255,0)
        ))
        



@bot.command()
async def Litecoin(ctx):
    await ctx.send("") # write here your LTC address.

@bot.command()
async def paypal(ctx):
    await ctx.send("") # Write here your PayPal email

client.run("Bot token here")
