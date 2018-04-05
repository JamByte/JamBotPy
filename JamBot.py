import discord
import asyncio
import random
import json
global jsondata
import re
import time
global timer
import threading
import sys

f = open("jam.json", "r")
json_string=f.read()
f.close()
jsondata=json.loads(json_string)
client = discord.Client()
qqqq=0

mix=["Chocolatechip","Oatmeal", "Cinnamon", "chocolate", "White chocolate", "Dark chocolate", "Chocolate coated", "Magic", "Firey","Frozen", "Enchanted", "Ginger Nut", "All nautral", "Burnt", "Chewy", "Sugar coated"]
@client.event
async def on_ready():
    x=[]
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    timer=time.time()
    await client.change_presence(game=discord.Game(name="In "+str(len(client.servers))+" Servers :[help]"))
    for server in client.servers:
        encoded = (server.name).encode("utf_8", errors='ignore')
        print(encoded)
def wait():
    time.sleep(1)
def cookiegen():
    global jsondata

    timer2=time.time()
    while 0==0:
        serverid=0
        for listems in jsondata["server"]:
            genindex=0
            for item in jsondata["userid"][serverid]:
                jsondata["cookies"][serverid][genindex]+=int(jsondata["grandma"][serverid][genindex]*2)
                jsondata["cookies"][serverid][genindex]+=int(jsondata["plantation"][serverid][genindex]*17)
                jsondata["cookies"][serverid][genindex]+=int(jsondata["foundary"][serverid][genindex]*1333)
                jsondata["cookies"][serverid][genindex]+=int(jsondata["anticookie"][serverid][genindex]*288185)
                jsondata["cookies"][serverid][genindex]+=int(jsondata["wizard"][serverid][genindex]*200)
                jsondata["cookies"][serverid][genindex]+=int(jsondata["demigod"][serverid][genindex]*18930)
                genindex+=1
            serverid+=1
            
            time.sleep(20)
def bakcup():
    global jsondata
    while 0==0:
        a=json.dumps(jsondata)
        print("DataBackedUp")
        f=open("jam.json", "w")
        f.write(a)
        f.close()
        time.sleep(50)

t=threading.Thread(target=cookiegen)
t.start()
f=threading.Thread(target=bakcup)
f.start()
def embed():
    global messagetext
    global cookieembed
    global rgb
    rgb=random.randint(0, 0xFFFFFF)
    cookieembed=discord.Embed(
            title= "Jam Bot",
            description= messagetext,
            color=rgb
            )
for each in client.get_all_emojis():
    if each.name=="Congablob":
        print(each.id)
