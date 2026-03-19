import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    # Bot自身の発言には反応しない
    if message.author.bot:
        return

    # 「うお」または「おお」が含まれているかチェック
    if "うお" in message.content or "おお" in message.content:
        # メンションして返信
        await message.channel.send(f"冷笑を検出しました！ しね！ {message.author.mention}")

client.run(os.getenv('DISCORD_TOKEN'))
