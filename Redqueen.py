#!/usr/bin/python3
# -*- coding: utf-8 -*-

from asciimatics.effects import Print 
from asciimatics.renderers import FigletText, Rainbow 
from asciimatics.particles import ShootScreen 
from asciimatics.scene import Scene 
from asciimatics.screen import Screen 
from random import randint, choice, shuffle 
from twython import Twython 
from pyfiglet import Figlet 
from threading import Thread 
import re,socket,time,sys,os,string,datetime,emoji,feedparser
import Config,IrcKey
import TwitterApiKeys as TAK

#Some Vars



GOGOGO_Trigger = False

Shutdown_Trigger = False

MasterPause_Trigger = False

MasterStop_Trigger = False

MasterStart_Trigger = False

RssSent = []

NoResult_List = []

ERRORCNT = 0

Tweet_Age = ""

Skip_Wait_Trigger = False

Id_Done_Trigger = False

Wait_Hour_Trigger = False

Wait_Half_Hour_Trigger = False

AvgScore = []

Emoji_List = []

RetweetSave = ""

CurrentDate = datetime.datetime.now()

Pth_Data = os.path.dirname(os.path.abspath(__file__)) + "/Data/"

Pth_Save= Pth_Data + "Save/"

Pth_TotalApi_Call = str(Pth_Data) + "TotalApi.Call"

Pth_Update_Call = str(Pth_Data) + "UpdateStatus.Call"

Pth_SearchTerms_Used = str(Pth_Data) + "SearchTerms.Used"

Pth_Keywords_Rq = str(Pth_Data) + "Rq.Keywords"

Pth_Following_Rq = str(Pth_Data) + "Rq.Following"

Pth_Friends_Rq = str(Pth_Data) + "Rq.Friends"

Pth_Bannedpeople_Rq= str(Pth_Data) + "Rq.Bannedpeople"

Pth_Bannedword_Rq= str(Pth_Data) + "Rq.Bannedword"

Pth_Rss_Rq = str(Pth_Data) + "Rq.Rss"

Pth_Request_Log = str(Pth_Data) + "Request.log"

Pth_Current_Session = str(Pth_Data) + "Current.Session"

Pth_NoResult = str(Pth_Data) + "No.Result"

Pth_Tweets_Sent = str(Pth_Data) + "Tweets.Sent"

Pth_Text_Sent = str(Pth_Data) + "Text.Sent"

RestABit_Trigger = False

Twitter_Api = ""

Keywords = []

Keywordsave = []

Following = []

Friends = []

Banned_Word_list = []

Banned_User_list = []

Ban_Double_List = []

Rss_Url_List = []

Requested_Cmd_List = []

Api_Call_Nbr = 0

Update_Call_Nbr = 0

Total_Call_Nbr = 0

Total_Update_Call_Nbr = 0

All_Ok_Trigger = False

Total_Sent_Nbr = 0

Menu_Check_Trigger = False
  
Search_ApiCallLeft_Nbr = 0

Search_Limit_Trigger = False

Search_Done_Trigger = False

Retweet_List = []

New_Keywords_List = []

Start_Date = ''

Time_To_Wait = 0

Totale_Score_Nbr = 0

Total_Already_Send_Nbr = 0

Total_Ban_By_Lang_Nbr = 0

Total_Ban_By_Date_Nbr = 0

Total_Ban_By_NoResult_Nbr = 0

Total_Ban_By_Keywords_Nbr = 0

Total_Ban_By_FollowFriday_Nbr = 0

Total_Ban_By_TooManyHashtags_Nbr = 0

Total_Ban_By_BannedPeople_Nbr = 0

Tweets_By_Same_User = []

printable = set(string.printable)

#Some Defs

def WakeApiUp():
   global Twitter_Api
   global Api_Call_Nbr
   global Search_ApiCallLeft_Nbr
   try:
      if TAK.OAUT_1 is True:
         Twitter_Api = Twython(TAK.oa1_app_key, TAK.oa1_app_secret, TAK.oa1_oauth_token, TAK.oa1_oauth_token_secret)
         Api_Call_Nbr += 1
         rate = Twitter_Api.get_application_rate_limit_status()
         Search_ApiCallLeft_Nbr = int(rate['resources']['search']['/search/tweets']['remaining'])
         return(Twitter_Api)
      elif TAK.OAUT_2 is True:
         Twitter_Api = Twython(TAK.oa2_app_key, access_token=TAK.oa2_access_token)
         rate = Twitter_Api.get_application_rate_limit_status()
         Search_ApiCallLeft_Nbr = int(rate['resources']['search']['/search/tweets']['remaining'])
         Api_Call_Nbr += 1
         return(Twitter_Api)
   except Exception as e:
     print("Error Api:",str(e))
     if GOGOGO_Trigger is False:
        sys.exit()

def checkfile(filename):
    try:
                        file = open(filename,"r")
                        file.close()
    except:
                        print("==")
                        print("File does not exist (Pth_Keywords_Rq)")
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

    clean_lines = list(dict.fromkeys(clean_lines))

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
    global Banned_Word_list
    global Banned_User_list
    global Requested_Cmd_List

    Fig("rev",'LoadVars()',True)
    print("\n\n\n\n")


    print("\n\n")
    Fig("cybermedium","Loading No Result",True)
    print("\n\n")
    checkfile(Pth_NoResult)
    lines = cleanfile(Pth_NoResult)

    for saved in lines:
      NoResult_List.append(saved)

    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d",'No Result Loaded',True)
    print("*=*=*=*=*=*=*=*=*=*\n")



    checkfile(Pth_Data+"RssSave")
    lines = cleanfile(Pth_Data+"RssSave")
    for saved in lines:
       RssSent.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Rss Sent Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    print("\n\n")

    Fig("cybermedium",'Loading Keywords',True)

    checkfile(Pth_Keywords_Rq)
    lines = cleanfile(Pth_Keywords_Rq)

    for saved in lines:
           Keywords.append(saved)

    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d",'Keywords Loaded',True)
    print("*=*=*=*=*=*=*=*=*=*\n")
    time.sleep(Config.Time_Sleep)
    Keywordsave = Keywords
    shuffle(Keywords)
    print("\n\n")
    Fig("cybermedium",'Loading Following',True)

    checkfile(Pth_Following_Rq)
    lines = cleanfile(Pth_Following_Rq)

    for saved in lines:
       Following.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Following Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    print("\n\n\n")
    Fig("cybermedium","Loading Friends",True)
    print("\n\n")

    checkfile(Pth_Friends_Rq)
    lines = cleanfile(Pth_Friends_Rq)
    for saved in lines:
       Friends.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Friends Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(Config.Time_Sleep)


    print("\n\n")
    Fig("cybermedium","Loading Banned Words",True)
    print("\n\n")
    checkfile(Pth_Bannedword_Rq)
    lines = cleanfile(Pth_Bannedword_Rq)

    for saved in lines:
      Banned_Word_list.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Banned Words Loaded",True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(Config.Time_Sleep)
    print("\n\n")
    Fig("cybermedium","Loading Banned Users",True)
    print("\n\n")
    checkfile(Pth_Bannedpeople_Rq)
    lines = cleanfile(Pth_Bannedpeople_Rq)
    for saved in lines:
      Banned_User_list.append(saved)
      
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d","Banned users Loaded,True")
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(Config.Time_Sleep)

    print("\n\n")
    Fig("cybermedium","Loading Rss Flux",True)
    print("\n\n")
    checkfile(Pth_Rss_Rq)
    lines = cleanfile(Pth_Rss_Rq)
    for saved in lines:
      Rss_Url_List.append(saved)

    print("\n\n")
    Fig("cybermedium","Loading cmds log",True)
    print("\n\n")
    checkfile(Pth_Request_Log)
    lines = cleanfile(Pth_Request_Log)
    for saved in lines:
      Requested_Cmd_List.append(saved)

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
   global Start_Date
   if mode == 2:
     now = ''
     timesup = ''
     timeleft = ''
     timed = ''

     now = datetime.datetime.now()
     timesup = now - Start_Date
     timeleft = "Time Left %i / %i"% (timesup.seconds,Time_To_Wait)
     timed = timesup.seconds

     return timeleft


   if mode == 1:

        now = ''
        timesup = ''
        timeleft = ''
        timed = ''



        now = datetime.datetime.now()
        timesup = now - Start_Date
        timed = timesup.seconds
        return timed




