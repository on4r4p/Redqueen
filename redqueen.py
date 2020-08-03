#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asciimatics.effects import Print 
from asciimatics.renderers import FigletText, Rainbow 
from asciimatics.particles import ShootScreen 
from asciimatics.scene import Scene 
from asciimatics.screen import Screen 
from random import randint, choice, shuffle 
from twython import Twython 
from TwitterApiKeys import app_key, app_secret, oauth_token, oauth_token_secret 
from pyfiglet import Figlet 
from threading import Thread 
import re,socket,time,sys,os,string,datetime,emoji,feedparser

#Some Vars



GOGOGO = False

SHUTDOWN = False

RssSent = []

CHANNEL = ""

fuck = 0

Rthourtweet = ""

exit = 0

tmpbypass = 0

doneid = 0

waithour = 0

waithalf = 0

moyscore = []

emolist = []

rtsave = ""

currentdate = datetime.datetime.now()

path = os.path.dirname(os.path.abspath(__file__)) + "/Data/"

TmpDay = str(path) + "TotalApi.Call"

TmpDay2 = str(path) + "UpdateStatus.Call"

TmpMeal = str(path) + "SearchTerms.Used"

Tmpkey = str(path) + "Rq.Keywords"

Tmpword = str(path) + "Rq.Bannedword"

Tmpfolo = str(path) + "Rq.Following"

Tmpfriend = str(path) + "Rq.Friends"

Tmpbppl= str(path) + "Rq.Bannedpeople"

Tmpbw= str(path) + "Rq.Bannedword"

Session = str(path) + "Current.Session"

noresult = str(path) + "No.Result"

idsaved = str(path) + "Tweets.Sent"

doublesaved = str(path) + "Text.Sent"

restabit = 0

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

Keywords = []

Keywordsave = []

Following = []

Friends = []

banlist = []

banppl = []

bandouble = []

apicall = 0

updatecall = 0

totalcall = 0

totalupdatecall = 0

tobsnd = []

allok = 0

Totalsent = 0

checkM = 0

mcdone = 0
  
searchapi = 0

searchlimit = 0

searchdone = 0

retweetlist = []

newkeywords = []

QueueList = []

startedat = ''

time2wait = 0

totalscore = 0

totalalrdysnd = 0

totallanguage = 0

total2old = 0

totalnokeyword = 0

totalbannedwords = 0

totalff = 0

totalhf = 0

totalbannedppl = 0

twtbyuser = []


#startedat = datetime.datetime.now()

newtlist = [] 
printable = set(string.printable)
#Some Defs

def checkfile(filename):
    try:
                        file = open(filename,"r")
                        file.close()
    except:
                        print("==")
                        print("File does not exist (Tmpkey)")
                        print("Creating file")
                        print("==")
                        file = open(filename,"w")
                        file.write("")
                        file.close()

def cleanfile(filename):

    clean_lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
        clean_lines = [l.strip() for l in lines if l.strip()]

    with open(filename, "w") as f:
        f.writelines('\n'.join(clean_lines))

    file = open(filename,"r+")
    return file.read().splitlines()


def Fig(font,txt,toirc=None):
    setfont = Figlet(font=font)
    print(setfont.renderText(txt))
    if toirc:
          IrSend(txt,toirc)

def loadvars():

    global Keywords
    global Keywordsave
    global Following
    global Friends
    global banlist
    global banppl


    Fig("rev",'LoadVars()',True)
    print("\n\n\n\n")
    Fig("cybermedium",'Loading Keywords',True)
    
    print("\n\n\n")
    Fig("cybermedium","Loading Friends",True)
    print("\n\n")

    checkfile(path+"RssSave")
    lines = cleanfile(path+"RssSave")
    for saved in lines:
       RssSent.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Rss Sent Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    print("\n\n")

    checkfile(Tmpkey)
    lines = cleanfile(Tmpkey)

    for saved in lines:
           Keywords.append(saved)

    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d",'Keywords Loaded',True)
    print("*=*=*=*=*=*=*=*=*=*\n")
    time.sleep(2)
    Keywordsave = Keywords
    shuffle(Keywords)
    print("\n\n")
    Fig("cybermedium",'Loading Following',True)

    checkfile(Tmpfolo)
    lines = cleanfile(Tmpfolo)

    for saved in lines:
       Following.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Following Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    print("\n\n\n")
    Fig("cybermedium","Loading Friends",True)
    print("\n\n")

    checkfile(Tmpfriend)
    lines = cleanfile(Tmpfriend)
    for saved in lines:
       Friends.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Friends Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(2)


    print("\n\n")
    Fig("cybermedium","Loading Banned Words",True)
    print("\n\n")
    checkfile(Tmpbw)
    lines = cleanfile(Tmpbw)

    for saved in lines:
      banlist.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Banned Words Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(2)
    print("\n\n")
    Fig("cybermedium","Loading Banned Users",True)
    print("\n\n")
    checkfile(Tmpbppl)
    lines = cleanfile(Tmpbppl)
    for saved in lines:
      banppl.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Banned users Loaded,True")
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(2)

