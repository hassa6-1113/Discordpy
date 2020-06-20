import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    server_id = message.author.guild.id
    voice_id = message.author.voice.channel.id
    vc = client.voice_clients
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    
    if message.content.startswith('calc'):
        phrase=message.content.split()
        formula=phrase[1]
        await message.channel.send(eval(formula))
    
    if message.content == 'あああ':
        vc.play(/app/SE/aaa.wav)
    
    if message.content == 'cwd':
        path = os.getcwd()
        await message.channel.send(path)
        
    if message.content == 'ls':
        path = os.listdir()
        await message.channel.send(path)
        
    if message.content.startswith('!se'):
        if message.author.voice == None:
            await message.channel.send('ボイスチャンネルに参加してからコマンドを打ってください。')
            return
        phrase=message.content.split()
        
        if phrase[1] == "cn" :
            channel =  client.get_channel(voice_id)
            vc = await channel.connect()
            return

# Botの起動とDiscordサーバーへの接続
client.run(token)