def Request(cmd):

  global Keywords
  global Banned_Word_list
  global Banned_User_list
  global Api_Call_Nbr
  global Banned
  global MasterPause_Trigger
  global NoResult_List
  global MasterStart_Trigger
  global MasterStop_Trigger

  Fig("rev",'#Request()')
  
  time.sleep(Config.Time_Sleep)

  adk = []
  delk = []
  bk = []
  adu = []
  delu = []
  bu = []
  adf = []
  delf = []
  bf = []
  adrss = []
  delrss = []

  RmNores = False

  print("New request from allowed user:", IrcKey.IRMASTER)
  
  timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print("At %s ."% timestamp)

  log = "\n***\nNew request from allowed user:%s at: %s \n %s\n***"%(IrcKey.IRMASTER,timestamp,cmd)
  output= []

  if cmd.count(",") >0:
     print("You v send those commandes :")
  else:
     print("You v send this commande :")
  print(cmd)

  items = cmd.split(';')
  
  cmds=["adduser:","deluser:","banuser:",
       "addkeyword:","delkeyword:","bankeyword:",
       "addfriend:","delfriend","banfriend:",
       "addrss:","delrss:",
       "!help","!users","!keywords","!friends",
       "!rss","!requests","!Pth_NoResult","!rmPth_NoResult",
       "!badkeys","!badppl","!start","!stop","!pause","!quit"]
  
  for sample in items:
      reconized = False
      for option in cmds:
          if sample.lower().startswith(option):
              reconized = True
              if option == "!help":
                     help = ["adduser:@user1 @user2 [Add user1 and user2 to Rq.Following]",
"deluser:@user1 @user2 [Delete user1 and user2 in Rq.Following]",
"banuser:@user1 @user2 [Add user1 and user2 to Rq.Bannedpeople and remove it from Rq.Keywords]",
"addfriend:@user1 @user2 [Add user1 and user2 to Rq.Friends]",
"delfriend:@user1 @user2 [Delete user1 and user2 in Rq.Friends]",
"banfriend:@user1 @user2 [Add user1 and user2 to Rq.Friends and remove it from Rq.Keywords]",
"addkeyword:Key word1,Key word2 [Add 'Key word1' and 'Key word2' to Rq.Keywords]",
"delkeyword:Key word1,Key word2 [Delete 'Key word1' and 'Key word2' in Rq.Keywords]",
"bankeyword:Key word1,Key word2 [Add Key word1 and Key word2 to Rq.Bannedword and remove it from Rq.Keywords]",
"addrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Add rss feeds to Rq.Rss]",
"delrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Delete rss feeds in Rq.Rss]",
"Commands starting with '!' can't be chained or have to be placed at the end of multiple cmd.",
"!help [Print this help]",
"!start [Launch Crawling.]",
"!stop [Stop Crawling.]",
"!pause [Start and Stop Pause mode]",
"!quit [Exit.]",
"!users [Print Rq.Following content]",
"!keywords [Print Rq.Keywords content]",
"!rss [Print Rq.Rss content]",
"!requests [Print Request.log content]",
"!Pth_NoResult [Print No.Result content]",
"!rmPth_NoResult [Remove No.Result content from Rq.Keywords]",
"!badkeys [Print Rq.Bannedword content]",
"!badppl [Print Rq.Bannedpeople content]",
"Example : deluser:@user1 @user2 ;addkeyword:key1,key two,key3;bankeyword:badkey1,bad key two;!rss"]
                     return(help)
              if option == "!pause":
                       if MasterPause_Trigger is True:
                          MasterPause_Trigger = False
                          return("Pause mode is off.")
                       else:
                          MasterPause_Trigger = True
                          return("Pause mode is on.")
              if option == "!start":
                          MasterStart_Trigger = True
                          if MasterStop_Trigger is True:
                                MasterStop_Trigger = False
                                return(Redqueen())
                          return("Redqueen has started.")
              if option == "!stop":
                          MasterStart_Trigger = False
                          MasterStop_Trigger = True
                          return("Redqueen has stopped.")
              if option == "!quit":
                          MasterStart_Trigger = False
                          Irc.send(bytes("PRIVMSG %s : Redqueen has been terminated. \r\n" % (IrcKey.IRMASTER), "UTF-8"))
                          os.system("pkill -f Redqueen.py")
              if option == "!badkeys":
                       return(Banned_Word_list)
              if option == "!badppl":
                       return(Banned_User_list)
              if option == "!users":
                       return(Following)
              if option == "!keywords":
                       return(Keywords)
              if option == "!friends":
                       return(Friends)
              if option == "!rss":
                       return(Rss_Url_List)
              if option == "!requests":
                       return(Requested_Cmd_List)
              if option == "!Pth_NoResult":
                       return(NoResult_List)
              if option == "!rmPth_NoResult":
                        print("Removing No.results from Rq.Keywords..")
                        RmNores = True
              if option == "banuser:":
                   if sample.count("@") == 1:
                        print("You asked to Ban this user :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            bu.append(single)
                            delk.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              bu.append(var.replace(str(option),"").replace(" ",""))
                              delk.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Ban those users: ",",".join(bu))
                   else:
                       print("No user found '@' is missing")

              if option == "adduser:":

                   if sample.count("@") == 1:
                        print("You asked to Add this user :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            adu.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              adu.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Add those users: ",",".join(adu))
                   else:
                       print("No user found '@' is missing")

              if option == "deluser:":
                   if sample.count("@") == 1:
                        print("You asked to Delete this user :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            delu.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              delu.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Delete those users: ",",".join(delu))
                   else:
                       print("No user found '@' is missing")

              if option == "banfriend:":
                   if sample.count("@") == 1:
                        print("You asked to Ban this friend :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            bf.append(single)
                            delk.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              bf.append(var.replace(str(option),"").replace(" ",""))
                              delk.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Ban those friends: ",",".join(bf))
                   else:
                       print("No user found '@' is missing")

              if option == "delfriend:":
                   if sample.count("@") == 1:
                        print("You asked to Delete this friend :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            delf.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              delf.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Delete those friends: ",",".join(delf))
                   else:
                       print("No user found '@' is missing")
              if option == "addfriend:":

                   if sample.count("@") == 1:
                        print("You asked to Add this friend :",sample)
                        single= sample.replace(str(option),"").replace("@","").replace(" ","")
                        if len(single) >0:
                            adf.append(single)
                        else:
                            print("User var is empty.")
                   elif sample.count("@") >1:
                        for var in sample.split("@"):
                           if len(var) >0:
                              adf.append(var.replace(str(option),"").replace(" ",""))
                           else:
                              print("User var is empty.")
                        print("You asked to Add those friends: ",",".join(adf))
                   else:
                       print("No user found '@' is missing")
              if option == "bankeyword:":
                   if sample.count(",") == 0:
                        print("You asked to Ban this keyword :",sample)
                        single= sample.replace(str(option),"")
                        if len(single) >0:
                            bk.append(single)
                            delk.append(single)
                        else:
                            print("Keyword var is empty.")
                   elif sample.count(",") >0:
                        for var in sample.split(","):
                           if len(var) >0:
                              bk.append(var.replace(str(option),""))
                              delk.append(var.replace(str(option),""))
                           else:
                              print("Keyword var is empty.")
                        print("You asked to Ban those Keywords: ",",".join(bk))
              if option == "addkeyword:":
                   if sample.count(",") == 0:
                        print("You asked to Add this keyword :",sample)
                        single= sample.replace(str(option),"")
                        if len(single) >0:
                            adk.append(single)
                        else:
                            print("Keyword var is empty.")
                   elif sample.count(",") >0:
                        for var in sample.split(","):
                           if len(var) >0:
                              adk.append(var.replace(str(option),""))
                           else:
                              print("Keyword var is empty.")
                        print("You asked to Add those Keywords: ",",".join(adk))
              if option == "delkeyword:":
                   if sample.count(",") == 0:
                        print("You asked to Delete this keyword :",sample)
                        single= sample.replace(str(option),"")
                        if len(single) >0:
                            delk.append(single)
                        else:
                            print("Keyword var is empty.")
                   elif sample.count(",") >0:
                        for var in sample.split(","):
                           if len(var) >0:
                             delk.append(var.replace(str(option),""))
                           else:
                              print("Keyword var is empty.")
                        print("You asked to Add those Keywords: ",",".join(delk))
              if option == "delrss:":
                   if sample.count("http") == 1:
                        print("You asked to Delete this rss feed :",sample)
                        single= sample.replace(str(option),"")
                        if len(single) >0:
                            delk.append(single)
                        else:
                            print("Rss var is empty.")
                   elif sample.count("http") >1:
                        for var in sample.split(","):
                           if len(var) >0:
                             delrss.append(var.replace(str(option),""))
                           else:
                              print("Rss var is empty.")
                        print("You asked to Delete those rss feeds: ",",".join(delrss))

                   else:
                       print("No rss found (flux must starts with http)")
              if option == "addrss:":
                   if sample.count("http") == 1:
                        print("You asked to Add this rss feed :",sample)
                        single= sample.replace(str(option),"")
                        if len(single) >0:
                            adrss.append(single)
                        else:
                            print("Keyword var is empty.")
                   elif sample.count("http") >1:
                        for var in sample.split(","):
                           if len(var) >0:
                             adrss.append(var.replace(str(option),""))
                           else:
                              print("Keyword var is empty.")
                        print("You asked to Delete those rss feeds: ",",".join(adrss))
                   else:
                       print("No rss found (flux must starts with http)")
      if reconized == False:
         checkfile(Pth_Request_Log)

         file = open(Pth_Data+"Request.log","a")
         file.write(log)
         return("Cmd not recognised.")

  checkfile(Pth_Request_Log)
          
  file = open(Pth_Data+"Request.log","a")
  file.write(log)
  file.close

  checkfile(Pth_Friends_Rq)
  checkfile(Pth_Following_Rq)
  checkfile(Pth_Bannedpeople_Rq)
  checkfile(Pth_Bannedword_Rq)
  checkfile(Pth_Keywords_Rq)
  checkfile(Pth_Rss_Rq)

  if RmNores is True:
     ret = Flush_NoResult()
     output.append(ret) 

  if len(adrss) > 0:
     print('Adding new entry to Rq.Rss')
     with open(Pth_Rss_Rq,"a") as f:
        for entry in adrss:
           f.write("\n"+str(entry))
     output.append("**Added %s new entry to Rq.Rss**"%len(adrss))



  if len(delrss) > 0:
     print('Deleting entry from Rq.Rss')
     with open(Pth_Rss_Rq, "r") as f:
         lines = f.readlines()
     ts = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
     save_copy = "cp "+str(Pth_Rss_Rq) +" "+str(Pth_Save)+"Rq.Rss"+str(ts)+".save"
     os.system(save_copy)
     with open(Pth_Rss_Rq, "w") as f:
         for line in lines:
            for entry in delrss:
               if line.strip("\n") != entry:
                    f.write(line)
     output.append("**Deleting %s entry in Rq.Rss**"%len(delrss))


  if len(delf) > 0:
     print('Deleting entry from Rq.Friends')
     with open(Pth_Friends_Rq, "r") as f:
         lines = f.readlines()
     ts = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
     save_copy = "cp "+str(Pth_Friends_Rq) +" "+str(Pth_Save)+"Rq.Friends"+str(ts)+".save"
     os.system(save_copy)
     with open(Pth_Friends_Rq, "w") as f:
         for line in lines:
            for entry in delf:
               if line.strip("\n") != entry:
                    f.write(line)
     output.append("**Deleting %s entry in Rq.Friends**"%len(delf))

  if len(delu) > 0:
     print('Deleting entry from Rq.Following')
     with open(Pth_Following_Rq, "r") as f:
         lines = f.readlines()
     ts = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
     save_copy = "cp "+str(Pth_Following_Rq) +" "+str(Pth_Save)+"Rq.Following"+str(ts)+".save"
     os.system(save_copy)
     with open(Pth_Following_Rq, "w") as f:
         for line in lines:
            for entry in delu:
               if line.strip("\n") != entry:
                    f.write(line)
     output.append("**Deleting %s entry in Rq.Following**"%len(delu))

  if len(delk) > 0:
     print('Deleting entry from Rq.Keywords')
     with open(Pth_Keywords_Rq, "r") as f:
         lines = f.readlines()
     ts = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
     save_copy = "cp "+str(Pth_Keywords_Rq) +" "+str(Pth_Save)+"Rq.Keywords"+str(ts)+".save"
     os.system(save_copy)
     with open(Pth_Keywords_Rq, "w") as f:
         for line in lines:
            for entry in delk:
               if line.strip("\n") != entry:
                    f.write(line)
     output.append("**Deleting %s entry in Rq.Keywords**"%len(delk))

  if len(adk) > 0:
     print('Adding new entry to Rq.Keywords')
     with open(Pth_Keywords_Rq,"a") as f:
        for entry in adk:
           f.write("\n"+str(entry))

     output.append("**Adding %s entry in Rq.Keywords**"%len(adk))

  if len(adu) > 0:
     print('Adding new entry to Rq.Following')
     with open(Pth_Following_Rq,"a") as f:
        for entry in adu:
           f.write("\n"+str(entry))
     output.append("**Adding %s entry in Rq.Following**"%len(adu))

  if len(adf) > 0:
     print('Adding new entry to Rq.Friends')
     with open(Pth_Friends_Rq,"a") as f:
        for entry in adf:
           f.write("\n"+str(entry))
     output.append("**Adding %s entry in Rq.Friends**"%len(adf))

  if len(bu) > 0:
     print('Adding new entry to Rq.Bannedpeople')
     with open(Pth_Bannedpeople_Rq,"a") as f:
        for entry in bu:
           f.write("\n"+str(entry))
     output.append("**Adding %s entry in Rq.Bannedpeople**"%len(bu))

  if len(bf) > 0:
     print('Adding new entry to Rq.Bannedpeople')
     with open(Pth_Bannedpeople_Rq,"a") as f:
        for entry in bf:
           f.write("\n"+str(entry))
     output.append("**Adding %s entry in Rq.Bannedpeople**"%len(bf))

  if len(bk) > 0:
     print('Adding new entry to Rq.Bannedword')
     with open(Pth_Bannedword_Rq,"a") as f:
        for entry in bk:
           f.write("\n"+str(entry))
     output.append("**Adding %s entry in Rq.Bannedword**"%len(bk))
  output.append("**Done**")
  return(output)


def Flush_NoResult():
     global NoResult_List
     Fig("rev",'SaveDouble()')
     print('Deleting No.Results content from Rq.Keywords')
     cnt = 0
     with open(Pth_Keywords_Rq, "r") as f:
         lines = f.readlines()
     ts = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
     save_copy = "cp "+str(Pth_Keywords_Rq) +" "+str(Pth_Save)+"Rq.Keywords"+str(ts)+".Before_Removing_Noresults.save"
     os.system(save_copy)
     with open(Pth_Keywords_Rq, "w") as f:
         for line in lines:
            for entry in NoResult_List:
               if line.strip("\n") != entry:
                    f.write(line)
               else:
                   print("Removed:",entry)
                   cnt += 1
     file = open(Pth_NoResult,"w")
     file.write("\n")
     file.close
     NoResult_List = []
     print("**Removed No results from Rq.Keywords: %s/%s **"%(cnt,len(NoResult_List)))
     return("**Removed No results from Rq.Keywords: %s/%s **"%(cnt,len(NoResult_List)))

def SaveDouble(text):
                
                

                Fig("rev",'SaveDouble()')
                
                time.sleep(Config.Time_Sleep)

                text = text.replace("\n","")
                if text not in Ban_Double_List:
                   checkfile(Pth_Text_Sent)

                   file = open(Pth_Text_Sent,"a")
                   file.write("\n"+str(text))
                   file.close()

                
                
                   print("*=*=*=*=*=*=*=*=*=*")
                   print("SAVING TWEET TO TMP :",text)
                   Fig("larry3d",'Saved')
                   print("*=*=*=*=*=*=*=*=*=*")
                else:
                   print("Already saved")
                
                time.sleep(Config.Time_Sleep)



def CheckDouble():


    global Ban_Double_List

    Fig("rev",'CheckDbl()',True)
    

    checkfile(Pth_Text_Sent)

    lines = cleanfile(Pth_Text_Sent)

    for saved in lines:
           if saved not in Ban_Double_List:
                Ban_Double_List.append(saved)
    print("*=*=*=*=*=*=*=*=*=*")
    Fig("larry3d",'BanDouble Updated',True)
    print("*=*=*=*=*=*=*=*=*=*")
    
    time.sleep(Config.Time_Sleep)



def flushtmp():

  global Api_Call_Nbr
  global Update_Call_Nbr

  goflush = 0

  Fig("rev",'flushtmp()',True)

  time.sleep(Config.Time_Sleep)
  if os.path.exists(Pth_Current_Session):

    file = open(Pth_Current_Session,"r")
    datefile = file.read()
    date_object = datetime.datetime.strptime(str(datefile), '%Y-%m-%d %H:%M:%S.%f')
    Laps = (CurrentDate - date_object)

    print(Laps)

    try:
      if (CurrentDate - date_object).total_seconds() > 86400:
           goflush = 1
    except Exception as e:
      print(e)
      
      Fig("cybermedium",'No need to flush',True)
      
      time.sleep(Config.Time_Sleep)

    if goflush == 1:


      
      print("==")
      Fig("basic",'Flushing Temps Files',True)
      print("==")
      
      
      file.close()
      try:
                          text="New Pth_Current_Session ! " + str(CurrentDate)
                          IrSend(text)
                          print("")
                          Fig("basic",'Status sent !')

      except Exception as e:
                          print(e)
                          print("fuck")
                          time.sleep(Config.Time_Sleep)
      time.sleep(Config.Time_Sleep)

      os.remove(Pth_Current_Session)


      if os.path.exists(Pth_TotalApi_Call):
                os.remove(Pth_TotalApi_Call)


      if os.path.exists(Pth_Update_Call):
                os.remove(Pth_Update_Call)


      if os.path.exists(Pth_SearchTerms_Used):
                os.remove(Pth_SearchTerms_Used)

      
      
      print("==")
      Fig("basic",'Saving current date',True)
      print(CurrentDate)
      print("==")
      
      
      time.sleep(Config.Time_Sleep)
      file = open(Pth_Current_Session,"w")
      file.write(str(CurrentDate))
      file.close()



      Fig("cybermedium",'Done Flushing',True)
      time.sleep(Config.Time_Sleep)
      
    else:
      lfts = 86400 - Laps.seconds

      
       
      print("==")
      Fig("basic",'Starting from Last Pth_Current_Session',True)
      
      print("Numbers of seconds since the first api call :",Laps.seconds)
      print("%i Seconds left until Twitter flushs Api_Call_Nbrs :" % lfts)
      print("==")
      
      
      
      time.sleep(Config.Time_Sleep)

  else:
    
    
    print("==")
    Fig("basic",'New Pth_Current_Session Started',True)
    print(CurrentDate)
    print("==")
    
    
    time.sleep(Config.Time_Sleep)
    file = open(Pth_Current_Session,"w")
    file.write(str(CurrentDate))
    file.close()


def checkmenu(wordlist):
  Fig("rev",'CheckMenu()',True)
  
  time.sleep(Config.Time_Sleep)
  try:
                global New_Keywords_List
                global Menu_Check_Trigger
                oldlen = len(wordlist)
                file = open(Pth_NoResult,"r")
                lines2 = file.read().splitlines()
                lenmatch2 = len(set(lines2) & set(wordlist))

                print("==")
                Fig("doom",'Removing Last Searches with No Result',True)
                time.sleep(Config.Time_Sleep)
                while lenmatch2 >0:
                        Fig("digital","Found %i occurences :" % lenmatch2,True)
                        set(lines2) & set(wordlist)
                        time.sleep(Config.Time_Sleep)
                        Fig("digital","Removing No result from list ...",True)
                        wordlist = list(set(wordlist) - set(lines2))
                        time.sleep(Config.Time_Sleep)
                        Fig("digital","New lenght of searchlist : " + str(len(wordlist)) + " (Was " + str(oldlen) + " )",True)
                        print("==")
                        time.sleep(Config.Time_Sleep)
                        lenmatch2 = len(set(lines2) & set(wordlist))
                file.close()

                Fig("doom",'Removing Old Searches',True)
                time.sleep(Config.Time_Sleep)
                New_Keywords_List = wordlist
                print("==")
                Fig("cybermedium",'Removed successfully',True)
                print("==")
                time.sleep(Config.Time_Sleep)

                oldlen = len(wordlist)
                file = open(Pth_SearchTerms_Used,"r")
                lines = file.read().splitlines()
                lenmatch = len(set(lines) & set(wordlist))

                while lenmatch >0:
                    Fig("digital","Found %i occurences :" % lenmatch,True)
                    set(lines) & set(wordlist)
                    time.sleep(Config.Time_Sleep)
                    Fig("digital","Removing from search list ...",True)
                    wordlist = list(set(wordlist) - set(lines))
                    time.sleep(Config.Time_Sleep)
                    Fig("digital"+"New lenght of searchlist : " + str(len(wordlist)) + " (Was " + str(oldlen) + " )",True)
                    print("==")
                    time.sleep(Config.Time_Sleep)
                    lenmatch = len(set(lines) & set(wordlist))
                file.close()
                print("==")
                Fig("cybermedium",'Removed successfully',True)
                print("==")
                Menu_Check_Trigger = True
                time.sleep(Config.Time_Sleep)
                New_Keywords_List = wordlist
  except Exception as e:
    print(e)

    print("==")
    Fig("basic",'No previous searchs found for today',True)
    print("==")
    time.sleep(Config.Time_Sleep)


def lastmeal(lastsearch):

    global Menu_Check_Trigger

    if Menu_Check_Trigger == False:
                  Fig("rev",'LastSearch()',True)
                  time.sleep(Config.Time_Sleep)
                  checkfile(Pth_SearchTerms_Used)
  
                  file = open(Pth_SearchTerms_Used,"a")
                  for words in lastsearch:
                    file.write(words + "\n")
                    Fig("digital","Marking " + words + " as old . ")
                  file.close()
                  Menu_Check_Trigger = True
                  time.sleep(Config.Time_Sleep)
    else:
                  print("==")
                  Fig("cybermedium",'Saved already')
                  print("==")

def SaveTotalCall(call,update):
    Fig("rev",'SaveTotalCall()')
    time.sleep(Config.Time_Sleep)
    global Total_Call_Nbr
    global Update_Call_Nbr
    global Total_Update_Call_Nbr
    checkfile(Pth_TotalApi_Call)
    file = open(Pth_TotalApi_Call,"a+")
    lines = file.read().splitlines()
    lenfile = len(lines)
    try:
         lastitem = lines[lenfile -1]
    except:
          lastitem = 0
    print("==")
    print("Last Total saved : ",lastitem)
    newitem = int(lastitem) + int(call)
    Total_Call_Nbr = newitem
    finalitem = str(newitem) + "\n"
    Fig("digital","Saving new Total : " + str(finalitem))
    print("==")
    file.write(finalitem)
    file.close()
    time.sleep(Config.Time_Sleep)
    checkfile(Pth_Update_Call)

    file2 = open(Pth_Update_Call,"a+")
    lines2 = file2.read().splitlines()
    lenfile2 = len(lines2)
    try:
         lastitem2 = lines2[lenfile2 -1]
    except:
          lastitem2 = 0
    print("==")
    print("Last Update Total saved : ",lastitem2)
    newitem2 = int(lastitem2) + int(update)
    Total_Update_Call_Nbr = newitem2
    finalitem2 = str(newitem2) + "\n"
    print("Saving new Update Total : ",finalitem2)
    print("==")
    file2.write(finalitem2)
    file2.close()
    Fig("basic",'Done Saving Calls')

    time.sleep(Config.Time_Sleep)


def IrSweet():
     global GOGOGO_Trigger
     global Irc

     Konnected = False
     Identified = False
     Joined = False
     IrcSocket = False
     Irc = ""
     Buffer = ""


     while IrcSocket == False:
       try:
          Fig("digital","\n--Connecting to :"+str(IrcKey.IRHOST) +"--\n")
          time.sleep(Config.Time_Sleep)
          Irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          Irc.connect((IrcKey.IRHOST, IrcKey.IRPORT))

          Irc.send(bytes("NICK %s\r\n" % IrcKey.IRNICK, "UTF-8"))
          Irc.send(bytes("USER %s %s woot :%s\r\n" % (IrcKey.IRIDENT, IrcKey.IRHOST, IrcKey.IRREALNAME), "UTF-8"))
          time.sleep(Config.Time_Sleep)
          IrcSocket = True
       except Exception as e:
               print("connect() Error : ",e)
               continue

     last_ping = time.time()
     threshold = 3 * 60

     while IrcSocket == True:
          try:
               Buffer = Irc.recv(1024).decode("UTF-8",errors="ignore")

               if len(Buffer) > 1:
                    print("Buffer: ",Buffer)

               if IrcKey.IRMASTERTrigger in Buffer and "PRIVMSG BlueKing :" in Buffer:
                    cmd = Buffer.split("PRIVMSG BlueKing :")[1]
                    Answer = Request(cmd[:-2])
                    if len(Answer) > 0:
                              if type(Answer) == list:
                                  for l in Answer:
                                      time.sleep(Config.Time_Sleep)
                                      print("\n--Sending :%s --\n"%l)
                                      Irc.send(bytes("PRIVMSG %s : < %s > \r\n" % (IrcKey.IRMASTER,l), "UTF-8"))
                              else:
                                  print("\n--Sending :%s --\n"%Answer)
                                  Irc.send(bytes("PRIVMSG %s : < %s > \r\n" % (IrcKey.IRMASTER,Answer), "UTF-8"))

               if Buffer.find("PING") != -1:
                    Fig("digital","\n--PINGED--\n")
                    try:
                         tmp = Buffer.split("PING :")[1]
                    except Exception as e:
                         tmp = "placeholder"
                         print("Error Ping:",e)
                    Irc.send(bytes("PONG :"+ tmp +"\r\n" ,"UTF-8" ))
                    Fig("digital","\n--PONG :"+ str(tmp) +" --\n")
                    last_ping = time.time()

               if Buffer.find("ERROR :Closing Link:") != -1:
                   Fig("digital"+"\n--TimeOut--\n\n--Restablishing Connection--\n")
                   return IrSweet()

               if Buffer.find(IrcKey.IRKonTrigger) != -1 and Konnected is False:
                    Konnected = True
                    Fig("digital","\n--Connected--\n")

               if Buffer.find(IrcKey.IRIdentTrigger) != -1 and Identified is False:
                    Identified = True
                    Fig("digital","\n--Authentified--\n")

               if Identified == False and Konnected is True:
                    time.sleep(Config.Time_Sleep)
                    Fig("digital","\n--Sending CREDENTIAL--\n")
                    Irc.send(bytes("%sIDENTIFY %s\r\n" % (IrcKey.IRNICKSERV,IrcKey.IRPASS), "UTF-8"))
                    time.sleep(Config.Time_Sleep)

               if Joined == False and Identified == True and Konnected == True:
                    print("\n--Joining "+str(IrcKey.IRCHANNEL)+"--\n")
                    Irc.send(bytes("JOIN %s %s\r\n" % (IrcKey.IRCHANNEL,IrcKey.IRCHANPASS), "UTF-8"));
                    time.sleep(Config.Time_Sleep)
                    Irc.send(bytes("PRIVMSG %s :<Knock Knock Neo ...>\r\n" % IrcKey.IRCHANNEL, "UTF-8"))
                    time.sleep(Config.Time_Sleep)
                    Irc.send(bytes("PRIVMSG %s :<The Matrix Has You.>\r\n" % IrcKey.IRCHANNEL, "UTF-8"))
                    time.sleep(Config.Time_Sleep)
                    Irc.send(bytes("PRIVMSG %s :<Follow The White Rabbit.>\r\n" % IrcKey.IRCHANNEL, "UTF-8"))
                    time.sleep(Config.Time_Sleep)
                    Fig("digital","\n--Joined--\n")
                    Joined = True
               if (time.time() - last_ping) > threshold:
                    Fig("digital","\n--TimeOut--\n\n--Restablishing Connection--\n")
                    return IrSweet()

               if Joined is True and Identified is True and Konnected is True:
                    GOGOGO_Trigger = True

          except Exception as e:
               print("Error IrSocket:",e)


def Feeds(ttl):
     global RssSent

     counter = 0

     for flux in Rss_Url_List:
         if counter <= ttl:
            try:
               rss = feedparser.parse(flux)
     
               for news in rss.entries:
                    time.sleep(Config.Time_Sleep)
                    counter = counter + 1
                    format = str(news.title)+" : "+str(news.link)
                    if format not in RssSent:
                         RssSent.append(format)
                         IrSend(format)
                         with open(Pth_Data+"RssSave","a") as f:
                              f.write("\n")
                              f.write(str(format))
            except Exception as e:
               time.sleep(Config.Time_Sleep)
               counter = counter + 1
               print("Rss Error %s : %s"%(flux,e))
               IrSend("Rss Error "+str(flux)+" : "+str(e))
         else:
               return

def IrSend(content,dontprint = None):
        global Irc
        Fig("rev","IrSend()")

        if not dontprint:
          print("==")
          Fig("epic","Tweet Loaded!")
          print("==")
          Irc.send(bytes("PRIVMSG %s :==============================================================\r\n" % IrcKey.IRCHANNEL, "UTF-8"))

        content = content.replace("\n"," ")
        print(content)
        time.sleep(Config.Time_Sleep)
        print("befor fig and irc.send")
        Fig("digital","\n--Sending :"+str(content)+"--\n")
        Irc.send(bytes("PRIVMSG %s :** %s **\r\n" % (IrcKey.IRCHANNEL,content), "UTF-8"))
        Fig("digital","\n--Done--\n")
        return

def Stat2Irc(Time_To_Wait):
#  Flood = randint(0,3)
#  if Flood == 3:
       Api_Call_Nbrtxt = "Total RT Sent: " + str(Total_Sent_Nbr)
       IrSend(Api_Call_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Update_Call_Nbrtxt = "Current Update Calls: " + str(Update_Call_Nbr)
       IrSend(Update_Call_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Call_Nbrtxt = "Total Calls: " +str(Total_Call_Nbr)
       IrSend(Total_Call_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Update_Call_Nbrtxt = "Total Update Calls: " + str(Total_Update_Call_Nbr)
       IrSend(Total_Update_Call_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Banned_User_listtxt = "Banned Users in list: " + str(len(Banned_User_list))
       IrSend(Banned_User_listtxt)
       time.sleep(Config.Time_Sleep)
       Ban_Double_Listtxt = "Total Banned (Double): "+str(Total_Already_Send_Nbr)
       IrSend(Ban_Double_Listtxt)
       time.sleep(Config.Time_Sleep)
       Banned_Word_listtxt = "Banned Words in list: "+str(len(Banned_Word_list))
       IrSend(Banned_Word_listtxt)
       time.sleep(Config.Time_Sleep)
       Friendstxt = "Nbr of friends: "+str(len(Friends))
       IrSend(Friendstxt)
       time.sleep(Config.Time_Sleep)
       Followingtxt = "Users Followed: "+str(len(Following))
       IrSend(Followingtxt)
       time.sleep(Config.Time_Sleep)
       Keywordstxt = "Keywords in list: "+str(len(Keywords))
       IrSend(Keywordstxt)
       time.sleep(Config.Time_Sleep)
       AvgScoreTxt = "Current Tweets collected: " + str(len(AvgScore))
       IrSend(AvgScoreTxt)
       time.sleep(Config.Time_Sleep)
       NbrRetweettxt = "Tweets sent to irc:"+str(len(Retweet_List))
       IrSend(NbrRetweettxt)
       time.sleep(Config.Time_Sleep)
       Totale_Score_Nbrtxt = "Total Banned (Score): "+str(Totale_Score_Nbr)
       IrSend(Totale_Score_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_Lang_Nbrtxt = "Total Banned (Language): " +str(Total_Ban_By_Lang_Nbr)
       IrSend(Total_Ban_By_Lang_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_Date_Nbrtxt = "Total Banned (Too old): "+str(Total_Ban_By_Date_Nbr)
       IrSend(Total_Ban_By_Date_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_NoResult_Nbrtxt = "Total Banned (No Keywords): "+str(Total_Ban_By_NoResult_Nbr)
       IrSend(Total_Ban_By_NoResult_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_Keywords_Nbrtxt = "Total Banned (Words): "+str(Total_Ban_By_Keywords_Nbr)
       IrSend(Total_Ban_By_Keywords_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_FollowFriday_Nbrtxt = "Total Banned (FF): "+str(Total_Ban_By_FollowFriday_Nbr)
       IrSend(Total_Ban_By_FollowFriday_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_TooManyHashtags_Nbrtxt = "Total Banned (###):"+str(Total_Ban_By_TooManyHashtags_Nbr)
       IrSend(Total_Ban_By_TooManyHashtags_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Total_Ban_By_BannedPeople_Nbrtxt = "Total Banned Users: "+str(Total_Ban_By_BannedPeople_Nbr)
       IrSend(Total_Ban_By_BannedPeople_Nbrtxt)
       time.sleep(Config.Time_Sleep)
       Feeds(Time_To_Wait)

def limits():
  Fig("rev",'Limits()')
  time.sleep(Config.Time_Sleep)
  global Api_Call_Nbr
  global Update_Call_Nbr
  global Total_Update_Call_Nbr
  global Total_Call_Nbr
  global Twitter_Api
  global Search_Limit_Trigger
  global RestABit_Trigger
  global Wait_Hour_Trigger
  global Wait_Half_Hour_Trigger
  global Time_To_Wait
  global Start_Date
  global All_Ok_Trigger
  global Skip_Wait_Trigger
  Start_Date = datetime.datetime.now()

  if Wait_Hour_Trigger == True:


                print("****************************************")
                print("****************************************")
                Fig("epic",'CURRENT LIMITS ARE REACHED !!')
                print("")
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
                Fig("cybermedium",'Resetting current Api_Call_Nbrs')


                Fig("cybermedium",'Login Out')
                Fig("cybermedium",'Waiting 60 minutes')
                print("\n\n\n\n")

                Stat2Irc(3600)
                Update_Call_Nbr = 0
                Api_Call_Nbr = 0
                Search_Limit_Trigger = False
                RestABit_Trigger = False
                Wait_Hour_Trigger = False

                Fig("cybermedium",'Waking up ..')
                time.sleep(Config.Time_Sleep)
                print("")
                Twitter_Api = WakeApiUp()
                print("\n\n")

  if RestABit_Trigger == True:
                print("****************************************")
                print("****************************************")
                Fig("epic",'Mysterious Error !!!',True)
                print("")
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
                Fig("cybermedium",'Resetting current Api_Call_Nbrs')

                Fig("cybermedium",'Login Out')
                Fig("cybermedium",'Waiting 5 minutes')
                Stat2Irc(3600)

                Update_Call_Nbr = 0
                Api_Call_Nbr = 0
                Search_Limit_Trigger = False
                RestABit_Trigger = False


                Fig("cybermedium",'Waking up ..')
                time.sleep(Config.Time_Sleep)
                print("")
                Twitter_Api = WakeApiUp()

  

  if Search_Limit_Trigger == True:

    #Request()
                print("****************************************")
                print("****************************************")
                
                Fig("epic",'SEARCH LIMITS ALMOST REACHED')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
                Fig("cybermedium",'Resetting current Api_Call_Nbrs')


                Fig("cybermedium",'Login Out')
                
                Fig("cybermedium",'Waiting 15 minutes')
                Stat2Irc(900)

                Update_Call_Nbr = 0
                Api_Call_Nbr = 0
                Search_Limit_Trigger = False

                Fig("cybermedium",'Waking up ..')
                print("")
                Twitter_Api = WakeApiUp()
                print("****************************************")
                print("****************************************\n\n\n\n")



  if Api_Call_Nbr >= Config.Maximum_Api_Search_Call_By_15_Minutes:
    
   
    #Request()
    print("****************************************")
    print("****************************************")
    
    Fig("epic",'CURRENT LIMITS ALMOST REACHED')
    Fig("cybermedium",'Saving Total Calls to file')
    SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
    Fig("cybermedium",'Resetting current Api_Call_Nbrs')


    Fig("cybermedium",'Login Out')
    

    if Wait_Half_Hour_Trigger != 1:
      Fig("cybermedium",'Waiting 15 minutes')

      Stat2Irc(900)
    else:
      Fig("cybermedium",'Waiting 30 minutes')
      Stat2Irc(1800)
      
    Update_Call_Nbr = 0
    Api_Call_Nbr = 0
    Fig("cybermedium",'Waking up ..')
    print("")
    Twitter_Api = WakeApiUp() 
    print("****************************************")
    print("****************************************\n\n\n\n")



  if Total_Call_Nbr > Config.Maximum_Api_Search_Call_By_Day:

    #Request()
                print("****************************************")
                print("****************************************")

                

                
                Fig("epic",'CURRENT LIMITS ALMOST REACHED (total)')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
                Fig("cybermedium",'Resetting current Api_Call_Nbrs')
                All_Ok_Trigger = True
                Skip_Wait_Trigger = True
                

  if Total_Update_Call_Nbr > Config.Maximum_Api_Search_Update_Call_By_Day:
    #Request()

                print("****************************************")
                print("****************************************")
                Fig("epic",'CURRENT LIMITS ALMOST REACHED (update)')
                Fig("cybermedium",'Saving Total Calls to file')
                SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)
                Fig("cybermedium",'Resetting current Api_Call_Nbrs')
                All_Ok_Trigger = True

  
  print("===================")
  Fig("cybermedium",'Ok')
  print("===================")
  time.sleep(Config.Time_Sleep)




def Ban(tweet,sender,id,bio):


  global Banned
  global Total_Ban_By_NoResult_Nbr
  global Total_Ban_By_Keywords_Nbr
  global Total_Already_Send_Nbr
  global Total_Ban_By_FollowFriday_Nbr
  global Total_Ban_By_TooManyHashtags_Nbr
  global Total_Ban_By_BannedPeople_Nbr


  ushallpass = 0

  Fig("rev",'Ban()')
  
  print("*=*=*=*=*=*=*=*=*=*")

  if Banned is False:

                for item in Emoji_List:
                        emotst = tweet.count(item)
                        if emotst > 0:
                                print("Found this emoji : ",item)
                                Banned = True
                if Banned is True:
                        Fig("cybermedium",'This tweet contains an Emoticon and must die . ')
                        
                        print(tweet)
                        
                        
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")



  if Banned is False:
     LuckyLuke = randint(0,Config.Luck_Factor)
     print("Luck Score (%s/%s) "%(LuckyLuke,Config.Luck_Factor))
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
     if ushallpass != 1 and LuckyLuke == 1:
                                
                                Fig("cybermedium",'Did not found any Keyword in tweet.')
                                Total_Ban_By_NoResult_Nbr = Total_Ban_By_NoResult_Nbr + 1
                                Banned = True
     print("*=*=*=*=*=*=*=*=*=*")

  for forbid in Banned_Word_list:
    if Banned is False:
      if str(forbid.lower()).replace(":"," ").replace(","," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("'"," ").replace('"',' ').replace("-"," ").replace("_"," ") in str(tweet.lower()).replace(":"," ").replace(","," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("'"," ").replace('"',' ').replace("-"," ").replace("_"," "):

        
        Fig("cybermedium",'This tweet contains banned words :')
        
        print(tweet)
        
        print("** %s **" % str(forbid))
        
        Fig("",'Going To Trash ...')
        print("*=*=*=*=*=*=*=*=*=*")
        
        Banned = True
        Total_Ban_By_Keywords_Nbr = Total_Ban_By_Keywords_Nbr + 1
        time.sleep(Config.Time_Sleep)
        for forbid in Banned_Word_list:
            if Banned is False:
                if str(forbid.lower()) in str(bio.lower()):

                        
                        Fig("cybermedium",'This user profile contains banned words :')
                        
                        print(bio)
                        
                        print("** %s **" % str(forbid))
                        
                        Fig("cybermedium",'Going To Trash ...')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = True
                        Total_Ban_By_Keywords_Nbr = Total_Ban_By_Keywords_Nbr + 1
                        time.sleep(Config.Time_Sleep)

        for forbid in Banned_User_list:
           if Banned is False:
                if str(forbid.lower()) in str(sender.lower()):

                        
                        Fig("cybermedium",'This tweet is from a banned user :')
                        
                        print(tweet)
                        
                        print("** %s **" % forbid)
                        
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = True
                        Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
                        time.sleep(Config.Time_Sleep)

        for forbid in Ban_Double_List:
           if Banned is False:
                if forbid in tweet:

                        
                        Fig("cybermedium",'This tweet is Identical to a Previous tweet :')
                        
                        print(tweet)
                        
                        Saveid(id)
                        
                        Fig("",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = True
                        Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
                        time.sleep(Config.Time_Sleep)


  for item in Ban_Double_List:

    if Banned is False and len(item) > 10:
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
                          Banned = True
                          Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
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



  if Banned is False:
    if tweet.count("@") >= 3:


                  Fig("basic",'Follow Friday')
                  Fig("cybermedium",'Going To Trash')
                  print("*=*=*=*=*=*=*=*=*=*")
                  
                  Banned = True
                  Total_Ban_By_FollowFriday_Nbr = Total_Ban_By_FollowFriday_Nbr +1
                  time.sleep(Config.Time_Sleep)

    if tweet.count("#") >= 3:

                  Fig("basic",'HashTags Fever')
                  Fig("cybermedium",'Going To Trash')
                  print("*=*=*=*=*=*=*=*=*=*")
                  
                  Banned = True
                  Total_Ban_By_TooManyHashtags_Nbr = Total_Ban_By_TooManyHashtags_Nbr + 1
                  time.sleep(Config.Time_Sleep)

    if Tweets_By_Same_User.count(str(sender)) >= Config.Maximum_Tweet_By_User:
                        Fig("basic",'Too many Tweets From this user ')
                        Fig("cybermedium",'Going To Trash')
                        print("*=*=*=*=*=*=*=*=*=*")
                        
                        Banned = True
                        Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
                        time.sleep(Config.Time_Sleep)
    else:
                        figy = "Nbr of tweets for this user : ",str(Tweets_By_Same_User.count(sender))
                        Fig("cybermedium",str(figy))
                        print("*=*=*=*=*=*=*=*=*=*")
                        time.sleep(Config.Time_Sleep)


  if Banned is False:

                Fig("speed",'Good To Go !!')
                print("*=*=*=*=*=*=*=*=*=*")
                time.sleep(Config.Time_Sleep)


def Saveid(id):

                Fig("rev",'Saveid()')
                time.sleep(Config.Time_Sleep)

                checkfile(Pth_Tweets_Sent)

                file = open(Pth_Tweets_Sent,"a")
                file.write("\n"+str(id))
                file.close()
                print("*=*=*=*=*=*=*=*=*=*")
                print("Id :",id)
                Fig("larry3d",'Saved')
                print("*=*=*=*=*=*=*=*=*=*")
                time.sleep(Config.Time_Sleep)


def Idlist(id):
    global Banned
    global Total_Sent_Nbr
    global Id_Done_Trigger

    Fig("rev",'Idlist()')
    time.sleep(Config.Time_Sleep)

    if Id_Done_Trigger == False:
        checkfile(Pth_Tweets_Sent)


        empty = cleanfile(Pth_Tweets_Sent)


        Total_Sent_Nbr = sum(1 for line in open(Pth_Tweets_Sent))
        Id_Done_Trigger = True

    file = open(Pth_Tweets_Sent,"r+")
    lines = file.read().splitlines()

    for saved in lines:

      if saved != "\n" or saved != "":
         if str(saved) in str(id):

               print("*=*=*=*=*=*=*=*=*=*")
               print("Id from file :",saved)
               print("tweet id :",id)
               print("*=*=*=*=*=*=*=*=*=*")
               Banned = True
               time.sleep(Config.Time_Sleep)
               return(True)

    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    Fig("basic",'Unknown Tweet ID')
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    return(False)




def Scoring(tweet,search):

  global Api_Call_Nbr
  global Total_Call_Nbr
  global Update_Call_Nbr
  global Total_Update_Call_Nbr
  global Banned
  global Ban_Double_List
  global AvgScore
  global Tweet_Age
  global Totale_Score_Nbr
  global Total_Already_Send_Nbr
  global Total_Ban_By_Lang_Nbr
  global Total_Ban_By_Date_Nbr
  global Tweets_By_Same_User
  global RestABit_Trigger
  global ERRORCNT
  global Wait_Hour_Trigger
  global Wait_Half_Hour_Trigger
  global RetweetSave

  Bouffon = 0
  Score = 0
  Banned = False
  now = datetime.datetime.now()

  
  
  
  Fig("rev",'Scoring()')
  

  if TAK.OAUT_1 is True:
     Tweext = tweet['text']
  elif TAK.OAUT_2 is True:
     Tweext = tweet["full_text"]

  print("*************************************************************************************")
  Fig("basic",'Starting Scoring function')
  print("")

  if 'screen_name' in tweet['user'] :
                        tstjester = tweet['user']['screen_name']
                        if tstjester in Config.Special_Users:
                               Bouffon = 1





  if len(Tweext) < Config.Minimum_Tweet_Length :
                                Banned = True
                                Fig("cybermedium",'NOT ENOUGH TEXT')
                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
  if Banned is False or Bouffon == 1:
    if 'retweet_count' in tweet:

      print("##")
      print("This tweet has been retweeted %i times " % tweet['retweet_count'])
      print("##")
      LuckyLuke = randint(0,Config.Luck_Factor)
      if tweet['retweet_count'] < Config.Minimum_Tweet_Retweet and LuckyLuke != 1:
                                Banned = True
                                Fig("cybermedium",'NOT ENOUGH RETWEET')
                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
                                time.sleep(Config.Time_Sleep)

      if tweet['retweet_count'] < Config.Minimum_Tweet_Retweet and LuckyLuke == 1:
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
                        if tweet['retweet_count'] > Config.Maximum_Tweet_Retweet:
                                Fig("cybermedium",'Too many Retweets checking if this tweet is from a known user or friend..')
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
                                        Banned = True


      else:
           pass


                                




  if 'entities' in tweet:
     if Banned is False or Bouffon == 1:
         if 'symbols' in tweet['entities'] and len(tweet['entities']['symbols']) > Config.Maximum_Tweet_Emoticon:
              print("##")
              print("This tweet contains a Symbol and must die for no reason. ")
              print("##")
              Banned = True
              time.sleep(Config.Time_Sleep) 

     if Banned is False or Bouffon == 1:
      nogo = 0
      if 'urls' in tweet['entities'] and len(tweet['entities']['urls']) > Config.Minimum_Link_In_Tweet:
               print("##")
               print("This tweet contains a link : ",tweet['entities']['urls'][-1]['expanded_url'])
               print("##")
               Score = Score + 3
               if 'hashtags' in tweet['entities'] and len(tweet['entities']['hashtags']) > Config.Minimum_Link_In_Tweet:
                        print("##")
                        print("This tweet contains Hashtag : ",tweet['entities']['hashtags'][-1]['text'])
                        print("##")
                        Score = Score + 1


               if 'media' in tweet['entities'] and len(tweet['entities']['media']) > Config.Minimum_Media_In_Tweet:
                        print("##")
                        print("This tweet contains Media : ",tweet['entities']['media'][-1]['media_url'])
                        print("##")
                        Score = Score + 3

               if tweet['favorite_count'] > Config.Minimum_Tweet_Fav:

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
                        if fav >= Config.Maximum_Tweet_Fav:
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
                               Banned = True
           






      if 'followers_count' in tweet['user'] and tweet['user']['followers_count'] > Config.Minimum_User_Following:
                        print("##")
                        print("Source followers count : ",tweet['user']['followers_count'])
                        print("##")

                        if tweet['user']['followers_count'] <= Config.Minimum_User_Friend:
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
                                        Banned = True
                                


                                Fig("cybermedium",'Going To Trash')
                                print("*=*=*=*=*=*=*=*=*=*")
                                Banned = True
                                Score = Score - 10000
                        if tweet['user']['followers_count'] > Config.Minimum_User_Friend:
                                Score = Score + 2
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

      if 'user_mentions' in tweet['entities'] and len(tweet['entities']['user_mentions']) > Config.Minimum_Tweet_Mention:
                        print("##")
                        print("This tweet is mentioning someone : ",tweet['entities']['user_mentions'][-1]['screen_name'])
                        print("##")

                        Score = Score + 1

                        if tweet['entities']['user_mentions'][-1]['screen_name'] in Config.Special_Users:
                               
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

          if (coop in Config.Special_Users) or Bouffon == 1:


                  Score = Score + 9000
                  randodge = ['Cool ','Gorgeous ','Soft ','Enjoy ','Totally ','Awesome ','Fun ','Easy ','Free ','Wow ','Much ','Many ','Too ','So ','Such ','Very ','Amaze ']
                  dodgecoin = str(choice(randodge)) + str(choice(Banned_Word_list)) + " "
                  time.sleep(Config.Time_Sleep)
                  print("================================================================================")
                  
                  Fig("basic",'SUCH SCORE !!')
                  
                  figy = "Score = %i" % Score
                  Fig("puffy",str(figy))
                  
                  Fig("basic",'MUCH TWEET !!')
                  
                  Fig("puffy","Text:")
                  Fig("digital",Tweext)
                  time.sleep(Config.Time_Sleep)
                  
                  Fig("basic",'MANY RETWEET !!')
                  
                  figy = "Retweets = %i" % tweet['retweet_count']
                  Fig("puffy",str(figy))
                  time.sleep(Config.Time_Sleep)
                  
                  Fig("basic",'SO FAVORITE !!')
                  
                  figy = "Favourites = %i" % tweet['favorite_count']
                  Fig("puffy",str(figy))
                  time.sleep(Config.Time_Sleep)
                  
                  Fig("basic",'VERY TREND !!')
                  
                  figy = "Followers = %i" % tweet['user']['followers_count']
                  Fig("puffy",str(figy))
                  time.sleep(Config.Time_Sleep)
                  
                  Fig("basic",'AMAZE TWEET!!')
                  
                  print("================================================================================")
                  figy = "Amaze Now !"
                  Fig("puffy",str(figy))
                  link = "https://twitter.com/"+ str(choice(randodge).replace(" ","")) + "/status/" + str(tweet['id'])
                  twit = Tweext.replace("@th3j35t3r","th3b0uf0n").replace("th3j35t3r","th3b0uf0n").replace("@jonathandata1","charlathandata1").replace("jonathandata1","charlathandata1")
                  dodgelink = str(dodgecoin) + " " + str(link)
                  time.sleep(Config.Time_Sleep)
                  limits()

                  Banned = False
                  for forbid in Ban_Double_List:
                    if Banned is False:
                      if forbid in Tweext:

                              Fig("cybermedium",'This tweet is Identical to a Previous tweet :')
                              print(Tweext)
                              Saveid(tweet['id'])
                              Fig("cybermedium",'Going To Trash')
                              print("*=*=*=*=*=*=*=*=*=*")
                              Banned = True
                              Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
                              time.sleep(Config.Time_Sleep)


                  for item in Ban_Double_List:

                    if Banned is False and len(item) > 10:
                         pos = 0
                         lng = len(item)
                         half = lng / 2
                         next = int(half) + pos
                         sample = item[pos:int(half)]
                         maxpos = pos + int(len(sample))

                         while int(maxpos) < int(lng):
                              try:
                                   if str(sample) in str(Tweext) and str(sample) != " ":
                                        
                                        Fig("cybermedium",'Some parts are Identicals to a Previous Tweet :')
                                        print("Tweet :",Tweext)
                                        
                                        print("Found Matched :",sample)
                                        Saveid(id)
                                        
                                        Fig("cybermedium",'Going To Trash')
                                        print("*=*=*=*=*=*=*=*=*=*")
                                        time.sleep(Config.Time_Sleep)

                                        
                                        maxpos = int(lng)
                                        Banned = True
                                        Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
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

                  if Banned is False:
                       SaveDouble(str(twit))
                       try:
                         print(twit)
                          
                         if len(dodgelink) > 140:
                               dodgelink = dodgelink[:140]
                         if len(twit) > 140:
                              twit = twit[:137] + "..."
                         
                         IrSend(twit)

                         time.sleep(Config.Time_Sleep)
                         

                         IrSend(dodgelink)

                         Fig("cybermedium","DONE")
                         Api_Call_Nbr = Api_Call_Nbr + 2
                         Update_Call_Nbr = Update_Call_Nbr + 2
                         Saveid(tweet['id'])
                         if ERRORCNT > 0:
                                                          ERRORCNT = ERRORCNT - 1


                       except Exception as e:
                         Fig("bell",'Twython Error')

                         print(e)


                       Banned = True
                  else:
                    print("================================================================================")
                    Fig("cybermedium",' WOW Already Sent !!')
                    print("================================================================================")
                    time.sleep(Config.Time_Sleep)
  TwtTime = tweet['created_at']
  TwtTime = TwtTime.replace(" +0000 "," ")
  Timed = datetime.datetime.strptime(TwtTime,'%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
  TimeFinal = datetime.datetime.strptime(Timed,'%Y-%m-%d %H:%M:%S')
  Tweet_Age = now - TimeFinal
  print("This tweet was send at : ",TwtTime)

  LuckyLuke = randint(0,Config.Luck_Factor)

  if Banned is False:
      if Tweet_Age.days >= Config.Maximum_Tweet_DayOld:
               Fig("basic",'WAY TOO OLD !')
               if LuckyLuke != 1:
                     Banned = True
                     Total_Ban_By_Date_Nbr = Total_Ban_By_Date_Nbr + 1
               else:
                    Fig("basic",'But who cares !')
      else:
            Score = Score + 12
  if Banned is False:
    if 'retweeted_status' in tweet :
      if 'created_at' in tweet['retweeted_status'] and len(tweet['retweeted_status']['created_at']) > 0:
          RtTime = tweet['retweeted_status']['created_at']
          RtTime = RtTime.replace(" +0000 "," ")
          RtTimed = datetime.datetime.strptime(RtTime,'%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d %H:%M:%S')
          RtTimeFinal = datetime.datetime.strptime(RtTimed,'%Y-%m-%d %H:%M:%S')
          RtTweet_Age = now - RtTimeFinal
          print("Retweet created at :" ,RtTimeFinal)

          if RtTweet_Age.days >= Config.Maximum_Retweet_DayOld:
                Fig("basic",'WAY TOO OLD !')
                if LuckyLuke != 1:
                       Banned = True
                       Total_Ban_By_Date_Nbr = Total_Ban_By_Date_Nbr + 1
                else :
                       Fig("basic",'But who cares !')
      else:
            Score = Score + 6
  if Banned is False:
    if Tweet_Age.seconds < 3600:
      Score = Score + 23
      print("Less than an hour ago .")
      print("Score = + 23")
      print("Score = ",Score)

    if Tweet_Age.seconds > 3600 and Tweet_Age.seconds <= 7200:
      Score = Score + 2 + 2
      print("An hour ago .")
      print("Score = + 22")

    if Tweet_Age.seconds > 7200 and Tweet_Age.seconds <= 10800:
                  Score = Score + 21
                  print("Two hours ago .")
                  print("Score = + 21")

    if Tweet_Age.seconds > 10800 and Tweet_Age.seconds <= 14400:
                  Score = Score + 20
                  print("Three hours ago .")
                  print("Score = + 20")

    if Tweet_Age.seconds > 14400 and Tweet_Age.seconds <= 18000:
                  Score = Score + 19
                  print("Four hours ago .")
                  print("Score = + 19")

    if Tweet_Age.seconds > 18000 and Tweet_Age.seconds <= 21600:
                  Score = Score + 18
                  print("Five hours ago .")
                  print("Score = + 18")

    if Tweet_Age.seconds > 21600 and Tweet_Age.seconds <= 25200:
                  Score = Score + 17
                  print("Six hours ago .")
                  print("Score = + 17")

    if Tweet_Age.seconds > 25200 and Tweet_Age.seconds <= 28800:
      Score = Score + 16
      print("Seven hours ago .")
      print("Score = + 16")

    if Tweet_Age.seconds > 28800 and Tweet_Age.seconds <= 32400:
                  Score = Score + 15
                  print("Eight hours ago .")
                  print("Score = + 15")

    if Tweet_Age.seconds > 32400 and Tweet_Age.seconds <= 36000:
                  Score = Score + 14
                  print("Nine hours ago .")
                  print("Score = + 14")
    if Tweet_Age.seconds > 36000 and Tweet_Age.seconds <= 39600:
                  print("Ten hours ago .")
                  print("Score = + 13")
                  Score = Score + 13
    if Tweet_Age.seconds > 39600 and Tweet_Age.seconds <= 43200:
                  Score = Score + 12
                  print("Eleven hours ago .")
                  print("Score = + 12")
                  print("Score = ",Score)


    if Tweet_Age.seconds > 43200 and Tweet_Age.seconds <= 46800:
                  print("Twelve hours ago .")
                  Score = Score + 11
                  print("Score = + 11")
                  print("Score = ",Score)


    if Tweet_Age.seconds > 46800 and Tweet_Age.seconds <= 50400:
                  Score = Score + 10
                  print("Thirteen hours ago .")
                  print("Score = + 10")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 50400 and Tweet_Age.seconds <= 54000:
                  Score = Score + 9
                  print("Fourteen hours ago .")
                  print("Score = + 9")


    if Tweet_Age.seconds > 54000 and Tweet_Age.seconds <= 57600:
                  Score = Score + 8
                  print("Fiveteen hours ago .")
                  print("Score = + 8")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 57600 and Tweet_Age.seconds <= 61200:
                  Score = Score + 7
                  print("Sixteen hours ago .")
                  print("Score = + 7")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 61200 and Tweet_Age.seconds <= 64800:
                  Score = Score + 6
                  print("Seventeen hours ago .")
                  print("Score = + 6")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 64800 and Tweet_Age.seconds <= 68400:
                        Score = Score + 5
                        print("Eighteen hours ago .")
                        print("Score = + 5")
                        print("Score = ",Score)

    if Tweet_Age.seconds > 68400 and Tweet_Age.seconds <= 72000:
                  Score = Score + 4
                  print("Nineteen hours ago .")
                  print("Score = + 4")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 72000 and Tweet_Age.seconds <= 75600:
                  Score = Score + 3
                  print("twenty hours ago .")
                  print("Score = + 3")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 75600 and Tweet_Age.seconds <= 79200:
                  Score = Score + 2
                  print("Twenty one hours ago .")
                  print("Score = + 2")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 79200 and Tweet_Age.seconds <= 82800:
                  Score = Score + 1
                  print("Twenty two hours ago .")
                  print("Score = + 1")
                  print("Score = ",Score)

    if Tweet_Age.seconds > 82800 and Tweet_Age.seconds < 86400:
                  print("Twenty three hours ago .")
                  Score = Score + 0
                  print("Score = + 0")
                  print("Score = ",Score)

  AvgScore.append(Score)

  if tweet['lang'] in Config.Allowed_Tweet_Lang:

    AlreadySend = Idlist(tweet['id'])

    if AlreadySend is False:

      Ban(Tweext,tweet['user']['screen_name'],tweet['id'],tweet['user']['description'])

      if Banned is False:
          if Score >= Config.Minimum_Tweet_Score:
               Tweext = Tweext.replace("\n"," ")
               print("######################################")
               print('Adding to Retweet List')
               print("Nbr of tweets in queue :",len(Retweet_List))
               print("Tweet Score : ",Score)
               print("Tweet ID :", tweet['id'])
               print("Current ApiCall Count :",Api_Call_Nbr)
               print("Total Number Of Calls :",Total_Call_Nbr)
               print("Current Update Status Count :",Update_Call_Nbr)
               print("Total Number Of Update Calls :",Total_Update_Call_Nbr)
               print("Search Call left :",search)
               print("Tweet :", Tweext)
               print("######################################")
               print("")
               
               time.sleep(Config.Time_Sleep)
               Tweets_By_Same_User.append(tweet['user']['screen_name'])
               Retweet_List.append(Tweext)
               Ban_Double_List.append(Tweext)
               clickme = "https://twitter.com/"+str(tweet['user']['screen_name'])+"/status/"+str(tweet['id'])
               Format_To_Irc ="From:%s %s -> %s Hype:%s"%(tweet['user']['screen_name'],Tweext,clickme,Score)
               IrSend(Format_To_Irc,True)
               time.sleep(Config.Time_Sleep)
               SaveDouble(Tweext)

          else:
                                        print("")
                                        Fig("epic","But ..")
                                        print("================================================================================")
                                        figy = "Score = %i" % Score
                                        Fig("puffy",str(figy))
                                        print("================================================================================")
                                        print("Score = ",Score)
                                        print("================================================================================")
                                        print(Tweext)
                                        print("================================================================================")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("This tweet does not match the requirement to be retweeted. (Score)")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("================================================================================")
                                        print("")
                                        Totale_Score_Nbr = Totale_Score_Nbr + 1
                                        time.sleep(Config.Time_Sleep)
      else:
                                  print("")
                                  Fig("epic","But ..")
                                  print("================================================================================")
                                  Fig("cybermedium","Banned")
                                  print("================================================================================")
                                  print(Tweext)

                                  print("================================================================================")
                                  print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                  print("This tweet does not match the requirement to be retweeted.")
                                  print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                  print("================================================================================")
                                  print("")
                                  time.sleep(Config.Time_Sleep)
    else:
                                        print("")
                                        Fig("epic","But ..")
                                        print("================================================================================")
                                        Fig("cybermedium","Already sent !")
                                        print("================================================================================")
                                        print(Tweext)

                                        print("===================================")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("This tweet has been already sent ..")
                                        print(":( :( :( :( :( :( :( :( :( :( :( :(")
                                        print("===================================")
                                        print("")
                                        Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
                                        time.sleep(Config.Time_Sleep)



  else:
                                
                                Fig("epic","but ..")
                                print("================================================================================")
                                Fig("cybermedium","Language")
                                print("===============================================================================")
                                print("Language : ",tweet['lang'])
                                print(Tweext)
                                print("================================================================================")
                                print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                print("This tweet does not match the requirement needed to be retweeted.")
                                print(":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :(")
                                print("================================================================================")
                                print("")
                                time.sleep(Config.Time_Sleep)
                                Total_Ban_By_Lang_Nbr = Total_Ban_By_Lang_Nbr +1

def Search_Keyword(word):
  global Api_Call_Nbr
  global Update_Call_Nbr
  global Twitter_Api
  global RestABit_Trigger
  global Search_Done_Trigger
  global Search_Limit_Trigger
  global Search_ApiCallLeft_Nbr

  Fig("rev",'Searching()')
  time.sleep(Config.Time_Sleep)
  ratechk = 0

  if Search_Done_Trigger == False:

    try :
            Twitter_Api = WakeApiUp()
            ratechk = 1
  
    except Exception as e:
  
      print("mysterious error")
      
      print(e)
      Twitter_Api = WakeApiUp()
      RestABit_Trigger = True
      limits()
      if ratechk != 1:
                  Search_ApiCallLeft_Nbr = 23
                  ratechk = 1

    if Search_ApiCallLeft_Nbr > 2:
           
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
               Twitter_Api = WakeApiUp()
               searchresults = Twitter_Api.search(q=word,tweet_mode="extended",count=100)
               print("##########################################")
               Fig("colossal",'%s Results Found !'%len(searchresults["statuses"]))
               #print(searchresults)
               #time.sleep(10)
               print("##########################################")
               Api_Call_Nbr = Api_Call_Nbr + 1
               Search_ApiCallLeft_Nbr = Search_ApiCallLeft_Nbr - 1
               time.sleep(Config.Time_Sleep)
         
           except Exception as e:
                         Api_Call_Nbr = Api_Call_Nbr + 1
                         print("Error search1:",e)
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         print("Error Sorry im trying next one")
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         
         
           try:
               
               print("==")
               print("Loading tweets for " + word)
               print("")
               time.sleep(Config.Time_Sleep)
               print("==")
               print("")
               time.sleep(Config.Time_Sleep)
               print("")
       
           except Exception as e:
                         Api_Call_Nbr = Api_Call_Nbr + 1
                         print("Error search2:",e)
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         print("Error Sorry trying next one")
                         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                         
                         time.sleep(Config.Time_Sleep)
           
           
           
           print("##########################################")
           print("**")
           Fig("doom",'Search function Terminated')
           print("**")
           print("##########################################")
           try:
               if len(searchresults["statuses"]) > Config.Minimum_Search_Result :
                    for item in searchresults["statuses"]:
                         time.sleep(Config.Time_Sleep)
                         if MasterPause_Trigger is False:
                             Scoring(item,Search_ApiCallLeft_Nbr)
                         else:
                             while True:
                                 time.sleep(Config.Time_Sleep)
                                 if MasterPause_Trigger is False:
                                     break
                             Scoring(item,Search_ApiCallLeft_Nbr)


               else:
                    print("****************************************")
                    
                    Fig("caligraphy",'No Result')
                    
                    

                    print("????????????????????????????")
                    print("Sorry not enough results for : ",word)
                    print("Maybe you should consider changing it ")
                    print("????????????????????????????")
                    
                    
                    
                    print("****************************************")
                    Fig("basic",'Saving unwanted search to no.result')
                    time.sleep(Config.Time_Sleep)
                    checkfile(Pth_NoResult)

                    file = open(Pth_NoResult,"a")
                    file.write(str(word) + "\n")
                    file.close()
           except Exception as e:
                print(e)


    else:
      
      Search_Limit_Trigger = True
      Search_Done_Trigger = False
      limits()



#Some Code
def RedQueen():

    global Keywords
    global MasterPause_Trigger

    while 1:
          if GOGOGO_Trigger == True:
               break

    Fig("basic","GOGOGO!",True)
    time.sleep(Config.Time_Sleep)
    
    loadvars()
    time.sleep(Config.Time_Sleep)
    CheckDouble()
    time.sleep(Config.Time_Sleep)
    
    Fig("basic",'Loading Emoticon',True)
    
    time.sleep(Config.Time_Sleep)
    for use_aliases, group in ((False, emoji.unicode_codes.EMOJI_UNICODE),(True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE)):
                         for name, ucode in list(group.items()):
                                  assert name.startswith(':') and name.endswith(':') and len(name) >= 3
                                  emj = emoji.emojize(name, use_aliases=use_aliases)
                                  Emoji_List.append(emj)
    print(Emoji_List)
    
    Fig("cybermedium",'Done')
    time.sleep(Config.Time_Sleep)
    Fig("basic",'Calling Flush function',True)
    
    flushtmp()
    
    Fig("basic",'Calling Search function',True)
    
    time.sleep(Config.Time_Sleep)

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
                            status="Redqueen started at "+ str(CurrentDate) + " Searching " + str(rndwords) + " items ."
                            IrSend(status)
                            print("")
                            Fig("basic",'Status sent !"')

    except Exception as e:
                            print(e)
                            print("fuck")
                            time.sleep(Config.Time_Sleep)

    time.sleep(Config.Time_Sleep)

    Fig("cybermedium","Check Last Menu started",True)

    checkmenu(Keywords)

    if Menu_Check_Trigger == True:
      Keywords = New_Keywords_List
      
      
      print("**")
      
      print("==")
      Fig("basic","New Menu for today !",True)
      print("==")
      
      
      print(Keywords[:rndwords])
      
      print("Total search terms : ",rndwords)
      
      
      print("**")
      
      time.sleep(Config.Time_Sleep)
    tmpcnt= 0
    if MasterStart_Trigger is False:
       print("**Waiting for !start command.**")
       IrSend("Idle mode..")
    else:
       IrSend("Redqueen is starting..")

    while True:
       time.sleep(Config.Time_Sleep)
       if MasterStart_Trigger is True:
          figy = "Starting Redqueen"
          Fig("puffy",figy)
          break

    for key in Keywords[:rndwords]:
      time.sleep(Config.Time_Sleep)
      if MasterPause_Trigger is False and MasterStart_Trigger is True:
          if MasterStop_Trigger is True:
                MasterStart_Trigger == False
                return(IrSend("Redqueen has been stopped"))
          tmpcnt = tmpcnt + 1
          figy = "Searching : %s %i/%i" % (key,tmpcnt,rndwords)
          Fig("puffy",figy)
          time.sleep(Config.Time_Sleep)
          Search_Keyword(key)
      else:
          while True:
                time.sleep(Config.Time_Sleep)
                if MasterStop_Trigger is True:
                   MasterStart_Trigger == False
                   return(IrSend("Redqueen has been stopped"))
                if MasterPause_Trigger is False and MasterStart_Trigger is True:
                     break
          tmpcnt = tmpcnt + 1
          figy = "Searching : %s %i/%i" % (key,tmpcnt,rndwords)
          Fig("puffy",figy)
          time.sleep(Config.Time_Sleep)
          Search_Keyword(key)


    Fig("basic","All Done !",True)
    
    
    time.sleep(Config.Time_Sleep)
    
    Fig("basic","Calling Save Search Terms Function",True)

    time.sleep(Config.Time_Sleep)
    lastmeal(Keywords[:rndwords])
    
    if (len(AvgScore)) != 0:
      avgscore = sum(AvgScore) / float(len(AvgScore))
    else:
      avgscore = 0
    try:
      dbrief= "*Redqueen Debrief* -Searchs: "+ str(rndwords) +"-Twts:" + str(len(AvgScore)) + "-Avg Score:" + str(avgscore) + "-Rtwts:" + str(RetweetSave)+ "-Tcall:" + str(Total_Call_Nbr) + "-Ucall:" + str(Total_Update_Call_Nbr)

      IrSend(dbrief)

      Fig("basic",'Status sent !')

    except Exception as e:
                            print(e)
                            print("fuck")
                            time.sleep(Config.Time_Sleep)

    
    Fig("basic","Calling Saving call function",True)
    
    

    SaveTotalCall(Api_Call_Nbr,Update_Call_Nbr)

    print("##############################################################################################################")
    print("##############################################################################################################")
    Fig("basic","The End")
    print("##############################################################################################################")
    print("##############################################################################################################")
    MasterPause_Trigger = True

if __name__ == '__main__':

     try:
          Screen.wrapper(title)
     except Exception as e:
       print("Title Error line 3257 :",e)

     if True is TAK.OAUT_1 and True is TAK.OAUT_2:
            print("You much choose between TAK.OAUT_1 and TAK.OAUT_2 in TwitterApiKeys.py")
            sys.exit()
     if False is TAK.OAUT_1 and False is TAK.OAUT_2:
            print("You much choose between TAK.OAUT_1 and TAK.OAUT_2 in TwitterApiKeys.py")
            sys.exit()

     if TAK.OAUT_1 is True:
          for lenchk in [len(TAK.oa1_app_key),len(TAK.oa1_app_secret),len(TAK.oa1_oauth_token),len(TAK.oa1_oauth_token_secret)]:
              if lenchk < 25:
                 print("All TAK.OAUT_1 keys must be filled and correct in TwitterApiKeys.py")
                 sys.exit()

     if TAK.OAUT_2 is True:
          for lenchk in [len(TAK.oa2_app_key),len(TAK.oa2_access_token)]:
              if lenchk < 25:
                 print("ALL TAK.OAUT_2 must be filled and correct in TwitterApiKeys.py")
                 sys.exit()
     print("Testing api:")
     WakeApiUp()

     Fig("cybermedium","Launching Blueking on IRC")
     time.sleep(Config.Time_Sleep)

     Fig("rev","IrSweet()")
     Fig("cybermedium","Waiting for idle mode")
     time.sleep(Config.Time_Sleep)
     Thread(target = IrSweet).start()
     Thread(target = RedQueen).start()







#################################################TheEnd#############################################################


