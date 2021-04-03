import discord
import asyncio
import datetime
import pytz
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 실행되었습니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(".명령어"))

@client.event
async def on_message(message):
    if message.content == ".명령어":
        embed = discord.Embed(title="명령어안내", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xCCCCCC)
        embed.add_field(name=".다이렉트 발급", value="`다이렉트 발급`", inline=False)
        embed.add_field(name=".관리자 명단", value="`관리자 명단을 확인합니다.`", inline=False)
        embed.add_field(name=".개발자 명단", value="`개발자 명단을 확인합니다.`", inline=False)
        embed.add_field(name=".디스코드 주소", value="`디스코드 주소를 확인합니다.`", inline=False)
        embed.add_field(name=".봇 개발자", value="`봇을 만든 개발자를 확인합니다.`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY", icon_url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".다이렉트 발급":
        embed = discord.Embed(title="다이렉트 발급", color=0xCCCCCC)
        embed.add_field(name="GENIE SERVER", value="`connect geniekr.kro.k`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".관리자 명단":
        embed = discord.Embed(title="관리자 명단", color=0xCCCCCC)
        embed.add_field(name="총관리자", value="`🌟 명품`", inline=False)
        embed.add_field(name="부총관리자", value="`⭐️ 딱대` `⭐️ 쥬브`", inline=False)
        embed.add_field(name="관리자", value="`⚡️ 동동` `⚡️ 아델`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".개발자 명단":
        embed = discord.Embed(title="개발자 명단", color=0xCCCCCC)
        embed.add_field(name="GENIE SERVER DEV", value="`🔨 붕어` `🔨 기리` `🔨 ChangE` `🔨 KAY`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".디스코드 주소":
        embed = discord.Embed(title="디스코드 주소", color=0xCCCCCC)
        embed.add_field(name="GENIE DISCORD", value="`https://discord.gg/YE9bcetNUS`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".봇 개발자":
        embed = discord.Embed(title="봇 개발자", color=0xCCCCCC)
        embed.add_field(name="BOT DEV", value="`KAY#1129` `TEAM GRAY :: https://discord.gg/AZNaxrmX3d`", inline=False)
        embed.set_footer(text="Made by. TEAM GRAY")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/827905879075979275/827908587178819594/image01.png")
        await message.channel.send (embed=embed)
        await message.delete()

    if message.content == ".내 정보":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xCCCCCC)
        embed.add_field(name="닉네임", value=message.author.name, inline=False)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send (embed=embed)
        await message.delete()

client.run('ODIxNjkwMDg0NTQ5MTk3ODU1.YFHYhg.gBZ1Wy1QevB5vg7Vt7Qsc_m1Y5U')