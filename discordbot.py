from discord.ext import commands
import os
import traceback
import discord
import random  # おみくじで使用

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "GoodMorning":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good morning")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "GoodNight":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Go to bed early♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "Mornin":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん ☆おはようございます☆Good morning!")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "Goodevening":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん　Good evening～☆" )  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "Hello!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention} ☆༺.Hello All.Everyone! Thank you!🤩")  # f文字列（フォーマット済み文字列リテラル）
 
    if message.content == "こんにちわ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんにちは☺️楽しんで！")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "こんばんわ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん こんばんは😃🌃早く休みましょう🎵")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おはよーさん":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん GoodMorning♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "おやすみなさいませ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん Good Night! Have a good dream♡")  # f文字列（フォーマット済み文字列リテラル）

    if message.content == "jp/jpyn":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip JPYN 10 "f"{message.author.mention}　 🔑<:JPYNdisco:698471276498649168> ")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "jp/ben":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BEN 100 "f"{message.author.mention}　　🔑<:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>  Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "jp/bgpt":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BGPT 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "jp/kenj":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip KENJ 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "jp/sprts":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip SPRTS 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
     if message.content == "sb/jpyn":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip JPYN 10 "f"{message.author.mention}　 🔑<:JPYNdisco:698471276498649168> ")  # f文字列（フォーマット済み文字列リテラル）
       
    if message.content == "sb/ben":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BEN 100 "f"{message.author.mention}　　🔑<:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>  Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/bgpt":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip BGPT 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/kenj":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip KENJ 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "sb/sprts":
        # チャンネルへメッセージを送信
        await message.channel.send("/tip SPRTS 100 "f"{message.author.mention}　 🔑<:BGPT02:698471366004965406> Thank you♡")  # f文字列（フォーマット済み文字列リテラル）
    
   
    elif message.content == "b/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "b/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "b/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記   
     
    
    elif message.content == "j/rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain BGPT 60 ActiveUserOnly  <:BGPT02:698471366004965406><:good01:699581068285706301>🌈☔It Rains")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '🌈')]  # for文の内包表記
         
            
    elif message.content == "j/Rain":
        # リアクションアイコンを付けたい
        q = await message.channel.send("  /rain BEN 30 ActiveUserOnly  <:benkeicoinsl:698471387064696833>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:benkeicoinsl:698471387064696833>')]  # for文の内包表記

        
    elif message.content == "j/RAIN":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain JPNY 50 ActiveUserOnly  <:JPYNdisco:698471276498649168>🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '🌈')]  # for文の内包表記
        
   
    elif message.content == "j/RAin":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain KENJ 100 ActiveUserOnly  <:kenj:700136543003607101> 🌈☔It Rains<:jhlo:700932650944299098>")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:sangras01:699579409220370514>')]  # for文の内包表記
      
    
    elif message.content == "j/RAIn":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /rain SPRTS 1000 ActiveUserOnly  <:sprts:699076413931782146> 🌈☔It Rains🌱")
        [await q.add_reaction(i) for i in ('<:sprts:699076413931782146>', '🌱')]  # for文の内包表記
        
        
   
    elif message.content == "j/throw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 200 4 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "j/THROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 80 4 EquallyDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記

        
    elif message.content == "j/THrow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 100 4 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "j/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 400 4 EquallyDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記


    elif message.content == "j/THROw":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 300 5 EquallyDistributed  <:good01:699581068285706301><:BGPT02:698471366004965406><:BGPT02:698471366004965406>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:good:699580636448423936>')]  # for文の内包表記


    elif message.content == "j/thunder":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /thunder BGPT 300 ActiveUserOnly  <:good:699580636448423936><:BGPT02:698471366004965406>thunder")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:BGPT02:698471366004965406>')]  # for文の内包表記

        
    elif message.content == "j/tHROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BGPT 500 4 AttenuationDistributed  <:BGPT02:698471366004965406><:good:699580636448423936>")
        [await q.add_reaction(i) for i in ('<:BGPT02:698471366004965406>', '<:jhlo:700932650944299098>')]  # for文の内包表記
    
    
    elif message.content == "j/thROW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw BEN 100 4 AttenuationDistributed  <:benkeicoinsl:698471387064696833>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:BENKEICOIN04:698471407650209832>', '<:good:699580636448423936>')]  # for文の内包表記
 
    
    elif message.content == "j/thrOW":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw JPYN 100 4 AttenuationDistributed  <:JPYNdisco:698471276498649168>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:JPYNdisco:698471276498649168>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "j/THRow":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /throw KENJ 1000 4 AttenuationDistributed  <:kenj:700136543003607101>Pls receive→/catch✋")
        [await q.add_reaction(i) for i in ('<:kenj:700136543003607101>', '<:good01:699581068285706301>')]  # for文の内包表記

        
    elif message.content == "死ね":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}　💀🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記


    elif message.content == "fuckyou":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}　💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記


    elif message.content == "shit":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記
      
    
    elif message.content == "cunt":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /tip dappuncoin 9314 "f"{message.author.mention}💩🚫Prohibited terms💩💩")
        [await q.add_reaction(i) for i in ('💩', '🚫')]  # for文の内包表記




    elif message.content == "運勢":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="オミクジ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[今日の運勢YourFortune] ",
                        value=random.choice(('☆☆彡超🤩最高☆彡☆【何してもVeryGood!勝負に強い日です】','🌟最高【チームに恵まれた日です。チャレンジしたら幸運を招きます☆彡】','やったね☆彡！【納得出来る日でしょう。金運は余り期待出来ないです。】'
                                             ,'大吉【☆☆☆自信もって取り組めば必ず好成果となって返ってきます。♡♡♡恋愛運は超ベリグっ】', '中吉【☆☆好チャンス！攻めて成果あり。♡♡とりあえず問題なしかな！？】', '小吉【☆☆通常のセオリーを変化させたら好成果となる。♡♡現状から変化ない】'
                                             ,  '末吉【☆☆参加型オンラインゲームで好成果あり♡ゲームばかりじゃダメ。出会いを求めて外にでたら吉あり】', '吉【☆現状変化なし♡特に変化なし。そのままやっとけ！】',  '吉【☆まぁ！こんなもんよ】'
                                             , 'ごく普通やね【何それ！？と思うだろうがごく普通だ！棚から牡丹餅はない】', '大凶【▲▲吐き気するわ！駄目だこりゃ】'
                                             , '凶【▲残念！好機はないね。負けも勝ちの内かと思え！】', '大凶【▲▲吐き気するわ！駄目だこりゃ】')), inline=False)
        await message.channel.send(embed=embed)


    elif message.content == "ortune":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="☆OMIKUJI☆Fortune☆", description=f"{message.author.mention}Today!YourFortune!☆",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[Today!YourFortune!] ",
                        value=random.choice(('☆☆彡Very🤩VeryGood☆彡☆【Very Good! It ’s a very competitive day.】','☆VeryGoood!☆【It is a good day for the team. 】','Good☆彡！【It will be a convincing day. I can not expect much money.】'
                                             ,'VeryGood【☆☆☆If you work with confidence, you will always get good results. ♡♡♡ Love luck is super berig】', 'GoodDay【☆☆Good chance! There is a result of attacking. ♡♡ For the time being, there is no problem! ?】', 'Good!【☆☆ If you change the usual theory, you will get good results. ♡♡ No change from the current situation】'
                                             ,  'usuallyGood【☆☆Good results with participatory online games ♡ Not only games. Good luck if you go outside to meet】', 'good!【☆The current situation is unchanged ♡ No particular change Let it go！】',  'Good!【☆I do not need any advice】'
                                             , 'It is normal [What is that! ? You probably think that is normal! There is no peony mochi from the shelf', 'Great evil [Great evil [▲▲ I am nauseous!]'
                                             , 'Worst【▲Sorry! There is no opportunity. I think the loss is a win！】', 'Very worst!BAD【▲▲I m nauseous! Useless】')), inline=False)
        await message.channel.send(embed=embed)
        
client.run(token)
