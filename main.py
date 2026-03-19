@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # 判定したい言葉をリストにする
    trigger_words = ["うお", "おお", "ウオ", "オオ"]
    
    # メッセージの中にトリガーワードのどれかが含まれているかチェック
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
