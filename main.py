import discord
import os
from flask import Flask
from threading import Thread

# Botの基本設定（これが消えていたのでエラーになっていました）
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 冷笑回数を記録するための辞書
reisho_counts = {}

# Render対策（サーバーを落とさないため）
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=10000)

@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # 「うお」「おお」のひらがな・カタカナ両方に対応
    trigger_words = ["うお", "おお", "ウオ", "オオ"]
    
    if any(word in message.content for word in trigger_words):
        user_id = message.author.id
        
        # カウントを増やす
        reisho_counts[user_id] = reisho_counts.get(user_id, 0) + 1
        count = reisho_counts[user_id]
        
        # 返信メッセージ
        response = (
            f"冷笑を検出しました！\n"
            f"しね！\n"
            f"{message.author.mention} の冷笑回数：{count}回"
        )
        await message.channel.send(response)

# サーバー起動とBot起動を同時に行う
Thread(target=run).start()
client.run(os.getenv('DISCORD_TOKEN'))