def title(screen):

    scenes = []
    effects = [
        Print(screen,
              Rainbow(screen, FigletText("* RED QUEEN *", font="alligator")),
              y=screen.height // 4 - 5),
        Print(screen,
              FigletText("-Twitter Search Bot-"),
              screen.height // 2 - 3),
        Print(screen,
              FigletText("-Crawling For InfoSec News-"),
              screen.height * 3 // 4 - 3),
    ]
    scenes.append(Scene(effects, 60))

    effects = [
        ShootScreen(screen, screen.width // 2, screen.height // 2, 100),
    ]
    scenes.append(Scene(effects, 40, clear=False))
    #scenes.append("error")

    try:
          screen.play(scenes, repeat=False, stop_on_resize=False)
    except Exception as e:
          print("Title Error:",e)
          pass


def timer(mode):
   global timeleft
   global timed
   global startedat
   if mode == 2:
     now = ''
     timesup = ''
     timeleft = ''
     timed = ''

     now = datetime.datetime.now()
     timesup = now - startedat
     timeleft = "Time Left %i / %i"% (timesup.seconds,time2wait)
     timed = timesup.seconds

     return timeleft


   if mode == 1:

        now = ''
        timesup = ''
        timeleft = ''
        timed = ''



        now = datetime.datetime.now()
        timesup = now - startedat
        timed = timesup.seconds
        return timed




def Request():

  global Keywords
  global banlist
  global banppl
  global apicall
  global Banned

  Fig("rev",'#Request()')
  
  time.sleep(0.3)
  try:
       dmlist = twitter.get_direct_messages(count=200)
  except:
       dmlist = []
  apicall = apicall + 1

  if len(dmlist) > 0:
  
        for dm in dmlist:
          Banned = 0
          Idlist(dm['id'])
          if Banned == 0:
                if "On4r4p" in str(dm['sender']['screen_name']):
                    words = []
                    users = []
                    addkey = []
          
                    Saveid(dm['id'])
                    
                    print("New msg from allowed user:", dm['id'])
                    
                    
                    print("On %s ."% dm['created_at'])
                    a = "On %s ."% dm['created_at']
                    print("You send this commande :")
                    b = "You send this commande :"
                    print(dm['text'])
                    c = dm['text']
                    items = dm['text'].split(',')
                    d = ""
                    e = ""
                    f = ""
                    g = ""
                    h = ""

                    
          
                    for sample in items:
                        if not "http" in sample and not "https" in sample and sample is not " " and len(sample) > 1:
                            if "@" in sample and not "add:" in sample and not "Add:" in sample and not "add :" in sample and not "Add :" in sample :
                                          print("You asked to Ban this user :",sample)
                                          users.append(sample.replace("@","").replace(" ",""))


                            if "Banuser" in sample or "banuser" in sample:
                              
                              print("You asked to Ban the user from that quote:")
                              d = "You asked to Ban the user from that quote:"

                              try:
                                      d = "You asked to Ban the user from that quote:"
                                      print(dm['entities']['urls'][-1]['expanded_url'])
                                      e = dm['entities']['urls'][-1]['expanded_url']
                                      if "http:" in e:
                                             name = re.split('http://twitter.com/|,|/status/| ',dm['entities']['urls'][-1]['expanded_url'])
                                      if "https:" in e:
                                             name = re.split('https://twitter.com/|,|/status/| ',dm['entities']['urls'][-1]['expanded_url'])
                                      print(name[1])
                                      f = name[1]
                                      users.append(name[1].replace("Banuser","").replace("banuser",""))
                              except:
                                    print("But no quote was found ...")

                            if "add:" in sample or "Add:" in sample or "add :" in sample or "Add :" in sample:
                                   
                                   print("You asked to add keywords :")
                     
           
                                   addkey.append(sample.split(":",1)[1])
                               
                                   h = "You asked to add Keywords :",addkey
                                   
                                   print(addkey)

                            if not "banuser"in sample and not "Banuser" in sample and not "add:" in sample and not "Add:" in sample and not "add :" in sample and not "Add :" in sample :
                                          words.append(sample)


                        if "http" in sample and sample is not " " and len(sample) > 1:
                              endcmd = sample.split("http")
                              if "@" in endcmd and not "add:"in endcmd and not "Add:" in endcmd and not "add :" in endcmd and not "Add :" in endcmd:
                                          print("You asked to Ban this user :",endcmd[0])
                                          users.append(endcmd[0].replace("@","").replace(" ",""))


                              if "Banuser" in endcmd or "banuser" in endcmd:
                                   
                                   print("You asked to Ban the user from that quote:")
                                   d = "You asked to Ban the user from that quote:"

                                   try:
                                      d = "You asked to Ban the user from that quote:"
                                      print(dm['entities']['urls'][-1]['expanded_url'])
                                      e = dm['entities']['urls'][-1]['expanded_url']
                                      if "http:" in e:
                                             name = re.split('http://twitter.com/|,|/status/| ',dm['entities']['urls'][-1]['expanded_url'])
                                      if "https:" in e:
                                              name = re.split('https://twitter.com/|,|/status/| ',dm['entities']['urls'][-1]['expanded_url'])
                                              print(name[1])
    
                                              f = name[1]
                                              users.append(name[1])
                                   except:
                                         print("But no quote was found ...")

                              if "add:" in endcmd or "add :" in endcmd or "Add :" in endcmd or "Add:" in endcmd and len(sample) > 0:
                                          addkey.append(endcmd[0].split(":",1)[1])
                                          print("You asked to add keywords :")
                                          h = "You asked to add Keywords :",addkey
                                          print("You asked to add Keywords :",addkey)

                              if not "banuser"in endcmd and not "Banuser" in endcmd and not "add:" in endcmd and not "Add:" in endcmd and not "add :" in endcmd and not "Add :" in endcmd :
                                          words.append(endcmd[0])

      
                    g = "%i Banned topic , %i Banned Users Detected and %i Keywords Detected" % (len(words),len(users),len(addkey))
                    print("%i Banned topic , %i Banned Users Detected and %i Keywords Detected" % (len(words),len(users),len(addkey)))


                       
                      
                     

           
                    checkfile("Request.log")
          
                    file = open(path+"Request.log","a")
                    file.write("\n"+"#####"+"\n"+str(a)+"\n"+str(b)+"\n"+str(c)+"\n"+str(d)+"\n"+str(e)+"\n"+str(f)+"\n"+str(g)+"\n"+str(h)+"\n"+"Users: "+str(users)+"\n"+"Topic: "+str(words)+"\n"+"#####"+"\n")
                    file.close

                    checkfile(Tmpbppl)
                    checkfile(Tmpword)
                    checkfile(Tmpkey)

                    file = open(Tmpbppl,"a")

                    for item in users:
                         file.write("\n"+str(item.replace(" ","").replace(",","")))
                    file.close()
  


                    file = open(Tmpword,"a")
      
                    for item in words:
                         file.write("\n"+str(item))
                    file.close()

                    file = open(Tmpkey,"a")

                    for item in addkey:
                                file.write("\n"+str(item))
                    file.close()


                    
                     
                    Fig("cybermedium",'Added new items to files')
                    
  
                    time.sleep(2)

                    Idlist(dm['id'])

                else:
                    print("%s You re not the boss of me now !"% dm['sender']['screen_name'])

      
  else:
          
          Fig("cybermedium",'0 new instruction has been sent to me',True)
          

  Banned = 0

def SaveDouble(text):
                
                

                Fig("rev",'SaveDouble()')
                
             #time.sleep(0.3)

                text = text.replace("\n"," ")
                checkfile(doublesaved)

                file = open(doublesaved,"a")
                file.write("\n"+str(text))
                file.close()

                
                
                print("*=*=*=*=*=*=*=*=*=*")
                print("SAVING TWEET TO TMP :",text)
                Fig("larry3d",'Saved')
                print("*=*=*=*=*=*=*=*=*=*")
                
                
                #time.sleep(0.3)



def CheckDouble():


    global bandouble

    Fig("rev",'CheckDbl()',True)
    

    checkfile(doublesaved)

    lines = cleanfile(doublesaved)

    for saved in lines:

                bandouble.append(saved)
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d",'BanDouble Updated',True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(2)



def flushtmp():

  global apicall
  global updatecall
  global twitter

  goflush = 0

  Fig("rev",'flushtmp()',True)

  time.sleep(3)
  if os.path.exists(Session):

    file = open(Session,"r")
    datefile = file.read()
    date_object = datetime.datetime.strptime(str(datefile), '%Y-%m-%d %H:%M:%S.%f')
    Laps = (currentdate - date_object)

    print(Laps)

    try:
      if (currentdate - date_object).total_seconds() > 86400:
           goflush = 1
    except Exception as e:
      print(e)
      
      Fig("cybermedium",'No need to flush',True)
      
      time.sleep(2)

    if goflush == 1:


      
      print("==")
      Fig("basic",'Flushing Temps Files',True)
      print("==")
      
      
      file.close()
      try:
                          text="New Session ! " + str(currentdate)
                          IrSend(text)
                          print("")
                          Fig("basic",'Status sent !')

      except Exception as e:
                          print(e)
                          print("fuck")
                          time.sleep(5)
      time.sleep(3)

      os.remove(Session)


      if os.path.exists(TmpDay):
                os.remove(TmpDay)


      if os.path.exists(TmpDay2):
                os.remove(TmpDay2)


      if os.path.exists(TmpMeal):
                os.remove(TmpMeal)

      
      
      print("==")
      Fig("basic",'Saving current date',True)
      print(currentdate)
      print("==")
      
      
      time.sleep(5)
      file = open(Session,"w")
      file.write(str(currentdate))
      file.close()



      Fig("cybermedium",'Done Flushing',True)
      time.sleep(2)
      
    else:
      lfts = 86400 - Laps.seconds

      
       
      print("==")
      Fig("basic",'Starting from Last Session',True)
      
      print("Numbers of seconds since the first api call :",Laps.seconds)
      print("%i Seconds left until Twitter flushs apicalls :" % lfts)
      print("==")
      
      
      
      time.sleep(5)

  else:
    
    
    print("==")
    Fig("basic",'New Session Started',True)
    print(currentdate)
    print("==")
    
    
    time.sleep(5)
    file = open(Session,"w")
    file.write(str(currentdate))
    file.close()


def checkmenu(wordlist):
  Fig("rev",'CheckMenu()',True)
  
  time.sleep(3)
  try:
                global newkeywords
                global checkM
                oldlen = len(wordlist)
                file = open(noresult,"r")
                lines2 = file.read().splitlines()
                lenmatch2 = len(set(lines2) & set(wordlist))

                
                print("==")
                Fig("doom",'Removing Last Searches with No Result',True)
                
                time.sleep(0.5)
                while lenmatch2 >0:
                        Fig("digital","Found %i occurences :" % lenmatch2,True)
                        set(lines2) & set(wordlist)
                        
                        
                        time.sleep(1)
                        Fig("digital","Removing No result from list ...",True)
                        wordlist = list(set(wordlist) - set(lines2))
                        
                        time.sleep(1)
                        
                        Fig("digital","New lenght of searchlist : " + str(len(wordlist)) + " (Was " + str(oldlen) + " )",True)
                        print("==")
                        
                        time.sleep(1)
                        lenmatch2 = len(set(lines2) & set(wordlist))
                file.close()

                Fig("doom",'Removing Old Searches',True)
                
                time.sleep(0.5)
                newkeywords = wordlist
                
                print("==")
                Fig("cybermedium",'Removed successfully',True)
                print("==")
                time.sleep(1)

                oldlen = len(wordlist)
                file = open(TmpMeal,"r")
                lines = file.read().splitlines()
                lenmatch = len(set(lines) & set(wordlist))

                while lenmatch >0:
                    Fig("digital","Found %i occurences :" % lenmatch,True)
                    set(lines) & set(wordlist)
                    
                    
                    time.sleep(1)
                    Fig("digital","Removing from search list ...",True)
                    wordlist = list(set(wordlist) - set(lines))
                    
                    time.sleep(1)
                    
                    Fig("digital"+"New lenght of searchlist : " + str(len(wordlist)) + " (Was " + str(oldlen) + " )",True)
                    print("==")
                    
                    time.sleep(1)
                    lenmatch = len(set(lines) & set(wordlist))
                file.close()
                print("==")
                Fig("cybermedium",'Removed successfully',True)
                print("==")
                checkM = 1
                time.sleep(1)
                newkeywords = wordlist
  except Exception as e:
    print(e)

    print("==")
    Fig("basic",'No previous searchs found for today',True)
    print("==")
    time.sleep(1)


def lastmeal(lastsearch):

    global mcdone

    if mcdone == 0:
                  Fig("rev",'LastSearch()',True)
                  time.sleep(3)
                  checkfile(TmpMeal)
  
                  file = open(TmpMeal,"a")
                  for words in lastsearch:
                    file.write(words + "\n")
                    Fig("digital","Marking " + words + " as old . ")
                  file.close()
                  mcdone = mcdone + 1
                  time.sleep(0.3)
    else:
                  print("==")
                  Fig("cybermedium",'Saved already')
                  print("==")

def SaveTotalCall(call,update):
    Fig("rev",'SaveTotalCall()')
    time.sleep(0.3)
    global totalcall
    global updatecall
    global totalupdatecall
    checkfile(TmpDay)
    file = open(TmpDay,"a+")
    lines = file.read().splitlines()
    lenfile = len(lines)
    try:
         lastitem = lines[lenfile -1]
    except:
          lastitem = 0
    print("==")
    print("Last Total saved : ",lastitem)
    newitem = int(lastitem) + int(call)
    totalcall = newitem
    finalitem = str(newitem) + "\n"
    Fig("digital","Saving new Total : " + str(finalitem))
    print("==")
    file.write(finalitem)
    file.close()
    time.sleep(0.3)
    checkfile(TmpDay2)

    file2 = open(TmpDay2,"a+")
    lines2 = file2.read().splitlines()
    lenfile2 = len(lines2)
    try:
         lastitem2 = lines2[lenfile2 -1]
    except:
          lastitem2 = 0
    print("==")
    print("Last Update Total saved : ",lastitem2)
    newitem2 = int(lastitem2) + int(update)
    totalupdatecall = newitem2
    finalitem2 = str(newitem2) + "\n"
    print("Saving new Update Total : ",finalitem2)
    print("==")
    file2.write(finalitem2)
    file2.close()
    Fig("basic",'Done Saving Calls')

    time.sleep(0.3)
    
    
    
    



def IrSweet():
     global GOGOGO
     global Irc
     global CHANNEL

     HOST = "irc.mindforge.org"
     #HOST = "irc.dal.net"
     PORT = 6667
     NICK = "BlueKing"
     IDENT = "BlueKing"
     REALNAME = "BlueKing"
     PASS = ""
     CHANPASS = ""
     MASTER = "On4r4p"
     CHANNEL = "#RedQueen"
     #NICKSERV = "PRIVMSG NickServ@services.dal.net :"
     NICKSERV = "PRIVMSG NickServ :"
     Konnected = False
     #KonTrigger = "End of /MOTD "
     KonTrigger = "Have a nice stay!"
     Identified = False
     IdentTrigger = "Password accepted"
     Joined = False
     IrcSocket = False
     Irc = ""
     Buffer = ""


     while IrcSocket == False:
       try:
          Fig("digital","\n--Connecting to :"+str(HOST) +"--\n")
          time.sleep(1)
          Irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          Irc.connect((HOST, PORT))

          Irc.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
          Irc.send(bytes("USER %s %s woot :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
          time.sleep(1)
          IrcSocket = True
       except Exception as e:
               print("connect() Error : ",e)
               continue

     last_ping = time.time()
     threshold = 3 * 60

     while IrcSocket == True:
       if SHUTDOWN is False:
          try:
               Buffer = Irc.recv(1024).decode("UTF-8")
               if len(Buffer) > 1:

                    print("Buffer: ",Buffer)
          
               if Buffer.find("PING") != -1:
                    Fig("digital","\n--PINGED--\n")
                    tmp = Buffer.split("PING :")[1]
                    Irc.send(bytes("PONG :"+ tmp +"\r\n" ,"UTF-8" ))
                    Fig("digital","\n--PONG :"+ str(tmp) +" --\n")
                    last_ping = time.time()

               if Buffer.find("ERROR :Closing Link:") != -1:
                   Fig("digital"+"\n--TimeOut--\n\n--Restablishing Connection--\n")
                   return IrSweet()

               if Buffer.find(KonTrigger) != -1 and Konnected is False:
                    Konnected = True
                    Fig("digital","\n--Connected--\n")

               if Buffer.find(IdentTrigger) != -1 and Identified is False:
                    Identified = True
                    Fig("digital","\n--Authentified--\n")

               if Identified == False and Konnected is True:
                    time.sleep(2)
                    Fig("digital","\n--Sending CREDENTIAL--\n")
                    Irc.send(bytes("%sIDENTIFY %s\r\n" % (NICKSERV,PASS), "UTF-8"))
                    time.sleep(2)

               if Joined == False and Identified == True and Konnected == True:
                    print("\n--Joining "+str(CHANNEL)+"--\n")
                    Irc.send(bytes("JOIN %s %s\r\n" % (CHANNEL,CHANPASS), "UTF-8"));
                    time.sleep(2)
                    Irc.send(bytes("PRIVMSG %s :<Knock Knock Neo ...>\r\n" % CHANNEL, "UTF-8"))
                    time.sleep(2)
                    Irc.send(bytes("PRIVMSG %s :<The Matrix Has You.>\r\n" % CHANNEL, "UTF-8"))
                    time.sleep(2)
                    Irc.send(bytes("PRIVMSG %s :<Follow The White Rabbit.>\r\n" % CHANNEL, "UTF-8"))
                    time.sleep(2)
                    Fig("digital","\n--Joined--\n")
                    Joined = True
               if (time.time() - last_ping) > threshold:
                    Fig("digital","\n--TimeOut--\n\n--Restablishing Connection--\n")
                    return IrSweet()

               if Joined is True and Identified is True and Konnected is True:
                    GOGOGO = True

          except Exception as e:
               print("Error :",e)
       else:
          sys.exit(0)


def Feeds(ttl):
     global RssSent

     fluxlist = ["http://www.securityfocus.com/rss/vulnerabilities.xml","http://googleprojectzero.blogspot.com/feeds/posts/default","https://rss.packetstormsecurity.com/","http://seclists.org/rss/fulldisclosure.rss","https://dankaminsky.com/feed/","http://seclists.org/rss/bugtraq.rss","https://www.exploit-db.com/rss.xml","https://foxglovesecurity.com/feed/","https://www.debian.org/security/dsa","http://www.us-cert.gov/ncas/alerts.xml","http://www.ubuntu.com/usn/atom.xml","http://www.freebsd.org/security/rss.xml","https://nvd.nist.gov/download/nvd-rss.xml","https://lcamtuf.blogspot.com/feeds/posts/default","http://blog.erratasec.com/feeds/posts/default","http://krebsonsecurity.com/feed/","http://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches","https://isc.sans.edu/xml.html","https://tools.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml","https://aws.amazon.com/security/security-bulletins/feed","https://www.grahamcluley.com/feed","https://feeds.feedburner.com/TroyHunt","https://nakedsecurity.sophos.com/feed","https://labsblog.f-secure.com/feed","https://www.wired.com/feed/category/security/latest/rss","http://www.theregister.co.uk/security/headlines.atom","http://threatpost.com/feed","https://securityintelligence.com/feed","http://www.tripwire.com/state-of-security/feed","http://www.infosecisland.com/rss.html","https://www.securemac.com/feed","http://www.itsecurityguru.org/feed","http://feeds.feedburner.com/govinfosecurity/com","http://www.symantec.com/connect/item-feeds/blog/691,2261/feed/all/en/all","http://www.pandasecurity.com/mediacenter/feed","https://blog.malwarebytes.org/feed","https://isc.sans.edu/newssummaryrss.xml","https://www.darknet.org.uk/feed/","https://blog.rootshell.be/feed/","https://feeds.pcmag.com/Rss.aspx/SectionArticles?sectionId=28026","https://www.bleepingcomputer.com/feed/"]
     counter = 0

     for flux in fluxlist:
         if counter <= ttl:
            try:
               rss = feedparser.parse(flux)
     
               for news in rss.entries:
                    time.sleep(1)
                    counter = counter + 1
                    format = str(news.title)+" : "+str(news.link)
                    if format not in RssSent:
                         RssSent.append(format)
                         IrSend(format)
                         with open(path+"RssSave","a") as f:
                              f.write("\n")
                              f.write(str(format))
            except Exception as e:
               time.sleep(1)
               counter = counter + 1
               print("Rss Error %s : %s"%(flux,e))
               IrSend("Rss Error "+str(flux)+" : "+str(e))
         else:
               return

def IrSend(content,dontprint = None):

        global Irc
        if not dontprint:
          Fig("rev","IrSend()")
          print("==")
          Fig("epic","Tweet Loaded!")
          print("==")
        
        time.sleep(1)
        Fig("digital","\n--Sending :"+str(content)+"--\n")
        Irc.send(bytes("PRIVMSG %s :** %s **\r\n" % (CHANNEL,content), "UTF-8"))
        Fig("digital","\n--Done--\n")
        return

def Stat2Irc(time2wait):
#  Flood = randint(0,3)
#  if Flood == 3:
       apicalltxt = "Total RT Sent: " + str(Totalsent)
       IrSend(apicalltxt)
       time.sleep(1)
       updatecalltxt = "Current Update Calls: " + str(updatecall)
       IrSend(updatecalltxt)
       time.sleep(1)
       totalcalltxt = "Total Calls: " +str(totalcall)
       IrSend(totalcalltxt)
       time.sleep(1)
       totalupdatecalltxt = "Total Update Calls: " + str(totalupdatecall)
       IrSend(totalupdatecalltxt)
       time.sleep(1)
       banppltxt = "Banned Users in list: " + str(len(banppl))
       IrSend(banppltxt)
       time.sleep(1)
       bandoubletxt = "Total Banned (Double): "+str(totalalrdysnd)
       IrSend(bandoubletxt)
       time.sleep(1)
       banlisttxt = "Banned Words in list: "+str(len(banlist))
       IrSend(banlisttxt)
       time.sleep(1)
       Friendstxt = "Nbr of friends: "+str(len(Friends))
       IrSend(Friendstxt)
       time.sleep(1)
       Followingtxt = "Users Followed: "+str(len(Following))
       IrSend(Followingtxt)
       time.sleep(1)
       Keywordstxt = "Keywords in list: "+str(len(Keywords))
       IrSend(Keywordstxt)
       time.sleep(1)
       moyscoretxt = "Current Tweets collected: " + str(len(moyscore))
       IrSend(moyscoretxt)
       time.sleep(1)
       NbrRetweettxt = "Tweets sent to irc:"+str(len(retweetlist))
       IrSend(NbrRetweettxt)
       time.sleep(1)
       totalscoretxt = "Total Banned (Score): "+str(totalscore)
       IrSend(totalscoretxt)
       time.sleep(1)
       totallanguagetxt = "Total Banned (Language): " +str(totallanguage)
       IrSend(totallanguagetxt)
       time.sleep(1)
       total2oldtxt = "Total Banned (Too old): "+str(total2old)
       IrSend(total2oldtxt)
       time.sleep(1)
       totalnokeywordtxt = "Total Banned (No Keywords): "+str(totalnokeyword)
       IrSend(totalnokeywordtxt)
       time.sleep(1)
       totalbannedwordstxt = "Total Banned (Words): "+str(totalbannedwords)
       IrSend(totalbannedwordstxt)
       time.sleep(1)
       totalfftxt = "Total Banned (FF): "+str(totalff)
       IrSend(totalfftxt)
       time.sleep(1)
       totalhftxt = "Total Banned (###):"+str(totalhf)
       IrSend(totalhftxt)
       time.sleep(1)
       totalbannedppltxt = "Total Banned Users: "+str(totalbannedppl)
       IrSend(totalbannedppltxt)
       time.sleep(1)
       Feeds(time2wait)

def limits():
  Fig("rev",'Limits()')

#  #time.sleep(0.3)
  global apicall
  global updatecall
  global totalupdatecall
  global totalcall
  global twitter
  global searchlimit
  global restabit
  global waithour
  global waithalf
  global time2wait
  global startedat
  global allok
  global tmpbypass
  startedat = datetime.datetime.now()

  if waithour == 1:


                print("****************************************")
                print("****************************************")
                Fig("epic",'CURRENT LIMITS ARE REACHED !!')
                print("")
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(apicall,updatecall)
                Fig("cybermedium",'Resetting current apicalls')


                Fig("cybermedium",'Login Out')
                Fig("cybermedium",'Waiting 60 minutes')
                print("\n\n\n\n")

                Stat2Irc(3600)
                updatecall = 0
                apicall = 0
                searchlimit = 0
                restabit = 0
                waithour = 0

                Fig("cybermedium",'Waking up ..')
                #time.sleep(0.3)
                print("")
                twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
                print("\n\n")

  if restabit == 1:
                print("****************************************")
                print("****************************************")
                Fig("epic",'Mysterious Error !!!',True)
                print("")
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(apicall,updatecall)
                Fig("cybermedium",'Resetting current apicalls')

                Fig("cybermedium",'Login Out')
                Fig("cybermedium",'Waiting 5 minutes')
                Stat2Irc(3600)

                updatecall = 0
                apicall = 0
                searchlimit = 0
                restabit = 0


                Fig("cybermedium",'Waking up ..')
    #time.sleep(1)
                print("")
                twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
                

  

  if searchlimit == 1:

    #Request()
                print("****************************************")
                print("****************************************")
                
                Fig("epic",'SEARCH LIMITS ALMOST REACHED')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(apicall,updatecall)
                Fig("cybermedium",'Resetting current apicalls')


                Fig("cybermedium",'Login Out')
                
                Fig("cybermedium",'Waiting 15 minutes')
                Stat2Irc(900)

                updatecall = 0
                apicall = 0
                searchlimit = 0

                Fig("cybermedium",'Waking up ..')
                print("")
                twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
                
                print("****************************************")
                print("****************************************\n\n\n\n")



  if apicall >= 165:
    
   
    #Request()
    print("****************************************")
    print("****************************************")
    
    Fig("epic",'CURRENT LIMITS ALMOST REACHED')
    Fig("cybermedium",'Saving Total Calls to file')
    SaveTotalCall(apicall,updatecall)
    Fig("cybermedium",'Resetting current apicalls')


    Fig("cybermedium",'Login Out')
    

    if waithalf != 1:
      Fig("cybermedium",'Waiting 15 minutes')

      Stat2Irc(900)
    else:
      Fig("cybermedium",'Waiting 30 minutes')
      Stat2Irc(1800)
      
    updatecall = 0
    apicall = 0
    Fig("cybermedium",'Waking up ..')
    print("")
    twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
    
    print("****************************************")
    print("****************************************\n\n\n\n")



  if totalcall > 8888:

    #Request()
                print("****************************************")
                print("****************************************")

                

                
                Fig("epic",'CURRENT LIMITS ALMOST REACHED (total)')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(apicall,updatecall)
                Fig("cybermedium",'Resetting current apicalls')
                allok = 1
                tmpbypass = 1
                

  if totalupdatecall > 2223:
    #Request()

                print("****************************************")
                print("****************************************")
                Fig("epic",'CURRENT LIMITS ALMOST REACHED (update)')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(apicall,updatecall)
                Fig("cybermedium",'Resetting current apicalls')
                allok = 1

  
  print("===================")
  Fig("cybermedium",'Ok')
  print("===================")
  #time.sleep(1)




def Ban(tweet,sender,id,bio):


  global Banned
  global totalnokeyword
  global totalbannedwords
  global totalalrdysnd
  global totalff
  global totalhf
  global totalbannedppl


  ushallpass = 0

  Fig("rev",'Ban()')
  
  print("*=*=*=*=*=*=*=*=*=*")

  if Banned == 0:

                for item in emolist:
                        emotst = tweet.count(item)
                        if emotst > 0:
                                print("Found this emoji : ",item)
                                Banned = 1
                if Banned == 1:
                        Fig("cybermedium",'This tweet contains an Emoticon and must die . ')
                        
                        print(tweet)
                        
                        
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")



  if Banned == 0:
     luck = randint(0,100)
     print("Luck Score (/100)= ",luck)
     for mustbe in Keywordsave:
      if ushallpass == 0:
           
                    pos = 0
                    lng = int(len(mustbe))
                    if lng >= 12:
                      half = lng / 2
                    else:
                          half = lng - 1
                    next = int(half) + pos
                    sample = mustbe[pos:int(half)]
                    maxpos = pos + int(len(sample))
                    while maxpos < int(lng):
                         try:
                             if len(sample) <= 3:
                                                pos = pos + 1
                                                next = int(half) + pos
                                                sample = mustbe[pos:int(next)]
                                                maxpos = pos + int(len(sample))


                             if str(sample.lower()) in str(tweet.lower()) and sample.count(" ") < 2:
                                    
                                    Fig("cybermedium",'Found Keywords :')
                     
                                    print("Sample : ",sample)
                                    
                                    Fig("basic",'You shall Pass')
                                    print("*=*=*=*=*=*=*=*=*=*")
                                    ushallpass = 1
                                    maxpos = lng
                             else:
                #print "Sample : ",sample
                                    pos = pos + 1
                                    next = int(half) + pos
                                    sample = mustbe[pos:int(next)]
                                    maxpos = pos + int(len(sample))
                         except:
                                                pos = pos + 1
                                                next = int(half) + pos
                                                sample = mustbe[pos:int(next)]
                                                maxpos = pos + int(len(sample))
     if ushallpass != 1 and luck > 50:
                                
                                Fig("cybermedium",'Did not found any Keyword in tweet.')
                                totalnokeyword = totalnokeyword + 1
                                Banned = 1
     print("*=*=*=*=*=*=*=*=*=*")

  for forbid in banlist:
    if Banned == 0:
      if str(forbid.lower()).replace(":"," ").replace(","," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("'"," ").replace('"',' ').replace("-"," ").replace("_"," ") in str(tweet.lower()).replace(":"," ").replace(","," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("'"," ").replace('"',' ').replace("-"," ").replace("_"," "):

        
        Fig("cybermedium",'This tweet contains banned words :')
        
        print(tweet)
        
        print("** %s **" % str(forbid))
        
        Fig("",'Going To Trash ...')
        print("*=*=*=*=*=*=*=*=*=*")
        
        Banned = 1
        totalbannedwords = totalbannedwords + 1
      #time.sleep(0.3)
        for forbid in banlist:
            if Banned == 0:
                if str(forbid.lower()) in str(bio.lower()):

                        
                        Fig("cybermedium",'This user profile contains banned words :')
                        
                        print(bio)
                        
                        print("** %s **" % str(forbid))
                        
                        Fig("cybermedium",'Going To Trash ...')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = 1
                        totalbannedwords = totalbannedwords + 1
                        #time.sleep(0.3)

        for forbid in banppl:
           if Banned == 0:
                if str(forbid.lower()) in str(sender.lower()):

                        
                        Fig("cybermedium",'This tweet is from a banned user :')
                        
                        print(tweet)
                        
                        print("** %s **" % forbid)
                        
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = 1
                        totalbannedppl = totalbannedppl + 1
                        #time.sleep(3)

        for forbid in bandouble:
           if Banned == 0:
                if forbid in tweet:

                        
                        Fig("cybermedium",'This tweet is Identical to a Previous tweet :')
                        
                        print(tweet)
                        
                        Saveid(id)
                        
                        Fig("",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = 1
                        totalalrdysnd = totalalrdysnd + 1
                        #time.sleep(0.3)


  for item in bandouble:

    if Banned == 0 and len(item) > 10:
      pos = 0
      lng = len(item)
      half = lng / 2
      next = int(half) + pos
      sample = item[pos:int(half)]
      maxpos = pos + int(len(sample))

      while int(maxpos) < int(lng):
        try:
          if str(sample) in str(tweet) and str(sample) != " ":
                          
                          Fig("cybermedium",'Some parts are Identicals to a Previous Tweet :')
                          print("Tweet :",tweet)
                          
                          print("Found Matched :",sample)
                          Saveid(id)
                          
                          Fig("cybermedium",'Going To Trash')
                          print("*=*=*=*=*=*=*=*=*=*")


                          
                          maxpos = int(lng)
                          Banned = 1
                          totalalrdysnd = totalalrdysnd + 1
          else:
              pos = pos + 1
              next = int(half) + pos
              sample = item[pos:int(next)]
              maxpos = pos + int(len(sample))
        except:
                                pos = pos + 1
                                next = int(half) + pos
                                sample = item[pos:int(next)]
                                maxpos = pos + int(len(sample))



  if Banned == 0:
    if tweet.count("@") >= 3:


                  Fig("basic",'Follow Friday')
                  Fig("cybermedium",'Going To Trash')
                  print("*=*=*=*=*=*=*=*=*=*")
                  
                  Banned = 1
                  totalff = totalff +1
      #time.sleep(0.5)

    if tweet.count("#") >= 3:

                  Fig("basic",'HashTags Fever')
                  Fig("cybermedium",'Going To Trash')
                  print("*=*=*=*=*=*=*=*=*=*")
                  
                  Banned = 1
                  totalhf = totalhf + 1
                  #time.sleep(0.5)

    if twtbyuser.count(str(sender)) >= 2:
                        Fig("basic",'Too many Tweets From this user ')
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = 1
                        totalbannedppl = totalbannedppl + 1
                        #time.sleep(0.5)
    else:
                        figy = "Nbr of tweets for this user : ",str(twtbyuser.count(sender))
                        Fig("cybermedium",str(figy))
                        print("*=*=*=*=*=*=*=*=*=*")
      #time.sleep(0.3)


  if Banned == 0:

                Fig("speed",'Good To Go !!')
                print("*=*=*=*=*=*=*=*=*=*")
                
    #time.sleep(0.3)


def Saveid(id):

                Fig("rev",'Saveid()')
                
#    #time.sleep(0.3)

                checkfile(idsaved)

                file = open(idsaved,"a")
                file.write("\n"+str(id))
                file.close()

                
                
                print("*=*=*=*=*=*=*=*=*=*")
                print("Id :",id)
                Fig("larry3d",'Saved')
                print("*=*=*=*=*=*=*=*=*=*")
                
                
    #time.sleep(0.3)


def Idlist(id):
    global Banned
    global alreadysend
    global Totalsent
    global doneid

    Fig("rev",'Idlist()')
#    #time.sleep(0.3)

    alreadysend = 0
    if doneid == 0:
        checkfile(idsaved)


        empty = cleanfile(idsaved)


        Totalsent = sum(1 for line in open(idsaved))
        doneid = 1



    file = open(idsaved,"r+")
    lines = file.read().splitlines()

    for saved in lines:

       if saved != "\n" or saved != "":
         if str(saved) in str(id):

               
               print("*=*=*=*=*=*=*=*=*=*")
               print("Id from file :",saved)
               print("tweet id :",id)
               print("*=*=*=*=*=*=*=*=*=*")
               
               Banned = 1
               alreadysend = 1
                #time.sleep(2)


    if alreadysend == 0:

      
      print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
      Fig("basic",'Unknown Tweet ID')

      print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
      
      #time.sleep(0.3)





def Scoring(tweet,search):

  global apicall
  global totalcall
  global updatecall
  global totalupdatecall
  global Banned
  global bandouble
  global alreadysend
  global moyscore
  global Rthourtweet
  global totalscore
  global totalalrdysnd
  global totallanguage
  global total2old
  global twtbyuser
  global tobsnd
  global restabit
  global twitter
  global fuck
  global waithour
  global waithalf
  global rtsave

  Bouffon = 0
  Score = 0
  Banned = 0
  alreadysend = 0
  now = datetime.datetime.now()

  
  
  
  Fig("rev",'Scoring()')
  
  ##time.sleep(0.2)

  
  
  
  print("*************************************************************************************")
  Fig("basic",'Starting Scoring function')
  print("")

  if 'screen_name' in tweet['user'] :
                        tstjester = tweet['user']['screen_name']
                        if tstjester == "th3j35t3r":
                               Bouffon = 1





  if len(tweet['text']) < 70 :
                                Banned = 1
                                
                                Fig("cybermedium",'NOT ENOUGH TEXT')
                                
                                
                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
  if Banned == 0 or Bouffon == 1:
    if 'retweet_count' in tweet:

      print("##")
      print("This tweet has been retweeted %i times " % tweet['retweet_count'])
      print("##")
      luck = randint(0,6)
      if tweet['retweet_count'] < 1 and luck != 1:
                                Banned = 1
                                
                                Fig("cybermedium",'NOT ENOUGH RETWEET')
                                
                                
                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
           ##time.sleep(0.2)

      if tweet['retweet_count'] < 1 and luck == 1:
                                
                                Fig("cybermedium",'Not enough retweet')
                                
                                
                                Fig("cybermedium",'But lets give it a chance ...')
                                print("*=*=*=*=*=*=*=*=*=*")

                                

      if tweet['retweet_count'] >= 1 and tweet['retweet_count'] <= 23:
                        Score = Score + int(tweet['retweet_count'])
                        
                        if tweet['retweet_count'] > 23 and tweet['retweet_count'] <= 30:
                                Score = Score + 23 + 3
                        if tweet['retweet_count'] > 30 and tweet['retweet_count'] <= 40:
                                Score = Score + 23 + 4
                        if tweet['retweet_count'] > 40 and tweet['retweet_count'] <= 50:
                                Score = Score + 23 + 5
                        if tweet['retweet_count'] > 50 and tweet['retweet_count'] <= 50:
                                Score = Score + 23 + 6
                        if tweet['retweet_count'] > 60 and tweet['retweet_count'] <= 70:
                                Score = Score + 23 + 7
                        if tweet['retweet_count'] > 70 and tweet['retweet_count'] <= 80:
                                Score = Score + 23 + 8
                        if tweet['retweet_count'] > 80 and tweet['retweet_count'] <= 90:
                                Score = Score + 23 + 9
                        if tweet['retweet_count'] > 90 and tweet['retweet_count'] <= 100:
                                Score = Score + 23 + 10
                        if tweet['retweet_count'] > 100 and tweet['retweet_count'] <= 110:
                                Score = Score + 23 + 11
                        if tweet['retweet_count'] > 110 and tweet['retweet_count'] <= 120:
                                Score = Score + 23 + 12
                        if tweet['retweet_count'] > 120 and tweet['retweet_count'] <= 130:
                                Score = Score + 23 + 13
                        if tweet['retweet_count'] > 130 and tweet['retweet_count'] <= 140:
                                Score = Score + 23 + 14
                        if tweet['retweet_count'] > 140 and tweet['retweet_count'] <= 150:
                                Score = Score + 23 + 15
                        if tweet['retweet_count'] > 150 and tweet['retweet_count'] <= 160:
                                Score = Score + 23 + 16
                        if tweet['retweet_count'] > 160 and tweet['retweet_count'] <= 170:
                                Score = Score + 23 + 17
                        if tweet['retweet_count'] > 170 and tweet['retweet_count'] <= 180:
                                Score = Score + 23 + 18
                        if tweet['retweet_count'] > 180 and tweet['retweet_count'] <= 190:
                                Score = Score + 23 + 19
                        if tweet['retweet_count'] > 190 and tweet['retweet_count'] <= 200:
                                Score = Score + 23 + 20
                        if tweet['retweet_count'] > 200 and tweet['retweet_count'] <= 210:
                                Score = Score + 23 + 21
                        if tweet['retweet_count'] > 210 and tweet['retweet_count'] <= 223:
                                Score = Score + 23 + 23
                        if tweet['retweet_count'] > 623:
                                 
                                
                                Fig("cybermedium",'Too many Fav checking if this tweet is from a known user or friend..')
                                
                                
                                coop = tweet['user']['screen_name']
                                nogo = 1
                                
                                print("##")

                                print("##")
                                

                                if coop in Following:
                                        print("##")
                                        print("This tweet is from a known user : ",tweet['user']['screen_name'])
                                        print("##")
                                        Score = Score + 123
                                        nogo = 0
                                if coop in Friends:
                                        print("##")
                                        print("This tweet is from a friend : ",tweet['user']['screen_name'])
                                        print("##")
                                        nogo = 0
                                        Score = Score + 123
                                if nogo == 1:
                                        print("Nop ...")
                                        
                                        print("Too many retweets to be legit.")
                                        Score = Score - 232
                                        Banned = 1


           ##time.sleep(0.2)

      else:
           pass


                                




  if 'entities' in tweet:
     if Banned == 0 or Bouffon == 1:
               pass

#               if 'symbols' in tweet['entities'] and len(tweet['entities']['symbols']) > 0:
#                        print "##" print "This tweet contains a Symbol and must die for no reason. " print "##" Banned = 1 time.sleep(1) 
#      print

     if Banned == 0 or Bouffon == 1:
      nogo = 0
      if 'urls' in tweet['entities'] and len(tweet['entities']['urls']) > 0:
               print("##")
               print("This tweet contains a link : ",tweet['entities']['urls'][-1]['expanded_url'])
               print("##")
               Score = Score + 3
               if 'hashtags' in tweet['entities'] and len(tweet['entities']['hashtags']) > 0:
                        print("##")
                        print("This tweet contains Hashtag : ",tweet['entities']['hashtags'][-1]['text'])
                        print("##")
                        Score = Score + 1


               if 'media' in tweet['entities'] and len(tweet['entities']['media']) > 0:
                        print("##")
                        print("This tweet contains Media : ",tweet['entities']['media'][-1]['media_url'])
                        print("##")
                        Score = Score + 3

               if tweet['favorite_count'] > 0:

                        print("##")
                        print("This tweet has been fav : ",tweet['favorite_count'])
                        print("##")
                        Score = Score + 1
                        fav = tweet['favorite_count']
                        if fav > 1 and fav <= 23:
                              Score = Score + int(fav)
                        if fav > 23 and fav <= 30:
                              Score = Score + 23 + 3
                        if fav > 30 and fav <= 40:
                                Score = Score + 23 + 4
                        if fav > 40 and fav <= 50:
                                Score = Score + 23 + 5
                        if fav > 50 and fav <= 60:
                                Score = Score + 23 + 6
                        if fav > 60 and fav <= 70:
                                Score = Score + 23 + 7
                        if fav > 70 and fav <= 80:
                                Score = Score + 23 + 8
                        if fav > 80 and fav <= 90:
                                Score = Score + 23 + 9
                        if fav > 90 and fav <= 100:
                                Score = Score + 23 + 10
                        if fav > 100 and fav <= 110:
                                Score = Score + 23 + 11
                        if fav > 110 and fav <= 120:
                                Score = Score + 23 + 12
                        if fav > 120 and fav <= 130:
                                Score = Score + 23 + 13
                        if fav > 130 and fav <= 140:
                                Score = Score + 23 + 14
                        if fav > 140 and fav <= 150:
                                Score = Score + 23 + 15
                        if fav > 150 and fav <= 160:
                                Score = Score + 23 + 16
                        if fav > 160 and fav <= 170:
                                Score = Score + 23 + 17
                        if fav > 170 and fav <= 180:
                                Score = Score + 23 + 18
                        if fav > 180 and fav <= 190:
                                Score = Score + 23 + 19
                        if fav > 190 and fav <= 200:
                                Score = Score + 23 + 20
                        if fav > 200 and fav <= 210:
                                Score = Score + 23 + 21
                        if fav > 210 and fav <= 220:
                                Score = Score + 23 + 22
                        if fav > 220 and fav <= 323:
                                Score = Score + 23 + 23
                        if fav >= 624:
                          coop = tweet['user']['screen_name']
                          nogo = 1
                          
                          print("##")
                          print("Too many Fav checking if this tweet is from a known user or friend ",coop)
                          print("##")
                          

                          if coop in Following:
                                  print("##")
                                  print("This tweet is from a known user : ",tweet['user']['screen_name'])
                                  print("##")
                                  Score = Score + 123
                                  nogo = 0
                          if coop in Friends:
                                  print("##")
                                  print("This tweet is from a friend : ",tweet['user']['screen_name'])
                                  print("##")
                                  nogo = 0
                                  Score = Score + 123
                          if nogo == 1:
                               print("Too many Favs to be legit.")
                               Score = Score - 232
                               Banned = 1
           






      if 'followers_count' in tweet['user'] and tweet['user']['followers_count'] > 0:
                        print("##")
                        print("Source followers count : ",tweet['user']['followers_count'])
                        print("##")

                        if tweet['user']['followers_count'] <= 400:
                                 
                                
                                Fig("cybermedium",'Not Enough Followers')
                                print(tweet['user']['followers_count'])
                                
                                
                                coop = tweet['user']['screen_name']
                                nogo = 1
                                
                                print("##")
                                print("Checking if this tweet is from a known user or friend ",coop)
                                print("##")
                                

                                if coop in Following:
                                        print("##")
                                        print("This tweet is from a known user : ",tweet['user']['screen_name'])
                                        print("##")

                                        nogo = 0
                                if coop in Friends:
                                        print("##")
                                        print("This tweet is from a friend : ",tweet['user']['screen_name'])
                                        print("##")
                                        nogo = 0
                                        Score = Score + 123
                                if nogo == 1:
                                        print("Nop...")
                                        Banned = 1
                                


                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
                                Banned = 1
                                Score = Score - 10000

                        if tweet['user']['followers_count'] > 400 and tweet['user']['followers_count'] < 500:
                                Score = Score + 4
                        if tweet['user']['followers_count'] > 500 and tweet['user']['followers_count'] < 600:
                                Score = Score + 5
                        if tweet['user']['followers_count'] > 600 and tweet['user']['followers_count'] < 700:
                                Score = Score + 6
                        if tweet['user']['followers_count'] > 700 and tweet['user']['followers_count'] < 800:
                                Score = Score + 7
                        if tweet['user']['followers_count'] > 800 and tweet['user']['followers_count'] < 900:
                                Score = Score + 8
                        if tweet['user']['followers_count'] > 900 and tweet['user']['followers_count'] < 1000:
                                Score = Score + 9
                        if tweet['user']['followers_count'] > 1000 and tweet['user']['followers_count'] < 1500:
                                Score = Score + 10
                        if tweet['user']['followers_count'] > 1500 and tweet['user']['followers_count'] < 2000:
                                Score = Score + 11
                        if tweet['user']['followers_count'] > 2000 and tweet['user']['followers_count'] < 2500:
                                Score = Score + 12
                        if tweet['user']['followers_count'] > 2500 and tweet['user']['followers_count'] < 3000:
                                Score = Score + 13
                        if tweet['user']['followers_count'] > 3000 and tweet['user']['followers_count'] < 3500:
                                Score = Score + 14
                        if tweet['user']['followers_count'] > 3500 and tweet['user']['followers_count'] < 4000:
                                Score = Score + 15
                        if tweet['user']['followers_count'] > 4000 and tweet['user']['followers_count'] < 4500:
                                Score = Score + 16
                        if tweet['user']['followers_count'] > 4500 and tweet['user']['followers_count'] < 5000:
                                Score = Score + 17
                        if tweet['user']['followers_count'] > 5000 and tweet['user']['followers_count'] < 6000:
                                Score = Score + 18
                        if tweet['user']['followers_count'] > 6000 and tweet['user']['followers_count'] < 7000:
                                Score = Score + 19
                        if tweet['user']['followers_count'] > 7000 and tweet['user']['followers_count'] < 8000:
                                Score = Score + 20
                        if tweet['user']['followers_count'] > 8000 and tweet['user']['followers_count'] < 9000:
                                Score = Score + 21
                        if tweet['user']['followers_count'] > 9000 and tweet['user']['followers_count'] < 10000:
                                Score = Score + 22
                        if tweet['user']['followers_count'] > 10000:
                                Score = Score + 23

      if 'user_mentions' in tweet['entities'] and len(tweet['entities']['user_mentions']) > 0:
                        print("##")
                        print("This tweet is mentioning someone : ",tweet['entities']['user_mentions'][-1]['screen_name'])
                        print("##")

                        Score = Score + 1

                        if tweet['entities']['user_mentions'][-1]['screen_name'] == "th3j35t3r":
                               Bouffon = 1

       

      if 'verified' in tweet['entities'] and len(tweet['entities']['verified']) == "True":
                        print("##")
                        print("This tweet has been sent by a verified user : ",tweet['entities']['verified'])
                        print("##")
                        Score = Score + 5


      if 'screen_name' in tweet['user'] :
          coop = tweet['user']['screen_name']
          
          print("##")
          print("This tweet is from ",coop)
          print("##")
          

          if coop in Following:
                          print("##")
                          print("This tweet is from a known user : ",tweet['user']['screen_name'])
                          print("##")
                          Score = Score + 10

          if coop in Friends:
               print("##")
               print("This tweet is from a friend : ",tweet['user']['screen_name'])
               print("##")

               Score = Score + 5

          if coop == "th3j35t3r" or Bouffon == 1:


            
                  Score = Score + 9000
                  randodge = ['Cool ','Gorgeous ','Soft ','Enjoy ','Totally ','Awesome ','Fun ','Easy ','Free ','Wow ','Much ','Many ','Too ','So ','Such ','Very ','Amaze ']
                  dodgecoin = str(choice(randodge)) + str(choice(banlist)) + " "
                  time.sleep(2)
                  print("================================================================================")
                  
                  Fig("basic",'SUCH SCORE !!')
                  
                  figy = "Score = %i" % Score
                  Fig("puffy",str(figy))
                  
                  Fig("basic",'MUCH TWEET !!')
                  
                  Fig("puffy","Text:")
                  Fig("digital",tweet['text'])
                  time.sleep(2)
                  
                  Fig("basic",'MANY RETWEET !!')
                  
                  figy = "Retweets = %i" % tweet['retweet_count']
                  Fig("puffy",str(figy))
                  time.sleep(2)
                  
                  Fig("basic",'SO FAVORITE !!')
                  
                  figy = "Favourites = %i" % tweet['favorite_count']
                  Fig("puffy",str(figy))
                  time.sleep(2)
                  
                  Fig("basic",'VERY TREND !!')
                  
                  figy = "Followers = %i" % tweet['user']['followers_count']
                  Fig("puffy",str(figy))
                  time.sleep(2)
                  
                  Fig("basic",'AMAZE TWEET!!')
                  
                  print("================================================================================")
                  figy = "Amaze Now !"
                  Fig("puffy",str(figy))
                  link = "https://twitter.com/"+ str(choice(randodge).replace(" ","")) + "/status/" + str(tweet['id'])

                  twit = tweet['text'].replace("@th3j35t3r","th3b0uf0n").replace("th3j35t3r","th3b0uf0n")
                  dodgelink = str(dodgecoin) + " " + str(link)
                  time.sleep(1)
                  limits()

                  Banned = 0
                  for forbid in bandouble:
                    if Banned == 0:
                      if forbid in tweet['text']:

                              
                              Fig("cybermedium",'This tweet is Identical to a Previous tweet :')
                              
                              print(tweet['text'])
                              
                              Saveid(tweet['id'])
                              
                              Fig("cybermedium",'Going To Trash')
                              print("*=*=*=*=*=*=*=*=*=*")
                              
                              Banned = 1
                              totalalrdysnd = totalalrdysnd + 1
                              time.sleep(1)


                  for item in bandouble:

                    if Banned == 0 and len(item) > 10:
                         pos = 0
                         lng = len(item)
                         half = lng / 2
                         next = int(half) + pos
                         sample = item[pos:int(half)]
                         maxpos = pos + int(len(sample))

                         while int(maxpos) < int(lng):
                              try:
                                   if str(sample) in str(tweet['text']) and str(sample) != " ":
                                        
                                        Fig("cybermedium",'Some parts are Identicals to a Previous Tweet :')
                                        print("Tweet :",tweet['text'])
                                        
                                        print("Found Matched :",sample)
                                        Saveid(id)
                                        
                                        Fig("cybermedium",'Going To Trash')
                                        print("*=*=*=*=*=*=*=*=*=*")
                                        time.sleep(1)

                                        
                                        maxpos = int(lng)
                                        Banned = 1
                                        totalalrdysnd = totalalrdysnd + 1
                                   else:
                                        pos = pos + 1
                                        next = int(half) + pos
                                        sample = item[pos:int(next)]
                                        maxpos = pos + int(len(sample))
                              except:
                                      pos = pos + 1
                                      next = int(half) + pos
                                      sample = item[pos:int(next)]
                                      maxpos = pos + int(len(sample))
                  Idlist(tweet['id'])

                  if Banned == 0:
                       SaveDouble(str(twit))
                       try:
                         print(twit)
                          
                         if len(dodgelink) > 140:
                               dodgelink = dodgelink[:140]
                         if len(twit) > 140:
                              twit = twit[:137] + "..."
                         
                         IrSend(twit)

                         time.sleep(1)
                         

                         IrSend(dodgelink)

                         Fig("cybermedium","DONE")
                         apicall = apicall + 2
                         updatecall = updatecall + 2
                         Saveid(tweet['id'])
                         if fuck > 0:
                                                          fuck = fuck - 1


                       except Exception as e:
                         Fig("bell",'Twython Error')

                         print(e)


                       Banned = 1
                  else:
                    print("================================================================================")
                    Fig("cybermedium",' WOW Already Sent !!')
                    print("================================================================================")
                    time.sleep(1)
  TwtTime = tweet['created_at']
  TwtTime = TwtTime.replace(" +0000 "," ")
  Timed = datetime.datetime.strptime(TwtTime,'%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
  TimeFinal = datetime.datetime.strptime(Timed,'%Y-%m-%d %H:%M:%S')
  hourtweet = now - TimeFinal
  
  print("This tweet was send at : ",TwtTime)
  
  ##time.sleep(0.2)
  
  luck = randint(0,10)
  try:
    if Banned != 1:
      if currentdate.day != 0o1:
               if TimeFinal.month != currentdate.month:
                                        
                                        Fig("basic",'WAY TOO OLD !')
                                        
                                        if luck != 1:
                                          Banned = 1
                                          total2old = total2old + 1
                                        if luck == 1:
                                          Fig("basic",'But who cares !')
                                          

               else:
                        pass
  except Exception as e:
                print(e)
                ##time.sleep(0.2)

  

  try:
       if Banned != 1:
          if TimeFinal.year != currentdate.year:
                                        
                                        Fig("basic",'FUCKING TOO OLD !')
                                        
                                        if luck != 1:
                                                Banned = 1
                                                total2old = total2old + 1
                                        if luck == 1:
                                          Fig("basic",'But who cares !')
                                          

          else:
                pass
  except Exception as e:
    print(e)
    ##time.sleep(0.2)
  try:
    if Banned != 1:
     if hourtweet.days == 1:
      print("Score - 13")
      print("More than a day Not so fresh ...")
      Score = Score - 13
     if hourtweet.days > 2:
                                        
                                        Fig("basic",'TOO OLD !')
                                        
                                        if luck != 1:
                                                Banned = 1
                                                total2old = total2old + 1
                                        if luck == 1:
                                          Fig("basic",'But who cares !')
                                          

  except:
    pass

  if Banned != 1:
    if 'retweeted_status' in tweet :
     if 'created_at' in tweet['retweeted_status'] and len(tweet['retweeted_status']['created_at']) > 0:
          RtTime = tweet['retweeted_status']['created_at']
          RtTime = RtTime.replace(" +0000 "," ")
          RtTimed = datetime.datetime.strptime(RtTime,'%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
          RtTimeFinal = datetime.datetime.strptime(RtTimed,'%Y-%m-%d %H:%M:%S')
          Rthourtweet = now - RtTimeFinal
          print("Retweet created at :" ,RtTimeFinal)
          try:
  
              if currentdate.day != 0o1:
                  if RtTimeFinal.month != currentdate.month:
                                          
                                          Fig("basic",'RT WAY TOO OLD !')
                                          
                                          if luck != 1:
                                                  Banned = 1
                                                  total2old = total2old + 1
                                          if luck == 1:
                                            Fig("basic",'But who cares !')
                                            

                  else:
                         pass
          except Exception as e:
                  print(e)
                  ##time.sleep(0.2)
  
          
  
          try:
                  if RtTimeFinal.year != currentdate.year:
                                          
                                          Fig("basic",'RT FUCKING TOO OLD !')
                                          
                                          Banned = 1
                                          total2old = total2old + 1
                                          ##time.sleep(0.2)
                  else:
                          pass
          except Exception as e:
                  print(e)
                  ##time.sleep(0.2)
  
  if Banned != 1:
    if hourtweet.seconds < 3600:
      Score = Score + 23
      print("Less than an hour ago .")
      print("Score = + 23")
      
      print("Score = ",Score)
      

    if hourtweet.seconds > 3600 and hourtweet.seconds <= 7200:
      Score = Score + 2 + 2
      print("An hour ago .")
      print("Score = + 22")

    if hourtweet.seconds > 7200 and hourtweet.seconds <= 10800:
                  Score = Score + 21
                  print("Two hours ago .")
                  print("Score = + 21")

    if hourtweet.seconds > 10800 and hourtweet.seconds <= 14400:
                  Score = Score + 20
                  print("Three hours ago .")
                  print("Score = + 20")

    if hourtweet.seconds > 14400 and hourtweet.seconds <= 18000:
                  Score = Score + 19
                  print("Four hours ago .")
                  print("Score = + 19")

    if hourtweet.seconds > 18000 and hourtweet.seconds <= 21600:
                  Score = Score + 18
                  print("Five hours ago .")
                  print("Score = + 18")

    if hourtweet.seconds > 21600 and hourtweet.seconds <= 25200:
                  Score = Score + 17
                  print("Six hours ago .")
                  print("Score = + 17")

    if hourtweet.seconds > 25200 and hourtweet.seconds <= 28800:
      Score = Score + 16
      print("Seven hours ago .")
      print("Score = + 16")

    if hourtweet.seconds > 28800 and hourtweet.seconds <= 32400:
                  Score = Score + 15
                  print("Eight hours ago .")
                  print("Score = + 15")

    if hourtweet.seconds > 32400 and hourtweet.seconds <= 36000:
                  Score = Score + 14
                  print("Nine hours ago .")
                  print("Score = + 14")
    if hourtweet.seconds > 36000 and hourtweet.seconds <= 39600:
                  print("Ten hours ago .")
                  print("Score = + 13")
                  Score = Score + 13
    if hourtweet.seconds > 39600 and hourtweet.seconds <= 43200:
                  Score = Score + 12
                  print("Eleven hours ago .")
                  print("Score = + 12")
                  
                  print("Score = ",Score)
                  


    if hourtweet.seconds > 43200 and hourtweet.seconds <= 46800:
                  print("Twelve hours ago .")
                  Score = Score + 11
                  print("Score = + 11")
                  
                  print("Score = ",Score)
                  


    if hourtweet.seconds > 46800 and hourtweet.seconds <= 50400:
                  Score = Score + 10
                  print("Thirteen hours ago .")
                  print("Score = + 10")
                  
                  print("Score = ",Score)
                  

    if hourtweet.seconds > 50400 and hourtweet.seconds <= 54000:
                  Score = Score + 9
                  print("Fourteen hours ago .")
                  print("Score = + 9")


    if hourtweet.seconds > 54000 and hourtweet.seconds <= 57600:
                  Score = Score + 8
                  print("Fiveteen hours ago .")
                  print("Score = + 8")
                  
                  print("Score = ",Score)
                  



    if hourtweet.seconds > 57600 and hourtweet.seconds <= 61200:
                  Score = Score + 7
                  print("Sixteen hours ago .")
                  print("Score = + 7")
                  
                  print("Score = ",Score)
                  


    if hourtweet.seconds > 61200 and hourtweet.seconds <= 64800:
                  Score = Score + 6
                  print("Seventeen hours ago .")
                  print("Score = + 6")
                  
                  print("Score = ",Score)
                  
    if hourtweet.seconds > 64800 and hourtweet.seconds <= 68400:
                        Score = Score + 5
                        print("Eighteen hours ago .")
                        print("Score = + 5")
                        
                        print("Score = ",Score)
                        



    if hourtweet.seconds > 68400 and hourtweet.seconds <= 72000:
                  Score = Score + 4
                  print("Nineteen hours ago .")
                  print("Score = + 4")
                  
                  print("Score = ",Score)
                  


    if hourtweet.seconds > 72000 and hourtweet.seconds <= 75600:
                  Score = Score + 3
                  print("twenty hours ago .")
                  print("Score = + 3")
                  
                  print("Score = ",Score)
                  


    if hourtweet.seconds > 75600 and hourtweet.seconds <= 79200:
                  Score = Score + 2
                  print("Twenty one hours ago .")
                  print("Score = + 2")
                  
                  print("Score = ",Score)
                  

    if hourtweet.seconds > 79200 and hourtweet.seconds <= 82800:
                  Score = Score + 1
                  print("Twenty two hours ago .")
                  print("Score = + 1")
                  
                  print("Score = ",Score)
                  

    if hourtweet.seconds > 82800 and hourtweet.seconds < 86400:
                  print("Twenty three hours ago .")
                  Score = Score + 0
                  print("Score = + 0")
                  
                  print("Score = ",Score)
                  

  #time.sleep(0.3)



  moyscore.append(Score)

  if tweet['lang'] == "en" or tweet['lang'] == "fr" or tweet['lang'] == "en-gb":

    Idlist(tweet['id'])

    if alreadysend == 0:

      Ban(tweet['text'],tweet['user']['screen_name'],tweet['id'],tweet['user']['description'])

      if Banned != 1:
          if Score >= 16:

               print("######################################")
               print('Adding to Retweet List')
               print("Nbr of tweets in queue :",len(retweetlist))
               print("Tweet Score : ",Score)
               print("Tweet ID :", tweet['id'])
               print("Current ApiCall Count :",apicall)
               print("Total Number Of Calls :",totalcall)
               print("Current Update Status Count :",updatecall)
               print("Total Number Of Update Calls :",totalupdatecall)
               print("Search Call left :",search)
               print("Tweet :", tweet['text'])
               print("######################################")
               print("")
               
               time.sleep(1)
               twtbyuser.append(tweet['user']['screen_name'])
               tobsnd.append(tweet['text'])
               retweetlist.append(tweet['text'])
               bandouble.append(tweet['text'].replace("\n"," "))
               clickme = "https://twitter.com/"+str(tweet['user']['screen_name'])+"/status/"+str(tweet['id'])
               IrSend("From:%s %s -> %s Hype:%s"%(tweet['user']['screen_name'],tweet["text"].replace("\n"," "),clickme,Score))
               time.sleep(1)
               SaveDouble(tweet['text'])

          else:
                                        print("")
                                        Fig("epic","But ..")
                                        print("================================================================================")
                                        figy = "Score = %i" % Score
                                        Fig("puffy",str(figy))
                                        print("================================================================================")
                                        print("Score = ",Score)
                                        print("================================================================================")
                                        print(tweet['text'])
                                        print("================================================================================")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("This tweet does not match the requirement to be retweeted. (Score)")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("================================================================================")
                                        print("")
                                        totalscore = totalscore + 1
                ##time.sleep(0.2)
      else:
                                  print("")
                                  Fig("epic","But ..")
                                  print("================================================================================")
                                  Fig("cybermedium","Banned")
                                  print("================================================================================")
                                  print(tweet['text'])

                                  print("================================================================================")
                                  print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                  print("This tweet does not match the requirement to be retweeted.")
                                  print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                  print("================================================================================")
                                  print("")
                ##time.sleep(0.2)
    else:
                                        print("")
                                        Fig("epic","But ..")
                                        print("================================================================================")
                                        Fig("cybermedium","Already sent !")
                                        print("================================================================================")
                                        print(tweet['text'])

                                        print("===================================")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("This tweet has been already sent ..")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("===================================")
                                        print("")
                                        alreadysend = 0
                                        totalalrdysnd = totalalrdysnd + 1
                                        ##time.sleep(0.2)



  else:
                                
                                Fig("epic","but ..")
                                print("================================================================================")
                                Fig("cybermedium","Language")
                                print("===============================================================================")
                                print("Language : ",tweet['lang'])
                                print(tweet['text'])
                                print("================================================================================")
                                print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                print("This tweet does not match the requirement needed to be retweeted.")
                                print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                print("================================================================================")
                                print("")
           ##time.sleep(0.2)
                                totallanguage = totallanguage +1
        #time.sleep(0.3)


  
  






def searchTst(word):
  global apicall
  global updatecall
  global twitter
  global restabit
  global searchdone
  global searchlimit
  global searchapi

  Fig("rev",'SearchTst()')
  #time.sleep(0.3)
  ratechk = 0
  print("Searchdone : " ,searchdone)
  if searchdone == 0:

    try :
            twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
            rate = twitter.get_application_rate_limit_status()
            search = rate['resources']['search']['/search/tweets']['remaining']
            searchapi = int(search)

            apicall = apicall + 2
            ratechk = 1
  
    except Exception as e:
  
      print("mysterious error")
      
      print(e)
      twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
      apicall = apicall + 1
      restabit = 1
      limits()
      if ratechk != 1:
                  searchapi = 23
                  ratechk = 1

    if searchapi > 2:
           
           
           
           
           
           
           

           
           print("##########################################")
           print("**")
           Fig("doom",'Starting search function')
           print("**")
           print("##########################################")

           
           print("=/\/\/\/\/\/\/\/\/\/\/\=")
           Fig("basic",'Calling Limit function')
           print("=/\/\/\/\/\/\/\/\/\/\/\=")
       
           limits()
           try:
               searchresults = twitter.search(q=word, count = 200)
               print("##########################################")
               Fig("colossal",'Results Found !')
               print("")
               apicall = apicall + 1
               searchapi = searchapi - 1
                #time.sleep(0.3)
         
           except :
                         apicall = apicall + 1
                         
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         print("Error Sorry im trying next one")
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         
         
           try:
               
               print("==")
               print("Loading tweets for " + word)
               print("")
                #time.sleep(0.3)
               print("==")
               print("")
                #time.sleep(0.3)
               print("")
       
           except:
                         apicall = apicall + 1
                         
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         print("Error Sorry trying next one")
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         
                          #time.sleep(0.3)
           
           
           
           print("##########################################")
           print("**")
           Fig("doom",'Search function Terminated')
           print("**")
           print("##########################################")
         
           
           
           
           
           
           
           
           try:
               if len(searchresults["statuses"]) > 3 :
       
                    for item in searchresults["statuses"]:
         
                         Scoring(item,search)
               else:
                    print("****************************************")
                    
                    Fig("caligraphy",'No Result')
                    
                    

                    print("????????????????????????????")
                    print("Sorry not enough results for : ",word)
                    print("Maybe you should consider changing it ")
                    print("????????????????????????????")
                    
                    
                    
                    print("****************************************")
                    Fig("basic",'Saving unwanted search to no.result')
                     #time.sleep(1)
                    checkfile(noresult)

                    file = open(noresult,"a")
                    file.write(str(word) + "\n")
                    file.close()
           except Exception as e:
                print(e)


    else:
      
      searchlimit = 1
      searchdone = 0
      limits()



#Some Code
def RedQueen():

    global Keywords
    while 1:
          if GOGOGO == True:
               break

    Fig("basic","GOGOGO!",True)
    time.sleep(1)
    
    Request()
    time.sleep(2)
    loadvars()
    time.sleep(2)
    CheckDouble()
    time.sleep(2)
    
    Fig("basic",'Loading Emoticon',True)
    
    time.sleep(2)
    for use_aliases, group in ((False, emoji.unicode_codes.EMOJI_UNICODE),(True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE)):
                         for name, ucode in list(group.items()):
                                  assert name.startswith(':') and name.endswith(':') and len(name) >= 3
                                  emj = emoji.emojize(name, use_aliases=use_aliases)
                                  emolist.append(emj)
    print(emolist)
    
    Fig("cybermedium",'Done')
    time.sleep(2)
    Fig("basic",'Calling Flush function',True)
    
    flushtmp()
    
    Fig("basic",'Calling Search function',True)
    
    time.sleep(2)

    Minwords = len(Keywords)/20
    Maxwords = len(Keywords)/10
    Minwords = int(Minwords)
    Maxwords = int(Maxwords)
    rndwords = randint(Minwords,Maxwords)
    if rndwords < 100:
      rndwords = len(Keywords)
    
    print("**")
    Fig("calgphy2","Today's Menu :")
    
    print(Keywords[:rndwords])
    
    print("Total search terms : ",rndwords)
    
    print("**")
    
    try:
                            status="Redqueen started at "+ str(currentdate) + " Searching " + str(rndwords) + " items ."
                            IrSend(status)
                            print("")
                            Fig("basic",'Status sent !"')

    except Exception as e:
                            print(e)
                            print("fuck")
                            time.sleep(5)

    time.sleep(5)

    Fig("cybermedium","Check Last Menu started",True)

    checkmenu(Keywords)

    if checkM == 1:
      Keywords = newkeywords
      
      
      print("**")
      
      print("==")
      Fig("basic","New Menu for today !",True)
      print("==")
      
      
      print(Keywords[:rndwords])
      
      print("Total search terms : ",rndwords)
      
      
      print("**")
      
      time.sleep(5)
    tmpcnt= 0
    for key in Keywords[:rndwords]:
      tmpcnt = tmpcnt + 1
      figy = "Searching : %s %i/%i" % (key,tmpcnt,rndwords)
      Fig("puffy",figy)
      time.sleep(1)
      searchTst(key)
      

    Fig("basic","All Done !",True)
    
    
    time.sleep(1)
    
    Fig("basic","Calling Save Search Terms Function",True)

    #time.sleep(0.3)
    lastmeal(Keywords[:rndwords])
    
    if (len(moyscore)) != 0:
      avgscore = sum(moyscore) / float(len(moyscore))
    else:
      avgscore = 0
    try:
      dbrief= "*Redqueen Debrief* -Searchs: "+ str(rndwords) +"-Twts:" + str(len(moyscore)) + "-Avg Score:" + str(avgscore) + "-Rtwts:" + str(rtsave)+ "-Tcall:" + str(totalcall) + "-Ucall:" + str(totalupdatecall)

      IrSend(dbrief)

      Fig("basic",'Status sent !')

    except Exception as e:
                            print(e)
                            print("fuck")
                            time.sleep(5)

    
    Fig("basic","Calling Saving call function",True)
    
    

    SaveTotalCall(apicall,updatecall)

    print("##############################################################################################################")
    print("##############################################################################################################")
    Fig("basic","The End")
    print("##############################################################################################################")
    print("##############################################################################################################")

    sys.exit(1)



if __name__ == '__main__':

     try:
          Screen.wrapper(title)
     except Exception as e:
       print("Title Error line 3257 :",e)
       sys.exit(1)
       pass


     
     Fig("cybermedium","Launching Blueking on IRC")
     time.sleep(1)

     Fig("rev","IrSweet()")
     Fig("cybermedium","Waiting for idle mode")
     time.sleep(1)
     Thread(target = IrSweet).start()
     Thread(target = RedQueen).start()







#################################################TheEnd#############################################################


