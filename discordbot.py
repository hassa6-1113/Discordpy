import discord
import  requests
from langdetect import detect

Discord_Token = "MTM0MTM5OTI3ODE3MzU1NjgwOQ.GsEx_S.DLbPPPg74OXOhd7musKzzTHfU03y64djjJyICA"

#動作指定チャンネル
Discord_channel_ID = 1341449538195558521

Intents = discord.Intents.all()
Intents.typing = False 
Intents.message_content = True

client = discord.Client(intents=Intents)

#言語判別関数
def language(text):
    lang = detect(text)
    return lang

#起動時動作
@client.event
async def on_ready():
    print("起動しました")

#翻訳関連動作
@client.event
async def on_message(message):
    #指定チャンネル以外からのメッセージは無視
    if message.channel.id != Discord_channel_ID:
        return

    #Bot自身のメッセージは無視
    if message.author == client.user:
        return

    #Bot終了コマンド
    if message.content.startswith("Wakaさん早期入稿ありがとう"):
        await message.channel.send("おやすみ！また明日！")
        await client.close()
        exit()

    DeepL_Token = "7666a337-a7ae-deeb-1aab-8cb64c16cb78:fx"
    DeepL_API_URL = "https://api-free.deepl.com/v2/translate"

      #言語を自動判定する
    chgcmd = message.content[0:2]
    if chgcmd[0:1] == "-":
        chgstr = message.content[3:]
    else:
        chgstr = message.content
        
    source_lang = language(chgstr)
    #-k ⇒ 日本語から韓国語
    if chgcmd == "-k":
        if source_lang == "ja":
            target_lang = "KO"
        else:
            target_lang = "KO"
    elif chgcmd == "-j":
        if source_lang == "ja":
            target_lang = "EN"
        elif source_lang == "en":
            target_lang = "JA"
        elif source_lang == "ko":
            target_lang = "JA"
        else:
             target_lang = "JA"
    else:
        if source_lang == "ja":
            target_lang = "EN"
        elif source_lang == "en":
            target_lang = "JA"
        elif source_lang == "ko":
            target_lang = "JA"
        else:
            target_lang = "JA"

    params = {
        "auth_key" : DeepL_Token,
        "text" : chgstr,
        "source_lang": source_lang,
        "target_lang": target_lang
    }

    response = requests.post(DeepL_API_URL, data=params)

    #HTTPリクエストが成功した場合
    if response.status_code == 200:
        response_json = response.json()
        translated_text = response_json["translations"][0]["text"]
        await message.channel.send(translated_text)

    #エラーメッセージ
    else:
        await message.channel.send("ごめんね。翻訳できません。")
        await message.channel.send("↓のコマンドを使ってみてね。")
        erromsg ="/translate"
        await message.channel.send(erromsg)

client.run(Discord_Token)
