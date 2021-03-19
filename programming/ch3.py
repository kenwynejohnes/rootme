#!/usr/bin/python3

import socket, codecs #connect special library socket

#defining ping_pong function
def ping_pong():
    bot.send("PRIVMSG Candy PING\n") #send message to Candy Bot
    while True:
        smsg = ""
        smsg = bot.recv(7000)
        print(smsg)
        if smsg.find("/")>-1:
            print("[!] Waiting for ping message...")
        elif smsg.find("PING")>-1:    # If PING is captured
            try:
                smsg=smsg.replace("PING","PONG") # raplace "PING" with "PONG"
                bot.send(smsg) # send back the "PONG" message
                bot.send(smsg) # do it more than once to make sure it's received
                bot.send(smsg)
                print("PONG sent")
                break
            except:
                print("[!] Waiting for ping message...")
    

#define function that solves this challenge
def ep3_solve():
    bot.send("PRIVMSG Candy :!ep3\n") #send message to Candy Bot
    smsg = ""
    smsg = bot.recv(7000)
    print(smsg)
    smsg1=smsg[42:smsg.find(":")-1]
    smsg2=codecs.decode(smsg1, 'rot-13')
    bot.send("PRIVMSG Candy :!ep3 -rep " + smsg2 + " \n")
    print("Answer sent")
    print(bot.recv(7000))
    bot.send("QUIT :By3 By3!")
        
#Setup a connection with the IRC Server
server = "irc.root-me.org" #server
port = 6667 #port
nickname = "LateraL"
botname = "Candy"
channel = "#root-me_challenge"

try:
    print("[+] Creating socket")
    bot = socket.socket() #create socket 
    print("[+] Connecting with %s:%d"%(server,port))
    bot.connect((server, port)) #connect to host:port
except:
    print("[!] Can't connect")
else:
    print("[+] Sending nickname")
    bot.send("NICK " + nickname + "\n") #setup nickname for user
    print("[+] Sending USER command")
    bot.send("USER LateraL irc.root-me.org root-me :ChallengeBot" ) 
    print("[+] Join "+ channel)
    bot.send("[+] JOIN " + channel) #joining channel
    ping_pong()
    ep3_solve()
print("[+] Go To Sleep")
bot.close()
