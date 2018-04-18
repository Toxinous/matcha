import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == "435316816852549632":
        await client.add_reaction(message, "✅")
        await client.add_reaction(message, "❎")

@client.event
async def on_member_join(member):

    embed = discord.Embed(colour=discord.Colour(0x78b64c), timestamp=datetime.datetime.utcnow())

    embed.set_thumbnail(url="https://orig00.deviantart.net/4b59/f/2018/107/1/a/matcha_by_lahlly-dc934g1.png")

    embed.add_field(name="Welcome to Matcha Café!", value="We hope you enjoy your stay, {} Make sure to check out the channels listed under **info & rules**! ♡".format(member.mention))
    embed.add_field(name="Feel free to invite your friends using the link below!", value="━♡ http://discord.gg/8Ne8gXP ♡━")

    await client.send_message(client.get_channel("433143594145021952"), embed=embed)

client.run(os.environ.get("TOKEN"))