@client.event
async def on_message(message):
    try:
        global cookiejar
        global timer
        global last
        global cookieembed
        global messagetext
        global rgb
        global jsondata
        global timeindex
        global command
        global mix
        rgb=random.randint(0, 0xFFFFFF)
        command=0
        x=[]
        if int(message.server.id) in jsondata["server"]:
            serverindex=jsondata["server"].index(int(message.server.id))
        else:
            jsondata["server"].append(int(message.server.id))
            jsondata["userid"].append([])
            jsondata["cookies"].append([])
            jsondata["mix"].append([])
            jsondata["grandma"].append([])
            jsondata["grandmaprice"].append([])
            jsondata["plantation"].append([])
            jsondata["plantationprice"].append([])
            jsondata["foundary"].append([])
            jsondata["foundaryprice"].append([])
            jsondata["anticookie"].append([])
            jsondata["anticookieprice"].append([])
            jsondata["wizard"].append([])
            jsondata["wizardprice"].append([])
            jsondata["demigod"].append([])
            jsondata["demigodprice"].append([])
            jsondata["mixtype"].append([])
            jsondata["mixmult"].append([])
            jsondata["mixcost"].append([])
            jsondata["cookiexp"].append([])
            jsondata["rank"].append([])
            jsondata["xpreq"].append([])
            jsondata["totalxp"].append([])
            messagetext= "Server added to internal data"
            embed()
            await client.send_message(message.channel, embed=cookieembed)
            serverindex=jsondata["server"].index(int(message.server.id))
        if int(message.author.id) in jsondata["userid"][serverindex]:
            idindex=jsondata["userid"][serverindex].index(int(message.author.id))
        else:
            jsondata["userid"][serverindex].append(int(message.author.id))
            jsondata["cookies"][serverindex].append(10)
            jsondata["mix"][serverindex].append(1)
            jsondata["grandma"][serverindex].append(0)
            jsondata["grandmaprice"][serverindex].append(1)
            jsondata["plantation"][serverindex].append(0)
            jsondata["plantationprice"][serverindex].append(1)
            jsondata["foundary"][serverindex].append(0)
            jsondata["foundaryprice"][serverindex].append(1)
            jsondata["anticookie"][serverindex].append(0)
            jsondata["anticookieprice"][serverindex].append(1)
            jsondata["wizard"][serverindex].append(0)
            jsondata["wizardprice"][serverindex].append(1)
            jsondata["demigod"][serverindex].append(0)
            jsondata["demigodprice"][serverindex].append(1)
            jsondata["mixtype"][serverindex].append(["Normal"])
            jsondata["mixmult"][serverindex].append(1)
            jsondata["mixcost"][serverindex].append(1)
            jsondata["cookiexp"][serverindex].append(0)
            jsondata["rank"][serverindex].append(0)
            jsondata["xpreq"][serverindex].append(15)
            jsondata["totalxp"][serverindex].append(0)
           

            idindex=jsondata["userid"][serverindex].index(int(message.author.id))
            
        if int(message.channel.id) in jsondata["channel"]:
            
            if int(message.author.id) in jsondata["userid"][serverindex]:
                    if int(message.author.id) in jsondata["usertime"]:
                        
                        timeindex = jsondata["usertime"].index(int(message.author.id))
                        if time.time()-int(jsondata["cooldown"][timeindex])>=10:
                            
                            jsondata["cooldown"][timeindex]=time.time()
                            idindex=jsondata["userid"][serverindex].index(int(message.author.id))
                            jsondata["mix"][serverindex][idindex]=jsondata["mix"][serverindex][idindex] + (1*jsondata["mixmult"][serverindex][idindex])
                            messageevent=0
                            ranevent = random.randint(200,464)
                            if ranevent == 464 and int(message.author.id)!= 372854723969155073:
                                event=random.randint(0,7)
                                if event ==0:
                                    rancookies = random.randint(500, 1000) + int(jsondata["cookies"][serverindex][idindex]*0.2)
                                    jsondata["cookies"][serverindex][idindex]+=rancookies
                                    messagetext= "<@"+str(message.author.id)+"> You found a hidden stash of cookies giving you "+str(rancookies)+" Cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==1:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*1.5)
                                    messagetext= "<@"+str(message.author.id)+"> The cookie gods smiled on you day and you gained 50% of the jar count. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==2:
                                    ranmix=random.randint(350,650)
                                    jsondata["mix"][serverindex][idindex]+=ranmix
                                    messagetext= "<@"+str(message.author.id)+"> Out of nowhere some guy gave you "+str(ranmix)+" Cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
                                elif event==3:
                                    jsondata["mix"][serverindex][idindex]=0
                                    messagetext= "<@"+str(message.author.id)+"> You were mugged of all your cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
                                elif event==4:
                                    jsondata["cookies"][serverindex][idindex]= int(jsondata["cookies"][serverindex][idindex]*0.8)
                                    messagetext= "<@"+str(message.author.id)+"> Sadly a storage crate lanned on your cookie collection and crushed 20% of your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==5:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*2)
                                    messagetext= "<@"+str(message.author.id)+"> Good news, you won the cookie lottery and doubled your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==6:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*0.7)
                                    messagetext= "<@"+str(message.author.id)+"> Sadly you lost 30% of your cookies in a freak baking accident. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==7:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*3)
                                    messagetext= "<@"+str(message.author.id)+"> GG the cookies gods just TRIPLED your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
                                embed()
                                await client.send_message(message.channel, embed=cookieembed)
                        
                            if message.author.id != "372854723969155073":
                                cookiegain=random.randint(1,3)
                                jsondata["cookiexp"][serverindex][idindex]+=cookiegain
                    
                                jsondata["totalxp"][serverindex][idindex]+=cookiegain
                    
                                if jsondata["cookiexp"][serverindex][idindex]>= jsondata["xpreq"][serverindex][idindex]:
                                    print( jsondata["totalxp"][serverindex][idindex])
                                    jsondata["rank"][serverindex][idindex]+=1
                                    jsondata["cookiexp"][serverindex][idindex]=0
                                    jsondata["xpreq"][serverindex][idindex]*=1.5
                                    jsondata["xpreq"][serverindex][idindex]=int(jsondata["xpreq"][serverindex][idindex])
                                    cookiegaink=random.randint(int((jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex])/2),jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex]*2)
                                    jsondata["cookies"][serverindex][idindex]+=cookiegaink
                                    messagetext= "You Just ranked up **"+message.author.name+"#"+message.author.discriminator+",** you are rank "+str(jsondata["rank"][serverindex][idindex])+" You Gained: "+str(cookiegaink)+" Cookies"
                                    embed()
                                    await client.send_message(message.channel, embed=cookieembed)
                                    if int(message.server.id) in [401274275560161290, 336935292269494272]:
                                        q=[]
                               
                                        for each in message.server.role_hierarchy:
                                            q.append(each.name)
                                    
                              
                                        c=q.index("Rank 1")
                               
                                        q=message.server.role_hierarchy
                                        await client.add_roles(message.author, q[(c- jsondata["rank"][serverindex][idindex])+1])
                                        print("thisworks")#
                    else:
                        jsondata["cooldown"].append(int(time.time()))
                        jsondata["jambotcooldown"].append(0)
                        jsondata["usertime"].append(int(message.author.id))
                        command = 1
        #            if command ==1:
        #                print(jsondata["mix"][serverindex][idindex])
        #                idindex=jsondata["userid"][serverindex].index(int(message.author.id))
        #                jsondata["mix"][serverindex][idindex]+=(1*jsondata["mixmult"][serverindex][idindex])
        #                print(jsondata["mix"][serverindex][idindex])
        #                messageevent=0
        #                ranevent = random.randint(100,464)
        #                if ranevent == 464:
        #                    event=random.randint(0,7)
        #                    if event ==0:
        #                        rancookies = random.randint(500, 1000) + int(jsondata["cookies"][serverindex][idindex]*0.2)
        #                        jsondata["cookies"][serverindex][idindex]+=rancookies
        #                        messagetext= "<@"+str(message.author.id)+"> You found a hidden stash of cookies giving you "+str(rancookies)+" Cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
        #                    elif event ==1:
        #                        jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*1.5)
        #                        messagetext= "<@"+str(message.author.id)+"> The cookie gods smiled on you day and you gained 50% of the jar count. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
        #                    elif event ==2:
        #                        ranmix=random.randint(350,650)
        #                        jsondata["mix"][serverindex][idindex]+=ranmix
        #                        messagetext= "<@"+str(message.author.id)+"> Out of nowhere some guy gave you "+str(ranmix)+" Cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
        #                    elif event==3:
        #                        jsondata["mix"][serverindex][idindex]=0
        #                        messagetext= "<@"+str(message.author.id)+"> You were mugged of all your cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
        #                    elif event==4:
        #                        jsondata["cookies"][serverindex][idindex]= int(jsondata["cookies"][serverindex][idindex]*0.8)
        #                        messagetext= "<@"+str(message.author.id)+"> Sadly a storage crate lanned on your cookie collection and crushed 20% of your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
        #                    elif event ==5:
        #                        jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*2)
        #                        messagetext= "<@"+str(message.author.id)+"> Good news, you won the cookie lottery and doubled your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
        #                    elif event ==6:
        #                        jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*0.7)
        #                        messagetext= "<@"+str(message.author.id)+"> Sadly you lost 30% of your cookies in a freak baking accident. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
        #                    elif event ==7:
        #                        jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*3)
        #                        messagetext= "<@"+str(message.author.id)+"> GG the cookies gods just TRIPLED your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
        #                    embed()
        #                    await client.send_message(message.channel, embed=cookieembed)
        else: 
            if message.content.startswith('[bakecookie]') or message.content.startswith('[bakecookies]'):
                if jsondata["mix"][serverindex][idindex]< 1:
                    messagetext= "<@"+str(message.author.id)+"> you dont have any cookie mix to bake with, chat to gain more"
                    jsondata["mix"][serverindex][idindex]=0
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)    
                else:
                    cookieamount= jsondata["mix"][serverindex][idindex] * 6
                    jsondata["cookies"][serverindex][idindex]+=int(cookieamount)
                    jsondata["mix"][serverindex][idindex]=0
                    messagetext= "You bake "+str(cookieamount)+" of "+str(random.choice(jsondata["mixtype"][serverindex][idindex]))+" Cookies and add it to the jar <@"+str(message.author.id)+"> your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)    
               
            elif message.content.startswith('[eatcookie')and "]" in message.content:
                eatamount=int(re.search(r'\d+', message.content).group())
                if jsondata["cookies"][serverindex][idindex]>=eatamount:
                    jsondata["cookies"][serverindex][idindex]-=int(eatamount)
                    jsondata["cookiejar"]+=eatamount
                    messagetext= "<@"+str(message.author.id)+"> you eat **"+str(eatamount)+"** helpless cookies from the jar, sending it to cookie heaven, you have **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in your jar"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                    if jsondata["cookies"][serverindex][idindex]==0:
                        messagetext= "<@"+str(message.author.id)+"> You haven eaten all your cookies, use **[bakecookies]** to get more"
                        embed()
                        await client.send_message(message.channel, embed=cookieembed)
                else:
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[heavencount]'):
                messagetext= "Cookie heaven currently has **"+str(jsondata["cookiejar"])+"** Cookies resting in it"
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[cookiemix]'):
                    messagetext= "You have **"+str(jsondata["mix"][serverindex][idindex])+"** cookie mix"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[cookiemix') and "]" in message.content :
                print(1)
                usermix=int(re.search(r'\d+', message.content).group())
                idindex1=jsondata["userid"].index(int(usermix))
                messagetext= "<@"+str(usermix)+"> has **"+str(jsondata["mix"][idindex1])+"** cookie mix"
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[spam]'):
                spam=0
                while spam<50:
                    await client.send_message(message.author, "I am self aware")
                    spam=spam+1
            elif message.content.startswith('[cookiejar]'):
                messagetext= "<@"+str(message.author.id)+"> You have **"+str(jsondata["cookies"][serverindex][idindex])+"** cookies in your jar"
                embed()
                await client.send_message(message.channel, embed=cookieembed)    
            elif message.content.startswith('[cookiejar') and "]" in message.content:
                    usermix=int(re.search(r'\d+', message.content).group())
                    idindex1=jsondata["userid"].index(int(usermix))
                    messagetext= "<@"+str(usermix)+"> has **"+str(jsondata["cookies"][idindex1])+"** cookies"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[gamble')and  "]" in message.content  :
                messagecontent=message.content
                idindex=jsondata["userid"][serverindex].index(int(message.author.id))
                gambleamount=int(re.search(r'\d+', message.content).group())
                if jsondata["cookies"][serverindex][idindex]< gambleamount:
                    messagetext= "<@"+str(message.author.id)+"> You dont have enough cookies to gamble, use [bakecookie] to get more"
                else:
                    jsondata["cookies"][serverindex][idindex]=jsondata["cookies"][serverindex][idindex]-gambleamount 
                    dice= random.randint(2,12)
                    if dice== 12 :
                        gamblenum = int(gambleamount*5)
                        jsondata["cookies"][serverindex][idindex]+=gamblenum
                        messagetext= '<@'+str(message.author.id)+'> You roll the dice and get a '+str(dice)+', you won '+str(gamblenum)+' cookies, Jar count at '+str(jsondata["cookies"][serverindex][idindex])+' Cookies'
                    elif dice== 11:
                        gamblenum = int(gambleamount*2)
                        jsondata["cookies"][serverindex][idindex]+=gamblenum
                        messagetext= '<@'+str(message.author.id)+'> You roll the dice and get a '+str(dice)+', you won '+str(gamblenum)+' cookies, Jar count at '+str(jsondata["cookies"][serverindex][idindex])+' Cookies'
                    
                    
                    elif dice==2:
                        jsondata["cookies"][serverindex][idindex] = int(jsondata["cookies"][serverindex][idindex]*0.75)
                        messagetext='<@'+str(message.author.id)+'> You roll the dice and get snake eyes, you lost 25% of your jars cookies and the cookies you gambled, Jar count at '+str(jsondata["cookies"][serverindex][idindex])+' Cookies'
                    else:
                        jsondata["cookiejar"]+= gambleamount
                        messagetext='<@'+str(message.author.id)+'> You roll the dice and get a '+str(dice)+', you lost all the cookies you betted, Jar count at '+str(jsondata["cookies"][serverindex][idindex])+' Cookies'
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[jammydodger]'):
        
                if int(message.author.id) in [250138264768479232,194517076432388096, 244728853929394186, 315278094493810700, 205694633001353226, 308209615911387139, 236173630306779138]:
                    idindex=jsondata["userid"][serverindex].index(int(message.author.id))
                    jsondata["cookies"][serverindex][idindex]+=50
                    messagetext= "You bake 50 cookies and add it to the jar <@"+str(message.author.id)+"> your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    messagetext= "You dont have the correct perrsions for this command <@"+str(message.author.id)+"> "
                    embed()
                    await client.send_message(message.channel, embed=cookieembed) 
            elif message.content.startswith('[help]'):
                    messagetext=  '''Avilable Commands:
    Talking in the server gains you cookie mix
    [cookiemix] - displays your current cookie mix count
    [cookiejar] - displays your current cookie count
    [bakecookie] - You bake all your cookie mix into cookies which get added to your jar
    [eatcookie <amount>] - You eat a cookie which decreased the amount in your jar by one
    [gamble <amount>] - gambles <amount> of cookies from your jar for the chance to win more
    [help] - its this command
    [heavencount] - displays the amount of cookies eaten and have gone to heaven
    [givecookie @<user> <amount>] - gives the person the amount of cookies you enetered with a 25% loss
    [leaderboard] - shows a leaderboard of the people with the hihest amount of cookies
    [spam] - does something
    [invite] - displayes the url to invite the bot to your server
    [stats] - displays your stats
    [stats @user] - displays the users stats
    [shop] - shows the shop which  contains items
    [buy] - brings up the buy help section
    '''
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[info]'):
                if int(message.author.id) in jsondata["userid"]:
                    messagetext=  '''**Info:**
    Jam Bot is a bot all about cookies
    When you talk in the server you gain cookie mix which allows you to bake cookies
    Jam Bot was based off the -addcookie and -eatcookie commands from Potato Bot
    Jam Bot by: JamByte#6060
    Jam Bot hosted on Ohceptions Raspberry Pi
    Gamble system devloped by Danny Parker
    '''
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)    
            
            elif message.content.startswith('[backup]'):
                if 0==0:
                        a=json.dumps(jsondata)
                        f=open("jam.json", "w")
                        f.write(a)
                        f.close()
                        messagetext= "You have saved all the bots data, you can now shut it down safely"
                        embed()
                        await client.send_message(message.channel, embed=cookieembed)
                else:
                        messagetext= "You dont have the correct perrsions for this command <@"+str(message.author.id)+"> "
                        embed()
                        await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[leaderboard]'):
                sortcookie, sortid = zip(*sorted(zip(jsondata["cookies"][serverindex], jsondata["userid"][serverindex]), reverse=True))
                index=0
                leaderboard = "LeaderBoard: \n"
                while index <10 and index<len(jsondata["cookies"][serverindex]):
                    leaderboard=leaderboard + "#"+str(index+1)+"<@"+str(sortid[index])+"> Has "+str(sortcookie[index])+" Cookies\n"
                    index=index+1
                messagetext= leaderboard
                embed()
                await client.send_message(message.channel, embed=cookieembed)
                
            elif message.content.startswith('[editcookie') and "]" in message.content:
                if int(message.author.id) in [250138264768479232, 308209615911387139, int(message.server.owner.id)] :
                        idcookie=re.findall(r'\d+', message.content)
                        idindex=jsondata["userid"][serverindex].index(int(idcookie[0]))
                        if "-" in message.content:
                            jsondata["cookies"][serverindex][idindex]=0-int(idcookie[1])
                            messagetext= "You have edited <@"+str(idcookie[0])+"> cookies to -"+str(idcookie[1])+" cookies"
                            embed()
                            await client.send_message(message.channel, embed=cookieembed)
                        elif "+" in message.content:
                            jsondata["cookies"][serverindex][idindex]+=int(idcookie[1])
                            messagetext= "You have edited <@"+str(idcookie[0])+"> cookies to "+str(idcookie[1])+" cookies"
                            embed()
                            await client.send_message(message.channel, embed=cookieembed)
                        else:
                            jsondata["cookies"][serverindex][idindex]=int(idcookie[1])
                            messagetext= "You have edited <@"+str(idcookie[0])+"> cookies to "+str(idcookie[1])+" cookies"
                            embed()
                            await client.send_message(message.channel, embed=cookieembed)
                else:
                        messagetext= "You dont have the correct perrsions for this command <@"+str(message.author.id)+"> "
                        embed()
                        await client.send_message(message.channel, embed=cookieembed) 
            elif message.content.startswith('[givecookie') and "]" in message.content:
                idcookie=re.findall(r'\d+', message.content)
                idindex=jsondata["userid"][serverindex].index(int(idcookie[0]))
                idindex2 =jsondata["userid"][serverindex].index(int(message.author.id))
                if jsondata["cookies"][serverindex][idindex2]<int(idcookie[1]):
                    messagetext= "You dont have enough cookies to make thiss transfer, use [bakecookie] to gain more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else: 
                    jsondata["cookies"][serverindex][idindex]+=int(int(idcookie[1])*0.75)
                    jsondata["cookies"][serverindex][idindex2]-=int(idcookie[1])
                    messagetext= "25% of the cookies were lost in transport, You have given <@"+str(idcookie[0])+">, "+str(int(int(idcookie[1])*0.75))+" cookies"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[blockchannel') and "]" in message.content:
                idcookie=re.findall(r'\d+', message.content)
                if int(message.server.owner.id) ==int(message.author.id):
                    jsondata["channel"].append(int(idcookie[0]))
                    messagetext= "You have blocked Jam Bot comamnds in <#"+str(idcookie[0])+"> but random chance messages will still happen"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    messagetext= "You dont have the correct perrsions for this command <@"+str(message.author.id)+"> "
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[unblockchannel') and "]" in message.content:
                idcookie=re.findall(r'\d+', message.content)
                if int(message.server.owner.id) == int(message.author.id):
                    jsondata["channel"].remove(int(idcookie[0]))
                    messagetext= "You have unblcoked Jam Bot comamnds in <#"+str(idcookie[0])+">"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    messagetext= "You dont have the correct perrsions for this command <@"+str(message.author.id)+"> "
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[shop items]') :
                messagetext= '''Shop:
    Grandma - Produces 2 cookies per 20s, costs '''+str(int(180*jsondata["grandmaprice"][serverindex][idindex]))+''' cookies
    Cookie Plantation - Produces 17 cookie per 20s, costs '''+str(int(1500*jsondata["plantationprice"][serverindex][idindex]))+''' cookies
    Cookie Wizard - Produces 200 cookies per 20s, costs '''+str(int(18000*jsondata["wizardprice"][serverindex][idindex]))+''' cookies
    Cookie Foundary - Produces 1333 cookies per 20s, costs '''+str(int(120000*jsondata["foundaryprice"][serverindex][idindex]))+''' cookies
    Cookie DemiGod - Produces 18930 cookies per 20s,  costs '''+str(int(1703670*jsondata["demigodprice"][serverindex][idindex]))+''' cookies
    Anticookie Condenser - Produces 288185 cookies per 20s, costs '''+str(int(25936680*jsondata["anticookieprice"][serverindex][idindex]))+''' cookies 
    Disclaimer: the 3 second cooldown still applys and everyones prices are different becuase of the 15% price increase
    Use [buy] to see how to buy these items'''
                embed()
                await client.send_message(message.channel, embed=cookieembed)

            elif message.content.startswith('[shop]') :
                messagetext= '''Shop:
    Use [shop items] to see how much  items cost and what they produce
    Use [buy] to see how to buy stuff
    Use [shop mix] to see what mix there are'''
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[shop mix]') :
                messagetext= '''Shop:
    Chocolatechip mix
    Oatmeal mix
    Cinnamon mix
    chocolate mix
    White chocolate mix
    Dark chocolate mix
    Chocolate coated mix
    Magic mix
    Firey mix
    Frozen mix
    Enchanted mix
    Ginger Nut mix
    All natural mix
    Burnt mix
    Chewy mix
    Sugar coated mix
    Every Mix you get doubles the amount of mix you get by sending messages, When you type [buy mix] you get a random mix type.
    Current mix cost '''+str(jsondata["mixcost"][serverindex][idindex]*100)+''' Cookies
    So Far you have collected '''+str(jsondata["mixtype"][serverindex][idindex])
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy mix]') :
                if len(mix)==len(jsondata["mixtype"][serverindex][idindex]):
                    messagetext= "<@"+str(message.author.id)+"> You Own all the types already"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                if jsondata["cookies"][serverindex][idindex]<(int(100*jsondata["mixcost"][serverindex][idindex])):
                    messagetext= "<@"+str(message.author.id)+"> You dont have enough cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    mixtype=random.choice(mix)
                    mixtype2=0
                    while mixtype2==0:
                        if mixtype in jsondata["mixtype"][serverindex][idindex]:
                                mixtype=random.choice(mix)
                        else:
                                mixtype2=1
                    jsondata["cookies"][serverindex][idindex]-=int((int(100*jsondata["mixcost"][serverindex][idindex])))         
                    jsondata["mixtype"][serverindex][idindex].append(mixtype)
                    jsondata["mixcost"][serverindex][idindex]=int(jsondata["mixcost"][serverindex][idindex]*3)
                    jsondata["mixmult"][serverindex][idindex]=int(jsondata["mixmult"][serverindex][idindex]*2)
                
                    messagetext= "You buy one random cookie mix, you now have "+str(mixtype)+" mix added to your collection"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy]') :
                messagetext= '''Buy:
    to buy items use the [buy] command:
    for example [buy grandma], adds one grandma to your count and rmeoves the cookies it costs
    [buy grandma]
    [buy plantation]
    [buy wizard]
    [buy foundary]
    [buy demigod]
    [buy anticookie]'''
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[invite]') :
                messagetext= '''https://discordapp.com/oauth2/authorize?client_id=372854723969155073&scope=bot&permissions=134152'''
                embed()
                await client.send_message(message.channel, embed=cookieembed)       
            elif message.content.startswith('[buy grandma]') :
                if jsondata["cookies"][serverindex][idindex]<(int(180*jsondata["grandmaprice"][serverindex][idindex])):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["grandma"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]-=(int(180*jsondata["grandmaprice"][serverindex][idindex]))
                    jsondata["grandmaprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one grandma, you now have "+str(jsondata["grandma"][serverindex][idindex])+" grandmas"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy plantation]') :
                if jsondata["cookies"][serverindex][idindex]<int(1500*jsondata["plantationprice"][serverindex][idindex]):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["plantation"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]-=(int(1500*jsondata["plantationprice"][serverindex][idindex]))
                    jsondata["plantationprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one Cookie Plantation, you now have "+str(jsondata["plantation"][serverindex][idindex])+" cookie plantations"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy foundary]') :
                if jsondata["cookies"][serverindex][idindex]<int(120000*jsondata["foundaryprice"][serverindex][idindex]):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["foundary"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex])-(int(120000*jsondata["foundaryprice"][serverindex][idindex]))
                    jsondata["foundaryprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one Cookie foundary, you now have "+str(jsondata["foundary"][serverindex][idindex])+" cookie foundarys"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy anticookie]') :
                if jsondata["cookies"][serverindex][idindex]<int(25936680*jsondata["anticookieprice"][serverindex][idindex]):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["anticookie"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]-=(int(25936680*jsondata["anticookieprice"][serverindex][idindex]))
                    jsondata["anticookieprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one anticookie condensor, you now have "+str(jsondata["anticookie"][serverindex][idindex])+" anticookie condensors"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy wizard]') :
                if jsondata["cookies"][serverindex][idindex]<int((18000*jsondata["wizardprice"][serverindex][idindex])):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["wizard"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]-=(int(18000*jsondata["wizardprice"][serverindex][idindex]))
                    jsondata["wizardprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one cookie wizard, you now have "+str(jsondata["wizard"][serverindex][idindex])+" wizards"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[buy demigod]') :
                if jsondata["cookies"][serverindex][idindex]<int(1703670*jsondata["demigodprice"][serverindex][idindex]):
                    messagetext= "<@"+str(message.author.id)+"> You dont have any cookies in your jar use **[bakecookies]** to get more"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
                else:
                    jsondata["demigod"][serverindex][idindex]+=1
                    jsondata["cookies"][serverindex][idindex]-=(int(1703670*jsondata["demigodprice"][serverindex][idindex]))
                    jsondata["demigodprice"][serverindex][idindex]+=0.15
                    messagetext= "You buy one cookie demigod, you now have "+str(jsondata["demigod"][serverindex][idindex])+" demigods"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[stats]'):
                cookieper=int(jsondata["grandma"][serverindex][idindex]*6)+int(jsondata["plantation"][serverindex][idindex]*50)+int(jsondata["foundary"][serverindex][idindex]*4000)+int(jsondata["anticookie"][serverindex][idindex]*864556)+int(jsondata["wizard"][serverindex][idindex]*600)+int(jsondata["demigod"][serverindex][idindex]*56789)
                messagetext= '''<@'''+str(message.author.id)+'''> has:
    **'''+str(jsondata["cookies"][serverindex][idindex])+'''** cookies
    **'''+str(jsondata["mix"][serverindex][idindex])+'''** Cookie mix
    **'''+str(int(cookieper/3))+'''** Cookies per 20s
    **'''+str(jsondata["mixmult"][serverindex][idindex])+'''** cookie mix multiplier
    **'''+str(jsondata["grandma"][serverindex][idindex])+'''** Grandmas 
    **'''+str(jsondata["plantation"][serverindex][idindex])+'''** Cookie Plantation
    **'''+str(jsondata["wizard"][serverindex][idindex])+'''** Cookie wizards 
    **'''+str(jsondata["foundary"][serverindex][idindex])+'''** Cookie Foundarys
    **'''+str(jsondata["demigod"][serverindex][idindex])+'''** Cookie demigods 
    **'''+str(jsondata["anticookie"][serverindex][idindex])+'''** Anticookie condensors
    '''
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            elif message.content.startswith('[stats') and "]" in message.content:
                usermix=int(re.search(r'\d+', message.content).group())
                idindex1=jsondata["userid"][serverindex].index(int(usermix))
                cookieper=int(jsondata["grandma"][serverindex][idindex1]*6)+int(jsondata["plantation"][serverindex][idindex1]*50)+int(jsondata["foundary"][serverindex][idindex1]*4000)+int(jsondata["anticookie"][serverindex][idindex1]*864556)+int(jsondata["wizard"][serverindex][idindex1]*600)+int(jsondata["demigod"][serverindex][idindex1]*56789)
                messagetext= '''<@'''+str(usermix)+'''> has:
    **'''+str(jsondata["cookies"][serverindex][idindex1])+'''** cookies
    **'''+str(jsondata["mix"][serverindex][idindex1])+'''** Cookie mix
    **'''+str(int(cookieper/3))+'''** Cookies per 20s
    **'''+str(jsondata["mixmult"][serverindex][idindex1])+'''** cookie mix multiplier
    **'''+str(jsondata["grandma"][serverindex][idindex1])+'''** Grandmas 
    **'''+str(jsondata["plantation"][serverindex][idindex1])+'''** Cookie Plantation
    **'''+str(jsondata["wizard"][serverindex][idindex1])+'''** Cookie wizards 
    **'''+str(jsondata["foundary"][serverindex][idindex1])+'''** Cookie Foundarys
    **'''+str(jsondata["demigod"][serverindex][idindex1])+'''** Cookie demigods 
    **'''+str(jsondata["anticookie"][serverindex][idindex1])+'''** Anticookie condensors
    '''
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            
            elif message.content.startswith('[xpleaderboard]'):
                sortcookie, sortid, rankid = zip(*sorted(zip(jsondata["totalxp"][serverindex], jsondata["userid"][serverindex],  jsondata["rank"][serverindex], ), reverse=True))
                index=0
                leaderboard = "LeaderBoard: \n"
                while index <10 and index<len(jsondata["cookies"][serverindex]):
                    leaderboard=leaderboard + "#"+str(index+1)+"<@"+str(sortid[index])+"> With Rank "+str(rankid[index])+" and "+str(sortcookie[index])+" Total Xp\n"
                    index=index+1
                messagetext= leaderboard
                embed()
                await client.send_message(message.channel, embed=cookieembed)
            else:
                if int(message.author.id) in jsondata["userid"][serverindex]:
                    if int(message.author.id) in jsondata["usertime"]:
                        
                        timeindex = jsondata["usertime"].index(int(message.author.id))
                        if time.time()-int(jsondata["cooldown"][timeindex])>=10:
                            
                            jsondata["cooldown"][timeindex]=time.time()
                            idindex=jsondata["userid"][serverindex].index(int(message.author.id))
                            jsondata["mix"][serverindex][idindex]=jsondata["mix"][serverindex][idindex] + (1*jsondata["mixmult"][serverindex][idindex])
                            messageevent=0
                            ranevent = random.randint(200,464)
                            if ranevent == 464 and int(message.author.id)!= 372854723969155073:
                                event=random.randint(0,7)
                                if event ==0:
                                    rancookies = random.randint(500, 1000) + int(jsondata["cookies"][serverindex][idindex]*0.2)
                                    jsondata["cookies"][serverindex][idindex]+=rancookies
                                    messagetext= "<@"+str(message.author.id)+"> You found a hidden stash of cookies giving you "+str(rancookies)+" Cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==1:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*1.5)
                                    messagetext= "<@"+str(message.author.id)+"> The cookie gods smiled on you day and you gained 50% of the jar count. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==2:
                                    ranmix=random.randint(350,650)
                                    jsondata["mix"][serverindex][idindex]+=ranmix
                                    messagetext= "<@"+str(message.author.id)+"> Out of nowhere some guy gave you "+str(ranmix)+" Cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
                                elif event==3:
                                    jsondata["mix"][serverindex][idindex]=0
                                    messagetext= "<@"+str(message.author.id)+"> You were mugged of all your cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
                                elif event==4:
                                    jsondata["cookies"][serverindex][idindex]= int(jsondata["cookies"][serverindex][idindex]*0.8)
                                    messagetext= "<@"+str(message.author.id)+"> Sadly a storage crate lanned on your cookie collection and crushed 20% of your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==5:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*2)
                                    messagetext= "<@"+str(message.author.id)+"> Good news, you won the cookie lottery and doubled your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==6:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*0.7)
                                    messagetext= "<@"+str(message.author.id)+"> Sadly you lost 30% of your cookies in a freak baking accident. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
                                elif event ==7:
                                    jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*3)
                                    messagetext= "<@"+str(message.author.id)+"> GG the cookies gods just TRIPLED your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
                                embed()
                                await client.send_message(message.channel, embed=cookieembed)
                        
                            if message.author.id != "372854723969155073":
                                cookiegain=random.randint(1,3)
                                jsondata["cookiexp"][serverindex][idindex]+=cookiegain
                    
                                jsondata["totalxp"][serverindex][idindex]+=cookiegain
                    
                                if jsondata["cookiexp"][serverindex][idindex]>= jsondata["xpreq"][serverindex][idindex]:
                                    print( jsondata["totalxp"][serverindex][idindex])
                                    jsondata["rank"][serverindex][idindex]+=1
                                    jsondata["cookiexp"][serverindex][idindex]=0
                                    jsondata["xpreq"][serverindex][idindex]*=1.5
                                    jsondata["xpreq"][serverindex][idindex]=int(jsondata["xpreq"][serverindex][idindex])
                                    cookiegaink=random.randint(int((jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex])/2),jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex]*2)
                                    jsondata["cookies"][serverindex][idindex]+=cookiegaink
                                    messagetext= "You Just ranked up **"+message.author.name+"#"+message.author.discriminator+",** you are rank "+str(jsondata["rank"][serverindex][idindex])+" You Gained: "+str(cookiegaink)+" Cookies"
                                    embed()
                                    await client.send_message(message.channel, embed=cookieembed)
                                    if int(message.server.id) in [401274275560161290, 336935292269494272]:
                                        q=[]
                               
                                        for each in message.server.role_hierarchy:
                                            q.append(each.name)
                                    
                              
                                        c=q.index("Rank 1")
                               
                                        q=message.server.role_hierarchy
                                        await client.add_roles(message.author, q[(c- jsondata["rank"][serverindex][idindex])+1])
                                        print("thisworks")#
                    else:
                        jsondata["cooldown"].append(int(time.time()))
                        jsondata["jambotcooldown"].append(0)
                        jsondata["usertime"].append(int(message.author.id))
            if message.channel.id == "375630029373046784" and  int(message.author.id)!=372854723969155073:
                maymay=message.channel
                messagetext= message.content
                av=message.author.avatar_url
                embed()
                await client.send_message(discord.Object(id="377183710916640770"), embed=cookieembed)
            if message.channel.id == "377183710916640770"and int(message.author.id)!=372854723969155073:
                jamjam=message.channel
                messagetext= message.content
                av=message.author.avatar_url
                embed()
                await client.send_message(discord.Object(id="375630029373046784"), embed=cookieembed)
            
                
    except Exception as e:
        print(e)
    if message.content.startswith('[rank]') :
                    messagetext= "You are rank: "+str(jsondata["rank"][serverindex][idindex])+"\nYou Need "+str(jsondata["cookiexp"][serverindex][idindex])+"/"+str(jsondata["xpreq"][serverindex][idindex])+" To rank up"
                    embed()
                    await client.send_message(message.channel, embed=cookieembed)
   
    if command == 1 and "372854723969155073" in message.content:
            messagetext= ":congablob:"
            embed()
            jsondata["jambotcooldown"][timeindex]=time.time()
            jsondata["cookies"][serverindex][idindex]+=25
            await client.send_message(message.channel,":cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:\n**25** Cookies have been transfered to your jar :P, you have** "+str(jsondata["cookies"][serverindex][idindex])+" **In your jar")
    command=0
    if int(message.author.id) in jsondata["usertime"]:
        timeindex = jsondata["usertime"].index(int(message.author.id))
        if (time.time()-int(jsondata["cooldown"][timeindex]))>=10:
            jsondata["cooldown"][timeindex]=time.time()
            command = 1
                        
    else:
        print("yes")
        jsondata["cooldown"].append(int(time.time()))
        jsondata["jambotcooldown"].append(0)
        jsondata["usertime"].append(int(message.author.id))
        command = 1
    
    if 1==0:
        idindex=jsondata["userid"][serverindex].index(int(message.author.id))
        jsondata["mix"][serverindex][idindex]=jsondata["mix"][serverindex][idindex] + (1*jsondata["mixmult"][serverindex][idindex])
        messageevent=0
        ranevent = random.randint(200,464)
        if ranevent == 464 and int(message.author.id)!= 372854723969155073:
            event=random.randint(0,7)
            if event ==0:
                rancookies = random.randint(500, 1000) + int(jsondata["cookies"][serverindex][idindex]*0.2)
                jsondata["cookies"][serverindex][idindex]+=rancookies
                messagetext= "<@"+str(message.author.id)+"> You found a hidden stash of cookies giving you "+str(rancookies)+" Cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
            elif event ==1:
                jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*1.5)
                messagetext= "<@"+str(message.author.id)+"> The cookie gods smiled on you day and you gained 50% of the jar count. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
            elif event ==2:
                ranmix=random.randint(350,650)
                jsondata["mix"][serverindex][idindex]+=ranmix
                messagetext= "<@"+str(message.author.id)+"> Out of nowhere some guy gave you "+str(ranmix)+" Cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
            elif event==3:
                jsondata["mix"][serverindex][idindex]=0
                messagetext= "<@"+str(message.author.id)+"> You were mugged of all your cookie mix. You have **"+str(jsondata["mix"][serverindex][idindex])+"** mix"
            elif event==4:
                jsondata["cookies"][serverindex][idindex]= int(jsondata["cookies"][serverindex][idindex]*0.8)
                messagetext= "<@"+str(message.author.id)+"> Sadly a storage crate lanned on your cookie collection and crushed 20% of your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
            elif event ==5:
                jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*2)
                messagetext= "<@"+str(message.author.id)+"> Good news, you won the cookie lottery and doubled your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
            elif event ==6:
                jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*0.7)
                messagetext= "<@"+str(message.author.id)+"> Sadly you lost 30% of your cookies in a freak baking accident. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it" 
            elif event ==7:
                jsondata["cookies"][serverindex][idindex]=int(jsondata["cookies"][serverindex][idindex]*3)
                messagetext= "<@"+str(message.author.id)+"> GG the cookies gods just TRIPLED your cookies. Your cookie jar has **"+str(jsondata["cookies"][serverindex][idindex])+"** Cookies in it"
            embed()
            await client.send_message(message.channel, embed=cookieembed)
                        
        if message.author.id != "372854723969155073":
            cookiegain=random.randint(1,2)
            jsondata["cookiexp"][serverindex][idindex]+=cookiegain
                    
            jsondata["totalxp"][serverindex][idindex]+=cookiegain
                    
            if jsondata["cookiexp"][serverindex][idindex]>= jsondata["xpreq"][serverindex][idindex]:
                print( jsondata["totalxp"][serverindex][idindex])
                jsondata["rank"][serverindex][idindex]+=1
                jsondata["cookiexp"][serverindex][idindex]=0
                jsondata["xpreq"][serverindex][idindex]*=1.5
                jsondata["xpreq"][serverindex][idindex]=int(jsondata["xpreq"][serverindex][idindex])
                cookiegaink=random.randint(int((jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex])/2),jsondata["rank"][serverindex][idindex]*jsondata["totalxp"][serverindex][idindex]*2)
                jsondata["cookies"][serverindex][idindex]+=cookiegaink
                messagetext= "You Just ranked up **"+message.author.name+"#"+message.author.discriminator+",** you are rank "+str(jsondata["rank"][serverindex][idindex])+" You Gained: "+str(cookiegaink)+" Cookies"
                embed()
                await client.send_message(message.channel, embed=cookieembed)
                if int(message.server.id) in [401274275560161290]:
                    q=[]
                               
                    for each in message.server.role_hierarchy:
                        q.append(each.name)
                                    
                              
                    c=q.index("Rank 1")
                               
                    q=message.server.role_hierarchy
                    await client.add_roles(message.author, q[(c- jsondata["rank"][serverindex][idindex])+1])
                    print("thisworks")
            print(e)
            
        #print("yes")
        #command=0
        #if int(message.author.id) in jsondata["usertime"]:
        #    timeindex = jsondata["usertime"].index(int(message.author.id))
        #    if (time.time()-int(jsondata["jambotcooldown"][timeindex]))>=10:
        #        jsondata["cooldown"][timeindex]=time.time()
        #        command = 1
                        
        #else:
        #    jsondata["cooldown"].append(int(time.time()))
        #    jsondata["jambotcooldown"].append(0)
        #    jsondata["usertime"].append(int(message.author.id))
        #    command = 1
        #if command == 1:
        #    messagetext= ":congablob:"
        #    embed()
        #    jsondata["jambotcooldown"][timeindex]=time.time()
        #    jsondata["cookies"][serverindex][idindex]+=25
        #    await client.send_message(message.channel,":cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie::cookie:\n**25** Cookies have been transfered to your jar :P, you have** "+str(jsondata["cookies"][serverindex][idindex])+" **In your jar")
                       
 



client.run("your token here",reconnect=True)

