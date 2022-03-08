#!/usr/bin/python3

from pbwrap import Pastebin
from random import randint, choice, shuffle
from twython import Twython
from pyfiglet import Figlet
from threading import Thread
import re, socket, time, sys, os, inspect, cherrypy, string, datetime, emoji, feedparser, csv
import Config, IrcKey, PastebinApiKey
import TwitterApiKeys as TAK

# Some Vars


GOGOGO_Trigger = False

Shutdown_Trigger = False

MasterPause_Trigger = False

MasterStop_Trigger = False

MasterStart_Trigger = False

Broken_pipe_Trigger = False

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

Pth_Web = os.path.dirname(os.path.abspath(__file__)) + "/Data/www/"

Pth_Img_Rq = Pth_Web + "img/redqueen-profile.png"

Pth_Save = Pth_Data + "Save/"

Pth_TotalApi_Call = str(Pth_Data) + "TotalApi.Call.Rq"

Pth_Update_Call = str(Pth_Data) + "Update.Status.Call.Rq"

Pth_Already_Searched_Rq = str(Pth_Data) + "Already.Searched.Rq"

Pth_Keywords_Rq = str(Pth_Data) + "Keywords.Rq"

Pth_Users_Timelines_Rq = str(Pth_Data) + "Users.Timelines.Rq"

Pth_Following_Rq = str(Pth_Data) + "Following.Rq"

Pth_Friends_Rq = str(Pth_Data) + "Friends.Rq"

Pth_Banned_People_Rq = str(Pth_Data) + "Banned.People.Rq"

Pth_Banned_Word_Rq = str(Pth_Data) + "Banned.Word.Rq"

Pth_Rss_Rq = str(Pth_Data) + "Rss.Feeds.Rq"

Pth_Request_Log = str(Pth_Data) + "Request.log.Rq"

Pth_Error_Log = str(Pth_Data) + "Errors.log.Rq"

Pth_Current_Session = str(Pth_Data) + "Current.Session.Rq"

Pth_NoResult_Rq = str(Pth_Data) + "No.Result.Rq"

Pth_Tweets_Id_Rq = str(Pth_Data) + "Tweets.Id.Sent.Rq"

Pth_Text_Sent_Rq = str(Pth_Data) + "Tweets.Txt.Sent.Rq"

Pth_Rq_Server_Save = str(Pth_Data) + "Server.Save.Rq"

Pth_Url_Sent_Rq = str(Pth_Data) + "Url.Sent.Rq"


RestABit_Trigger = False

Twitter_Api = ""

Keywords_List = []

Timelines_List = []

Following_List = []

Friends_List = []

Banned_Word_list = []

Banned_User_list = []

Ban_Double_List = []

Ban_Double_Url_List = []

Rss_Url_List = []

Requested_Cmd_List = []

Already_Searched_List = []

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

Start_Date = ""

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


Extracted_Datas = []

Template_Header = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://kit.fontawesome.com/7e675542d3.js" crossorigin="anonymous"></script>
    <link href="css/static_style.css" rel="stylesheet">
    <title>Redqueen</title>
    <meta name="description" content="">
    <meta name="author" content="On4r4p">
    <link rel="icon" href="img/Rdfavicon.ico">
    <style> %s </style>
  </head>
  <body style="  background-color: #15202b;">"""

Template_Footer = "</body></html>"

Cherryconf = {
    "/": {"tools.sessions.on": True, "tools.staticdir.root": Pth_Web + "WebTemplate"},
    "/favicon.ico": {
        "tools.staticfile.on": True,
        "tools.staticfile.filename": Pth_Web + "WebTemplate/img/Rdfavicon.ico",
    },
    "/css": {"tools.staticdir.on": True, "tools.staticdir.dir": "./css"},
    "/img": {"tools.staticdir.on": True, "tools.staticdir.dir": "./img"},
    "global": {
        "environment": "production",
        "log.screen": True,
        "server.socket_host": "0.0.0.0",
        "server.socket_port": 8080,
        "engine.autoreload_on": True,
    },
}

# Some Defs


class Redqueen_Server:
    def header(self):
        css_box = GenCss()
        return str(Template_Header) % css_box

    def footer(self):
        return Template_Footer

    @cherrypy.expose
    def index(self):
        timeline = GenFeed()

        yield self.header()

        for feed in timeline:
            yield feed

        yield self.footer()

    @cherrypy.expose
    def redqueen_retweet(self, rid=None):
        if rid != None and rid.isnumeric():
            print("About to Retweet : ", rid)

            try:
                Twitter_CherryApi = Twython(
                    TAK.oa1_app_key,
                    TAK.oa1_app_secret,
                    TAK.oa1_oauth_token,
                    TAK.oa1_oauth_token_secret,
                )
                Twitter_CherryApi.retweet(id=rid)
            except Exception as e:
                Betterror(e, inspect.stack()[0][3])
        else:
            print("not num:", rid)
        return self.index()

    @cherrypy.expose
    def redqueen_favorite(self, fid=None):
        if fid != None and fid.isnumeric():
            print("About to Fav : ", fid)

            try:
                Twitter_CherryApi = Twython(
                    TAK.oa1_app_key,
                    TAK.oa1_app_secret,
                    TAK.oa1_oauth_token,
                    TAK.oa1_oauth_token_secret,
                )
                Twitter_CherryApi.create_favorite(id=fid)
            except Exception as e:
                Betterror(e, inspect.stack()[0][3])
        else:
            print("not num:", fid)
        return self.index()


def Extract_Tweet_Data(tweet):
    global Extracted_Datas
    #       print("Tweet:\n",tweet)
    #       print()
    ##
    if "retweeted_status" in tweet:

        Tweet_Id = str(tweet["retweeted_status"]["id"])
        Tweet_Timestamp = tweet["retweeted_status"]["created_at"]
        Tweet_Author = tweet["retweeted_status"]["user"]["screen_name"]
        Tweet_Author_Link = "https://twitter.com/" + Tweet_Author
        Tweet_Profile_Author = tweet["retweeted_status"]["user"]["profile_image_url"]
        Tweet_Favorite_Counter = tweet["retweeted_status"]["favorite_count"]
        Tweet_Retweet_Counter = tweet["retweeted_status"]["retweet_count"]
        Tweet_Origin_Link = (
            "https://twitter.com/" + str(Tweet_Author) + "/status/" + str(Tweet_Id)
        )
        Tweet_Rt_Author = tweet["user"]["screen_name"]
        Tweet_Rt_Author_Link = "https://twitter.com/" + Tweet_Rt_Author

        Tweet_Url = []
        Tweet_Media = []
        if "media" in tweet["retweeted_status"]["entities"]:
            for media in tweet["retweeted_status"]["entities"]["media"]:
                Tweet_Media.append(media["media_url"])
        if "urls" in tweet["retweeted_status"]["entities"]:
            for url in tweet["retweeted_status"]["entities"]["urls"]:
                Tweet_Url.append(url["expanded_url"])

    else:

        Tweet_Id = str(tweet["id"])
        Tweet_Timestamp = tweet["created_at"]
        Tweet_Author = tweet["user"]["screen_name"]
        Tweet_Author_Link = "https://twitter.com/" + Tweet_Author
        Tweet_Profile_Author = tweet["user"]["profile_image_url"]
        Tweet_Favorite_Counter = tweet["favorite_count"]
        Tweet_Retweet_Counter = tweet["retweet_count"]

        Tweet_Origin_Link = (
            "https://twitter.com/" + str(Tweet_Author) + "/status/" + str(Tweet_Id)
        )
        Tweet_Rt_Author = ""
        Tweet_Rt_Author_Link = ""

        Tweet_Url = []
        Tweet_Media = []
        if "media" in tweet["entities"]:
            for media in tweet["entities"]["media"]:
                Tweet_Media.append(media["media_url"])
        if "urls" in tweet["entities"]:
            for url in tweet["entities"]["urls"]:
                Tweet_Url.append(url["expanded_url"])
    ##
    if "full_text" in tweet:
        Tweet_Text = tweet["full_text"]
    else:
        Tweet_Text = tweet["text"]

    #       print("Tweet_Origin_Link=",Tweet_Origin_Link)
    #       print("Tweet_Id = ",Tweet_Id)
    #       print("Tweet_Timestamp = ",Tweet_Timestamp)
    #       print("Tweet_Author = ",Tweet_Author)
    #       print("Tweet_Profile_Author =",Tweet_Profile_Author)
    #       print("Tweet_Author_Link=",Tweet_Author_Link)
    #       print("Tweet_Text=",Tweet_Text)
    #       print("Tweet_Rt_Author=",Tweet_Rt_Author)
    #       print("Tweet_Rt_Author_Link=",Tweet_Rt_Author_Link)
    #       print("Tweet_Favorite_Counter = ",Tweet_Favorite_Counter)
    #       print("Tweet_Retweet_Counter = ",Tweet_Retweet_Counter)
    #       print("Tweet_Media = ",Tweet_Media)
    #       print("Tweet_Url = ",Tweet_Url)
    Tweet_tuple = (
        Tweet_Origin_Link,
        Tweet_Id,
        Tweet_Timestamp,
        Tweet_Author,
        Tweet_Profile_Author,
        Tweet_Author_Link,
        Tweet_Text,
        Tweet_Rt_Author,
        Tweet_Rt_Author_Link,
        Tweet_Favorite_Counter,
        Tweet_Retweet_Counter,
        Tweet_Media,
        Tweet_Url,
    )

    if Tweet_Text not in Ban_Double_List:
        Extracted_Datas.append(Tweet_tuple)
        with open(Pth_Rq_Server_Save, "w") as file:
            writer = csv.writer(
                file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(
                [
                    "Tweet_Origin_Link",
                    "Tweet_Id",
                    "Tweet_Timestamp",
                    "Tweet_Author",
                    "Tweet_Profile_Author",
                    "Tweet_Author_Link",
                    "Tweet_Text",
                    "Tweet_Rt_Author",
                    "Tweet_Rt_Author_Link",
                    "Tweet_Favorite_Counter",
                    "Tweet_Retweet_Counter",
                    "Tweet_Media",
                    "Tweet_Url",
                ]
            )
            for ed in Extracted_Datas:
                writer.writerow(
                    [
                        ed[0],
                        ed[1],
                        ed[2],
                        ed[3],
                        ed[4],
                        ed[5],
                        ed[6],
                        ed[7],
                        ed[8],
                        ed[9],
                        ed[10],
                        ed[11],
                        ed[12],
                    ]
                )


def GenFeed():
    Tweets_Feed = []
    for nbr, D in enumerate(Extracted_Datas):

        Template_Tweet = (
            """    <div class="center-feeds-container">
      <div class="profile-picture"> <img src="%s" class="image">"""
            % (str(D[4]))
            + """ </div>
      <div class="center-feeds">
        <div class="main-tweet">
          <div class="on-actual-tweet">
            <div class="handle">
              <div class="handu"> <span>"""
            + """<a href="%s">%s</a>""" % (D[5], str(D[3]))
            + "</span>"
        )
        if len(D[7]) > 0:
            Template_Tweet += """ Rt by <a href="%s">%s</a> %s</div>""" % (
                D[8],
                D[7],
                D[2],
            )
        else:
            Template_Tweet += "  %s</div>" % (D[2])
        Template_Tweet += (
            """
            </div>
          </div>
          <div class="actual-tweet"> """
            + str(D[6])
            + """<a href="%s"> Tweet link</a>\n""" % (D[0])
        )

        if type(D[12]) == list:
            if len(D[12]) > 0:
                for link in D[12]:
                    Template_Tweet += """<a href="%s">%s</a>""" % (link, link)
            Template_Tweet += """ </div>
        </div>"""
        elif type(D[12]) == str:
            frmt = D[12].replace("[", "").replace("]", "")
            frmt = frmt.split(",")
            if len(frmt) > 0:
                for url in frmt:
                    if url.startswith("'") and url.endswith("'"):
                        url = url[1:]
                        url = url[:-1]
                        Template_Tweet += """<a href="%s">%s</a>""" % (url, url)
            Template_Tweet += """ </div>
        </div>"""

        if type(D[11]) == list:
            if len(D[11]) > 0:
                for media in D[11]:
                    Template_Tweet += """
        <div class="picture-insert" align="center"> <img src="%s" class="tweet-image" ></div>""" % (
                        media
                    )
        elif type(D[11]) == str:
            frmt = D[11].replace("[", "").replace("]", "")
            frmt = frmt.split(",")
            if len(frmt) > 0:
                for media in frmt:
                    if media.startswith("'") and media.endswith("'"):
                        media = media[1:]
                        media = media[:-1]
                        Template_Tweet += """
        <div class="picture-insert" align="center"> <img src="%s" class="tweet-image" ></div>""" % (
                            media
                        )

        Template_Tweet += (
            """
        <div class="under-main-tweet">
            <div class="retweet%s"><form action="redqueen_retweet" method="POST"><input id="retweet%s" type="checkbox" name="rid" value="%s" onclick="submit()"><label class="btn" for="retweet%s"><i class="fas fa-retweet"></i> %s</label></form></div>"""
            % (nbr, nbr, D[1], nbr, D[10])
            + """
            <div class="like%s"><form action="redqueen_favorite" method="POST"><input id="like%s" type="checkbox" name="fid" value="%s" onclick="submit()"><label class="btn" for="like%s"><i class="far fa-heart"></i> %s</label></form></div>"""
            % (nbr, nbr, D[1], nbr, D[9])
            + """
        </div>
      </div>
    </div>"""
        )
        Tweets_Feed.append(Template_Tweet)
    return Tweets_Feed


def GenCss():

    css = ""
    for i in range(0, len(Extracted_Datas)):
        css += (
            ".comment"
            + str(i)
            + """ {
  color: #9eaab3;
  float: left;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}

.comment"""
            + str(i)
            + """:hover { 
    color: skyblue;
    float: left;
    margin-top: 12.5px;
    height: 25px;
    width: 25px;
}


#retweet"""
            + str(i)
            + """ {
    display: none;
}

.retweet"""
            + str(i)
            + """ {
  color: #9eaab3;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}

.retweet"""
            + str(i)
            + """:hover {
  color: green;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}


.retweet"""
            + str(i)
            + """:active{
  color: red;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}

#retweet"""
            + str(i)
            + """:checked + label {
  color: green;

}

#like"""
            + str(i)
            + """ {
    display: none;
}

.like"""
            + str(i)
            + """ {
  color: #9eaab3;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}

.like"""
            + str(i)
            + """:hover {
  color: red;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}

.like"""
            + str(i)
            + """:active{
  color: green;
  float: left;
  margin-left: 22%;
  margin-top: 12.5px;
  height: 25px;
  width: 25px;
}
#like"""
            + str(i)
            + """:checked + label {
  color: red;
}
"""
        )

        css += "\n"
    return css


def Pastbin(data):

    pb = Pastebin(PastebinApiKey.PBA)
    past = pb.create_paste(
        api_paste_code=str(data), api_paste_private=0, api_paste_expire_date="1H"
    )
    if past.startswith("http"):
        return past
    else:
        return ("Error:", past)


def Betterror(error_msg, def_name):
    try:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Err_to_log = (
            "!!\nFile: %s has encounter a %s error in %s() at line %s\nError Message:%s\n!!"
            % (fname, exc_type, def_name, exc_tb.tb_lineno, error_msg)
        )
        print(Err_to_log)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        Err_to_log = (
            "!!\nFile: %s has encounter a %s error in Betterror() at line %s\nError Message:%s\n!!"
            % (fname, exc_type, exc_tb.tb_lineno, e)
        )
        print(Err_to_log)

    time.sleep(Config.Time_Sleep)
    return Error_Log(Err_to_log)


def Error_Log(Err_to_log):

    try:

        with open(Pth_Error_Log, "a+") as fuck:
            fuck.write("\n"+str(CurrentDate) + "\n")
            fuck.write("\n"+Err_to_log + "\n")

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def WakeApiUp():
    global Twitter_Api
    global Api_Call_Nbr
    global Search_ApiCallLeft_Nbr
    try:
        Twitter_Api = Twython(TAK.oa2_app_key, access_token=TAK.oa2_access_token)
        rate = Twitter_Api.get_application_rate_limit_status()
        Search_ApiCallLeft_Nbr = int(
            rate["resources"]["search"]["/search/tweets"]["remaining"]
        )
        Api_Call_Nbr += 1
        return Twitter_Api
    except Exception as e:
        if GOGOGO_Trigger is False:
            sys.exit()
        Betterror(e, inspect.stack()[0][3])


def Cleanfile(filename):

    try:
        if os.path.isfile(filename) is False:
            print("==")
            print("File does not exist (%s)" % filename)
            print("Creating file")
            print("==")
            open(filename, "w")
            ret = []
        else:

            clean_lines = []
            with open(filename, "r") as f:
                lines = f.readlines()

                clean_lines = [l.strip() for l in lines if l.strip()]

            clean_lines = list(dict.fromkeys(clean_lines))
            with open(filename, "w") as f:
                f.writelines("\n".join(clean_lines))
            with open(filename, "r") as f:
                ret = f.read().splitlines()
        return ret

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])
        return []


def Fig(font, txt, toirc=None):
    try:
        setfont = Figlet(font=font)
        print(setfont.renderText(txt))
        if toirc:
            IrSend(txt, toirc)
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Load_Variables():

    global Keywords_List
    global Timelines_List
    global Following_List
    global Friends_List
    global Banned_Word_list
    global Banned_User_list
    global Requested_Cmd_List
    global Already_Searched_List
    global Extract_Tweet_Data
    global NoResult_List
    global Emoji_List
    global Ban_Double_List
    global Total_Already_Send_Nbr
    global Ban_Double_Url_List

    Checkfiles = [
        Pth_TotalApi_Call,
        Pth_Update_Call,
        Pth_Request_Log,
        Pth_Error_Log,
        Pth_Current_Session,
        Pth_Rq_Server_Save,
        Pth_Banned_Word_Rq,
        Pth_Tweets_Id_Rq,
        Pth_Banned_People_Rq,
        Pth_Keywords_Rq,
        Pth_Users_Timelines_Rq,
        Pth_Following_Rq,
        Pth_Friends_Rq,
        Pth_Already_Searched_Rq,
        Pth_Url_Sent_Rq,
        Pth_Text_Sent_Rq,
        Pth_NoResult_Rq,
        Pth_Rss_Rq,
    ]

    for cf in Checkfiles:
        if os.path.isfile(cf) is False:
            print("==")
            print("File does not exist (%s)" % cf)
            print("Creating file")
            print("==")
            open(cf, "w")

    try:
        Fig("cybermedium", "LoadVars()", True)
        print("\n\n\n\n")

        for saved in Cleanfile(Pth_NoResult_Rq):
            NoResult_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "No Result Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*\n")

        for saved in Cleanfile(Pth_Data + "RssSave"):
            RssSent.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Rss Sent Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")
        print("\n\n")

        for saved in Cleanfile(Pth_Keywords_Rq):
            Keywords_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Keywords Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*\n")
        print("\n\n")


        for saved in Cleanfile(Pth_Users_Timelines_Rq):
            Timelines_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Users Timelines Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*\n")
        print("\n\n")


        for saved in Cleanfile(Pth_Following_Rq):
            Following_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Following Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")
        print("\n\n")

        for saved in Cleanfile(Pth_Friends_Rq):
            Friends_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Friends Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        for saved in Cleanfile(Pth_Banned_Word_Rq):
            Banned_Word_list.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Banned Words Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        for saved in Cleanfile(Pth_Banned_People_Rq):
            Banned_User_list.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Banned users Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        for saved in Cleanfile(Pth_Rss_Rq):
            Rss_Url_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Rss Feeds Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")
        print("\n\n")

        for saved in Cleanfile(Pth_Request_Log):
            Requested_Cmd_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Request Cmd Log Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        for saved in Cleanfile(Pth_Already_Searched_Rq):
            Already_Searched_List.append(saved)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Already Searched Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        Fig("digital", "Loading Emoticon", True)

        for use_aliases, group in (
            (False, emoji.unicode_codes.EMOJI_UNICODE),
            (True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE),
        ):
            for name, ucode in list(group.items()):
                assert name.startswith(":") and name.endswith(":") and len(name) >= 3
                emj = emoji.emojize(name, use_aliases=use_aliases)
                Emoji_List.append(emj)
        print(Emoji_List)

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Emoji Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        with open(Pth_Rq_Server_Save, "r") as f:
            Tweet_Datas = csv.DictReader(f)

            for td in Tweet_Datas:
                Extracted_Datas.append(
                    (
                        td["Tweet_Origin_Link"],
                        td["Tweet_Id"],
                        td["Tweet_Timestamp"],
                        td["Tweet_Author"],
                        td["Tweet_Profile_Author"],
                        td["Tweet_Author_Link"],
                        td["Tweet_Text"],
                        td["Tweet_Rt_Author"],
                        td["Tweet_Rt_Author_Link"],
                        td["Tweet_Favorite_Counter"],
                        td["Tweet_Retweet_Counter"],
                        td["Tweet_Media"],
                        td["Tweet_Url"],
                    )
                )

        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Saved Server Tweets Loaded", True)
        print("*=*=*=*=*=*=*=*=*=*")

        for saved in Cleanfile(Pth_Text_Sent_Rq):
            if saved not in Ban_Double_List:
                Ban_Double_List.append(saved)
                Total_Already_Send_Nbr += 1

        for saved in Cleanfile(Pth_Url_Sent_Rq):
            if saved not in Ban_Double_Url_List:
                Ban_Double_Url_List.append(saved)



        print("*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "BanDouble Updated", True)
        print("*=*=*=*=*=*=*=*=*=*")



        Fig("digital", "Done")

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])

def Checkdouble(tweet,id,urls):
        banned = False
        tweet = re.sub(r'http\S+', '', tweet)

        for item in urls:
            if item in Ban_Double_Url_List:
                Fig(
                    "cybermedium",
                    "Link Already Sent :",
                   )
                print("Found Matched :", item)
                return(True)

        for item in Ban_Double_List:
            if len(item) >= Config.Minimum_Tweet_Length:
                pos = 0
                lng = len(item)
                half = int(lng/2)
                next = int(half) + pos
                sample = item[pos : int(half)]
                maxpos = pos + int(len(sample))

                while int(maxpos) < int(lng):
                    try:
                        if str(sample) in str(tweet) and str(sample) != " ":
                            Fig(
                                "cybermedium",
                                "Some parts are Identicals to a Previous Tweet :",
                            )
                            print("Found Matched :", sample)
                            Saveid(id)
                            maxpos = int(lng)
                            banned = True
                            Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
                            break
                        else:
                            pos = pos + 1
                            next = int(half) + pos
                            sample = item[pos : int(next)]
                            maxpos = pos + int(len(sample))
                    except Exception as e:
                        pos = pos + 1
                        next = int(half) + pos
                        sample = item[pos : int(next)]
                        maxpos = pos + int(len(sample))
                if banned is True:
                   break

        if banned is True:
           return(True)
        else:
           return(False)

def title():
    print(Config.Trinity)


def timer(mode):
    global timeleft
    global timed
    global Start_Date

    try:

        if mode == 2:
            now = ""
            timesup = ""
            timeleft = ""
            timed = ""

            now = datetime.datetime.now()
            timesup = now - Start_Date
            timeleft = "Time Left %i / %i" % (timesup.seconds, Time_To_Wait)
            timed = timesup.seconds

            return timeleft

        if mode == 1:

            now = ""
            timesup = ""
            timeleft = ""
            timed = ""

            now = datetime.datetime.now()
            timesup = now - Start_Date
            timed = timesup.seconds
            return timed
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Request(cmd):

    global Keywords_List
    global Timelines_List
    global Banned_Word_list
    global Banned_User_list
    global Api_Call_Nbr
    global Banned
    global MasterPause_Trigger
    global NoResult_List
    global MasterStart_Trigger
    global MasterStop_Trigger

    Fig("cybermedium", "#Request()")

    try:

        time.sleep(Config.Time_Sleep)

        adk = []
        delk = []
        bk = []
        adt = []
        delt = []
        bt = []
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

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("At %s ." % timestamp)

        log = "\n***\nNew request from allowed user:%s at: %s \n %s\n***" % (
            IrcKey.IRMASTER,
            timestamp,
            cmd,
        )
        output = []

        if cmd.count(",") > 0:
            print("You v send those commandes :")
        else:
            print("You v send this commande :")
        print(cmd)

        items = cmd.split(";")

        cmds = [
            "adduser:",
            "deluser:",
            "banuser:",
            "addtimeline:",
            "deltimeline:",
            "bantimeline:",
            "addkeyword:",
            "delkeyword:",
            "bankeyword:",
            "addfriend:",
            "delfriend:",
            "banfriend:",
            "addrss:",
            "delrss:",
            "!help",
            "!users",
            "!keywords",
            "!timeline",
            "!friends",
            "!rss",
            "!requests",
            "!Pth_NoResult_Rq",
            "!rmPth_NoResult_Rq",
            "!badkeys",
            "!badppl",
            "!start",
            "!stop",
            "!pause",
            "!quit",
        ]

        for sample in items:
            reconized = False
            for option in cmds:
                if sample.lower().startswith(option):
                    reconized = True
                    if option == "!help":
                        help = [
                            "adduser:@user1 @user2 [Add user1 and user2 to Following.Rq]",
                            "deluser:@user1 @user2 [Delete user1 and user2 in Following.Rq]",
                            "banuser:@user1 @user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from Keywords.Rq]",
                            "addfriend:@user1 @user2 [Add user1 and user2 to Friends.Rq]",
                            "delfriend:@user1 @user2 [Delete user1 and user2 in Friends.Rq]",
                            "banfriend:@user1 @user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from Friend.Rq]",
                            "addkeyword:Key word1,Key word2 [Add 'Key word1' and 'Key word2' to Keywords.Rq]",
                            "delkeyword:Key word1,Key word2 [Delete 'Key word1' and 'Key word2' in Keywords.Rq]",
                            "bankeyword:Key word1,Key word2 [Add Key word1 and Key word2 to Bannedword.Rq and remove it from Keywords.Rq]",
                            "addtimeline:@user1 @user2 [Add user1 and user2 timelines to Users.Timelines.Rq]",
                            "deltimeline:@user1 @user2 [Delete user1 and user2 timelines in Users.Timelines.Rq]",
                            "bantimeline:@user1 @user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from Users.Timelines.Rq]",
                            "addrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Add rss feeds to Rq.Rss]",
                            "delrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Delete rss feeds in Rq.Rss]",
                            "Commands starting with '!' can't be chained or have to be placed at the end of multiple cmd.",
                            "!help [Print this help]",
                            "!start [Launch Crawling.]",
                            "!stop [Stop Crawling.]",
                            "!pause [Start and Stop Pause mode]",
                            "!quit [Exit.]",
                            "!users [Print Following.Rq content]",
                            "!timeline [print User.Timeline.Rq]",
                            "!keywords [Print Keywords.Rq content]",
                            "!rss [Print Rss.Rq content]",
                            "!requests [Print Request.log content]",
                            "!Pth_NoResult_Rq [Print No.Result content]",
                            "!rmPth_NoResult_Rq [Remove No.Result content from Rq.Keywords]",
                            "!badkeys [Print Rq.Bannedword content]",
                            "!badppl [Print Rq.Bannedpeople content]",
                            "Example : deluser:@user1 @user2 ;addkeyword:key1,key two,key3;bankeyword:badkey1,bad key two;!rss",
                        ]
                        return help
                    if option == "!pause":
                        if MasterPause_Trigger is True:
                            MasterPause_Trigger = False
                            return "Pause mode is off."
                        else:
                            MasterPause_Trigger = True
                            return "Pause mode is on."
                    if option == "!start":
                        MasterStart_Trigger = True
                        if MasterStop_Trigger is True:
                            MasterStop_Trigger = False
                            return Redqueen()
                        return "Redqueen has started."
                    if option == "!stop":
                        MasterStart_Trigger = False
                        MasterStop_Trigger = True
                        return "Redqueen has stopped."
                    if option == "!quit":
                        MasterStart_Trigger = False
                        Irc.send(
                            bytes(
                                "PRIVMSG %s : Redqueen has been terminated. \r\n"
                                % (IrcKey.IRMASTER),
                                "UTF-8",
                            )
                        )
                        os.system("pkill -f Redqueen.py")
                    if option == "!badkeys":
                        return Pastbin(Banned_Word_list)
                    if option == "!badppl":
                        return Pastbin(Banned_User_list)
                    if option == "!users":
                        return Pastbin(Following_List)
                    if option == "!keywords":
                        return Pastbin(Keywords_List)
                    if option == "!timeline":
                        return Pastbin(Timelines_List)
                    if option == "!friends":
                        return Pastbin(Friends_List)
                    if option == "!rss":
                        return Pastbin(Rss_Url_List)
                    if option == "!requests":
                        return Pastbin(Requested_Cmd_List)
                    if option == "!Pth_NoResult_Rq":
                        return Pastbin(NoResult_List)

                    if option == "!rmPth_NoResult_Rq":
                        print("Removing No.results from Rq.Keywords..")
                        RmNores = True
##

                    if option == "bantimeline:":
                        if sample.count("@") == 1:
                            print("You asked to Ban this user timeline :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                bt.append(single)
                                delt.append(single)
                            else:
                                print("User timeline var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    bt.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                    delt.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User timeline var is empty.")
                            print("You asked to Ban those users timelines: ", ",".join(bt))
                        else:
                            print("No user timeline found '@' is missing")

                    if option == "addtimeline:":

                        if sample.count("@") == 1:
                            print("You asked to Add this user timeline:", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                adt.append(single)
                            else:
                                print("User timeline var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    adt.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User timeline var is empty.")
                            print("You asked to Add those users: ", ",".join(adt))
                        else:
                            print("No user timeline found '@' is missing")

                    if option == "deltimeline:":
                        if sample.count("@") == 1:
                            print("You asked to Delete this user timeline:", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                delt.append(single)
                            else:
                                print("User timeline var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    delt.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User timeline var is empty.")
                            print("You asked to Delete those users timelines: ", ",".join(delt))
                        else:
                            print("No user timeline found '@' is missing")

##
                    if option == "banuser:":
                        if sample.count("@") == 1:
                            print("You asked to Ban this user :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                bu.append(single)
                                delk.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    bu.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                    delk.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Ban those users: ", ",".join(bu))
                        else:
                            print("No user found '@' is missing")

                    if option == "adduser:":

                        if sample.count("@") == 1:
                            print("You asked to Add this user :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                adu.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    adu.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Add those users: ", ",".join(adu))
                        else:
                            print("No user found '@' is missing")

                    if option == "deluser:":
                        if sample.count("@") == 1:
                            print("You asked to Delete this user :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                delu.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    delu.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Delete those users: ", ",".join(delu))
                        else:
                            print("No user found '@' is missing")

                    if option == "banfriend:":
                        if sample.count("@") == 1:
                            print("You asked to Ban this friend :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                bf.append(single)
                                delk.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    bf.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                    delk.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Ban those friends: ", ",".join(bf))
                        else:
                            print("No user found '@' is missing")

                    if option == "delfriend:":
                        if sample.count("@") == 1:
                            print("You asked to Delete this friend :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                delf.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    delf.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Delete those friends: ", ",".join(delf))
                        else:
                            print("No user found '@' is missing")
                    if option == "addfriend:":

                        if sample.count("@") == 1:
                            print("You asked to Add this friend :", sample)
                            single = sample.replace(str(option), "").replace(" ", "")
                            if len(single) > 0:
                                adf.append(single)
                            else:
                                print("User var is empty.")
                        elif sample.count("@") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    adf.append(
                                        var.replace(str(option), "").replace(" ", "")
                                    )
                                else:
                                    print("User var is empty.")
                            print("You asked to Add those friends: ", ",".join(adf))
                        else:
                            print("No user found '@' is missing")
                    if option == "bankeyword:":
                        if sample.count(",") == 0:
                            print("You asked to Ban this keyword :", sample)
                            single = sample.replace(str(option), "")
                            if len(single) > 0:
                                bk.append(single)
                                delk.append(single)
                            else:
                                print("Keyword var is empty.")
                        elif sample.count(",") > 0:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    bk.append(var.replace(str(option), ""))
                                    delk.append(var.replace(str(option), ""))
                                else:
                                    print("Keyword var is empty.")
                            print("You asked to Ban those Keywords: ", ",".join(bk))
                    if option == "addkeyword:":
                        if sample.count(",") == 0:
                            print("You asked to Add this keyword :", sample)
                            single = sample.replace(str(option), "")
                            if len(single) > 0:
                                adk.append(single)
                            else:
                                print("Keyword var is empty.")
                        elif sample.count(",") > 0:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    adk.append(var.replace(str(option), ""))
                                else:
                                    print("Keyword var is empty.")
                            print("You asked to Add those Keywords: ", ",".join(adk))
                    if option == "delkeyword:":
                        if sample.count(",") == 0:
                            print("You asked to Delete this keyword :", sample)
                            single = sample.replace(str(option), "")
                            if len(single) > 0:
                                delk.append(single)
                            else:
                                print("Keyword var is empty.")
                        elif sample.count(",") > 0:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    delk.append(var.replace(str(option), ""))
                                else:
                                    print("Keyword var is empty.")
                            print("You asked to Add those Keywords: ", ",".join(delk))
                    if option == "delrss:":
                        if sample.count("http") == 1:
                            print("You asked to Delete this rss feed :", sample)
                            single = sample.replace(str(option), "")
                            if len(single) > 0:
                                delk.append(single)
                            else:
                                print("Rss var is empty.")
                        elif sample.count("http") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    delrss.append(var.replace(str(option), ""))
                                else:
                                    print("Rss var is empty.")
                            print(
                                "You asked to Delete those rss feeds: ",
                                ",".join(delrss),
                            )

                        else:
                            print("No rss found (flux must starts with http)")
                    if option == "addrss:":
                        if sample.count("http") == 1:
                            print("You asked to Add this rss feed :", sample)
                            single = sample.replace(str(option), "")
                            if len(single) > 0:
                                adrss.append(single)
                            else:
                                print("Keyword var is empty.")
                        elif sample.count("http") > 1:
                            for var in sample.split(","):
                                if len(var) > 0:
                                    adrss.append(var.replace(str(option), ""))
                                else:
                                    print("Keyword var is empty.")
                            print(
                                "You asked to Delete those rss feeds: ", ",".join(adrss)
                            )
                        else:
                            print("No rss found (flux must starts with http)")
            if reconized == False:
                with open(Pth_Data + "Request.log.Rq", "a") as file:
                    file.write("\n"+log + "\n")
                return "Cmd not recognised."

        with open(Pth_Data + "Request.log.Rq", "a") as f:
            f.write("\n"+log + "\n")

        if RmNores is True:
            ret = Flush_NoResult()
            output.append(ret)

#
        if len(adt) > 0:
            print("Adding new entry to Users.Timelines.Rq")
            with open(Pth_Users_Timelines_Rq, "a") as f:
                for entry in adt:
                    if entry not in Timelines_List:
                        f.write("\n"+str(entry) + "\n")

            output.append("**Adding %s entry in Users.Timelines.Rq**" % len(adt))

        if len(bt) > 0:
            print("Adding new entry to Bannedpeople.Rq")
            with open(Pth_Banned_People_Rq, "a") as f:
                for entry in bt:
                    if entry not in Banned_User_list:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Bannedpeople.Rq**" % len(bt))

        if len(delt) > 0:
            print("Deleting entry from Users.Timelines.Rq")
            lines = Cleanfile(Pth_Users_Timelines_Rq)
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            save_copy = (
                "cp "
                + str(Pth_Users_Timelines_Rq)
                + " "
                + str(Pth_Save)
                + "Users.Timelines.Rq"
                + str(ts)
                + ".save"
            )
            os.system(save_copy)
            with open(Pth_Users_Timelines_Rq, "w") as f:
                for line in lines:
                    for entry in delt:
                        if line.strip("\n") != entry:
                            f.write("\n"+line + "\n")
            output.append("**Deleting %s entry in Users.Timelines.Rq**" % len(delt))


#
        if len(adrss) > 0:
            print("Adding new entry to Rq.Rss")
            with open(Pth_Rss_Rq, "a") as f:
                for entry in adrss:
                    if entry not in Rss_Url_List:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Added %s new entry to Rq.Rss**" % len(adrss))

        if len(delrss) > 0:
            print("Deleting entry from Rq.Rss")
            lines = Cleanfile(Pth_Rss_Rq)
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            save_copy = (
                "cp "
                + str(Pth_Rss_Rq)
                + " "
                + str(Pth_Save)
                + "Rss.Feeds.Rq"
                + str(ts)
                + ".save"
            )
            os.system(save_copy)
            with open(Pth_Rss_Rq, "w") as f:
                for line in lines:
                    for entry in delrss:
                        if line.strip("\n") != entry:
                            f.write("\n"+line + "\n")
            output.append("**Deleting %s entry in Rq.Rss**" % len(delrss))

        if len(delf) > 0:
            print("Deleting entry from Rq.Friends")
            lines = Cleanfile(Pth_Friends_Rq)
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            save_copy = (
                "cp "
                + str(Pth_Friends_Rq)
                + " "
                + str(Pth_Save)
                + "Friends.Rq"
                + str(ts)
                + ".save"
            )
            os.system(save_copy)
            with open(Pth_Friends_Rq, "w") as f:
                for line in lines:
                    for entry in delf:
                        if line.strip("\n") != entry:
                            f.write("\n"+line + "\n")
            output.append("**Deleting %s entry in Rq.Friends**" % len(delf))

        if len(delu) > 0:
            print("Deleting entry from Rq.Following")
            lines = Cleanfile(Pth_Following_Rq)
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            save_copy = (
                "cp "
                + str(Pth_Following_Rq)
                + " "
                + str(Pth_Save)
                + "Following.Rq"
                + str(ts)
                + ".save"
            )
            os.system(save_copy)
            with open(Pth_Following_Rq, "w") as f:
                for line in lines:
                    for entry in delu:
                        if line.strip("\n") != entry:
                            f.write("\n"+line + "\n")
            output.append("**Deleting %s entry in Rq.Following**" % len(delu))

        if len(delk) > 0:
            print("Deleting entry from Rq.Keywords")
            lines = Cleanfile(Pth_Keywords_Rq)
            ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            save_copy = (
                "cp "
                + str(Pth_Keywords_Rq)
                + " "
                + str(Pth_Save)
                + "Keywords.Rq"
                + str(ts)
                + ".save"
            )
            os.system(save_copy)
            with open(Pth_Keywords_Rq, "w") as f:
                for line in lines:
                    for entry in delk:
                        if line.strip("\n") != entry:
                            f.write("\n"+line + "\n")
            output.append("**Deleting %s entry in Rq.Keywords**" % len(delk))

        if len(adk) > 0:
            print("Adding new entry to Rq.Keywords")
            with open(Pth_Keywords_Rq, "a") as f:
                for entry in adk:
                    if entry not in Keywords_List:
                        f.write("\n"+str(entry) + "\n")

            output.append("**Adding %s entry in Rq.Keywords**" % len(adk))

        if len(adu) > 0:
            print("Adding new entry to Rq.Following")
            with open(Pth_Following_Rq, "a") as f:
                for entry in adu:
                    if entry not in Following_List:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Rq.Following**" % len(adu))

        if len(adf) > 0:
            print("Adding new entry to Rq.Friends")
            with open(Pth_Friends_Rq, "a") as f:
                for entry in adf:
                    if entry not in Friends_List:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Rq.Friends**" % len(adf))

        if len(bu) > 0:
            print("Adding new entry to Rq.Bannedpeople")
            with open(Pth_Banned_People_Rq, "a") as f:
                for entry in bu:
                    if entry not in Banned_User_list:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Rq.Bannedpeople**" % len(bu))

        if len(bf) > 0:
            print("Adding new entry to Rq.Bannedpeople")
            with open(Pth_Banned_People_Rq, "a") as f:
                for entry in bf:
                    if entry not in Banned_User_list:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Rq.Bannedpeople**" % len(bf))

        if len(bk) > 0:
            print("Adding new entry to Rq.Bannedword")
            with open(Pth_Banned_Word_Rq, "a") as f:
                for entry in bk:
                    if entry not in Banned_Word_list:
                        f.write("\n"+str(entry) + "\n")
            output.append("**Adding %s entry in Rq.Bannedword**" % len(bk))
        output.append("**Done**")
        return output
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Flush_NoResult():
    global NoResult_List
    try:

        Fig("cybermedium", "NoResult()")
        print("Deleting No.Results content from Rq.Keywords")
        cnt = 0
        lines = Cleanfile(Pth_Keywords_Rq)
        ts = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        save_copy = (
            "cp "
            + str(Pth_Keywords_Rq)
            + " "
            + str(Pth_Save)
            + "Keywords.Rq"
            + str(ts)
            + ".Before_Removing_Noresults.save"
        )
        os.system(save_copy)
        with open(Pth_Keywords_Rq, "w") as f:
            for line in lines:
                for entry in NoResult_List:
                    if line.strip("\n") != entry:
                        f.write("\n"+line + "\n")
                    else:
                        print("Removed:", entry)
                        cnt += 1
        file = open(Pth_NoResult_Rq, "w")
        file.write("")
        file.close
        NoResult_List = []
        print(
            "**Removed No results from Rq.Keywords: %s/%s **"
            % (cnt, len(NoResult_List))
        )
        return "**Removed No results from Rq.Keywords: %s/%s **" % (
            cnt,
            len(NoResult_List),
        )
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])

def SaveDouble(text,urls):
    global Ban_Double_List
    global Ban_Double_Url_List

    try:

        Fig("cybermedium", "SaveDouble()")

        time.sleep(Config.Time_Sleep)
        with open(Pth_Url_Sent_Rq, "a") as file:
            UrlDouble = False
            for u in urls:
                if u not in Ban_Double_Url_List:
                    file.write("\n"+str(u)+"\n")
                    Ban_Double_Url_List.append(u)
                else:
                    UrlDouble = True
        if UrlDouble is False:
           print("*=*=*=*=*=*=*=*=*=*")
           print("SAVING URLS :", urls)
           Fig("digital", "Saved")
           print("*=*=*=*=*=*=*=*=*=*")
        else:
          print("*=*=*=*=*=*=*=*=*=*")
          print("Already Saved")
          print("*=*=*=*=*=*=*=*=*=*")
        text = text.replace("\n", "")
        if text not in Ban_Double_List:
            TxtDouble = False
            with open(Pth_Text_Sent_Rq, "a") as file:
                file.write("\n"+str(text) + "\n")

            Ban_Double_List.append(str(text))
            print("*=*=*=*=*=*=*=*=*=*")
            print("SAVING TWEET TO TMP :", text)
            Fig("digital", "Saved")
            print("*=*=*=*=*=*=*=*=*=*")
        else:
          TxtDouble = True
          print("*=*=*=*=*=*=*=*=*=*")
          print("Already Saved")
          print("*=*=*=*=*=*=*=*=*=*")
        time.sleep(Config.Time_Sleep)

        if UrlDouble is True or TxtDouble is True:
          return(True)
        else:
          return(False)

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])



def flushtmp():

    global Api_Call_Nbr
    global Update_Call_Nbr
    try:

        goflush = 0

        Fig("cybermedium", "flushtmp()", True)

        if os.path.exists(Pth_Current_Session):

            file = open(Pth_Current_Session, "r")
            datefile = file.read()
            date_object = datetime.datetime.strptime(
                str(datefile), "%Y-%m-%d %H:%M:%S.%f"
            )
            Laps = CurrentDate - date_object

            print(Laps)

            try:
                if (CurrentDate - date_object).total_seconds() > 86400:
                    goflush = 1
            except Exception as e:
                Betterror(e, inspect.stack()[0][3])

                Fig("digital", "No need to flush", True)

            if goflush == 1:

                print("==")
                Fig("digital", "Flushing Temps Files", True)
                print("==")
                file.close()
                try:
                    text = "New Pth_Current_Session ! " + str(CurrentDate)
                    IrSend(text)
                    print("")
                    Fig("digital", "Status sent !")

                except Exception as e:
                    Betterror(e, inspect.stack()[0][3])
                    time.sleep(Config.Time_Sleep)

                os.remove(Pth_Current_Session)

                if os.path.exists(Pth_TotalApi_Call):
                    os.remove(Pth_TotalApi_Call)

                if os.path.exists(Pth_Update_Call):
                    os.remove(Pth_Update_Call)

                if os.path.exists(Pth_Already_Searched_Rq):
                    os.remove(Pth_Already_Searched_Rq)

                print("==")
                Fig("digital", "Saving current date", True)
                print(CurrentDate)
                print("==")

                file = open(Pth_Current_Session, "w")
                file.write(str(CurrentDate))
                file.close()

                Fig("digital", "Done Flushing", True)

            else:
                lfts = 86400 - Laps.seconds

                print("==")
                Fig("digital", "No need to flush", True)
                Fig("digital", "Starting from Last Pth_Current_Session", True)

                print("Numbers of seconds since the first api call :", Laps.seconds)
                print("%i Seconds left until Twitter flushs Api_Call_Nbrs :" % lfts)
                print("==")

        else:

            print("==")
            Fig("digital", "New Pth_Current_Session Started", True)
            print(CurrentDate)
            print("==")

            file = open(Pth_Current_Session, "w")
            file.write(str(CurrentDate))
            file.close()
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Last_Session(lastsearch):

    global Menu_Check_Trigger
    try:
        if Menu_Check_Trigger == False:
            Fig("cybermedium", "Last_Session()", True)

            with open(Pth_Already_Searched_Rq, "a") as file:
                for words in lastsearch:
                    file.write("\n"+words + "\n")
                    Fig("digital", "Marking " + words + " as old . ")

            Menu_Check_Trigger = True
        else:
            print("==")
            Fig("digital", "Saved already")
            print("==")
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def SaveTotalCall(call, update):
    try:
        Fig("cybermedium", "SaveTotalCall()")
        global Total_Call_Nbr
        global Update_Call_Nbr
        global Total_Update_Call_Nbr

        try:
            lastitem = Cleanfile(Pth_TotalApi_Call)[0]
        except Exception as e:
            Betterror(e, inspect.stack()[0][3])
            lastitem = 0
        print("==")
        print("Last Total saved : ", lastitem)
        Total_Call_Nbr = int(lastitem) + int(call)
        Fig("digital", "Saving new Total : " + str(Total_Call_Nbr))
        print("==")
        with open(Pth_TotalApi_Call, "w") as file:
            file.write(str(Total_Call_Nbr))

        try:
            lastitem = Cleanfile(Pth_Update_Call)[0]
        except Exception as e:
            Betterror(e, inspect.stack()[0][3])
            lastitem = 0
        print("==")
        print("Last Update Total saved : ", lastitem)
        Total_Call_Nbr = int(lastitem) + int(call)
        print("Saving new Update Total : ", Total_Call_Nbr)
        print("==")
        with open(Pth_Update_Call, "w") as file:
            file.write(str(Total_Call_Nbr))
        Fig("digital", "Done Saving Calls")

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def IrSweet():
    global GOGOGO_Trigger
    global Irc
    global Broken_pipe_Trigger
    global MasterPause_Trigger

    Konnected = False
    Identified = False
    Joined = False
    IrcSocket = False
    Irc = ""
    Buffer = ""

    while IrcSocket == False:
        try:
            Fig("digital", "\n--Connecting to :" + str(IrcKey.IRHOST) + "--\n")
            time.sleep(Config.Time_Sleep)
            Irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Irc.connect((IrcKey.IRHOST, IrcKey.IRPORT))

            Irc.send(bytes("NICK %s\r\n" % IrcKey.IRNICK, "UTF-8"))
            Irc.send(
                bytes(
                    "USER %s %s woot :%s\r\n"
                    % (IrcKey.IRIDENT, IrcKey.IRHOST, IrcKey.IRREALNAME),
                    "UTF-8",
                )
            )
            time.sleep(Config.Time_Sleep)
            IrcSocket = True
            if Broken_pipe_Trigger is True:
                Broken_pipe_Trigger = False
                MasterPause_Trigger = False
        except Exception as e:
            Betterror(e, inspect.stack()[0][3])
            if "Broken pipe" in str(e):
                 Broken_pipe_Trigger = True
                 MasterPause_Trigger = True
                 time.sleep(60)
            continue

    last_ping = time.time()
    threshold = 3 * 60

    while IrcSocket == True:
        try:
            Buffer = Irc.recv(1024).decode("UTF-8", errors="ignore")

            if len(Buffer) > 1:
                print("Buffer: ", Buffer)

            if IrcKey.IRMASTERTrigger in Buffer and "PRIVMSG BlueKing :" in Buffer:
                cmd = Buffer.split("PRIVMSG BlueKing :")[1]
                Answer = Request(cmd[:-2])
                if len(Answer) > 0:
                    if type(Answer) == list:
                        for l in Answer:
                            time.sleep(Config.Time_Sleep)
                            print("\n--Sending :%s --\n" % l)
                            Irc.send(
                                bytes(
                                    "PRIVMSG %s : < %s > \r\n" % (IrcKey.IRMASTER, l),
                                    "UTF-8",
                                )
                            )
                    else:
                        print("\n--Sending :%s --\n" % Answer)
                        Irc.send(
                            bytes(
                                "PRIVMSG %s : < %s > \r\n" % (IrcKey.IRMASTER, Answer),
                                "UTF-8",
                            )
                        )

            if Buffer.find("PING") != -1:
                Fig("digital", "\n--PINGED--\n")
                try:
                    tmp = Buffer.split("PING :")[1]
                except Exception as e:
                    Betterror(e, inspect.stack()[0][3])
                    tmp = "placeholder"

                Irc.send(bytes("PONG :" + tmp + "\r\n", "UTF-8"))
                Fig("digital", "\n--PONG :" + str(tmp) + " --\n")
                last_ping = time.time()

            if Buffer.find("ERROR :Closing Link:") != -1:
                Fig("digital", "\n--TimeOut--\n\n--Restablishing Connection--\n")
                return IrSweet()

            if Buffer.find(IrcKey.IRKonTrigger) != -1 and Konnected is False:
                Konnected = True
                Fig("digital", "\n--Connected--\n")

            if Buffer.find(IrcKey.IRIdentTrigger) != -1 and Identified is False:
                Identified = True
                Fig("digital", "\n--Authentified--\n")

            if Identified == False and Konnected is True:
                time.sleep(Config.Time_Sleep)
                Fig("digital", "\n--Sending CREDENTIAL--\n")
                Irc.send(
                    bytes(
                        "%sIDENTIFY %s\r\n" % (IrcKey.IRNICKSERV, IrcKey.IRPASS),
                        "UTF-8",
                    )
                )
                time.sleep(Config.Time_Sleep)

            if Joined == False and Identified == True and Konnected == True:
                print("\n--Joining " + str(IrcKey.IRCHANNEL) + "--\n")
                Irc.send(
                    bytes(
                        "JOIN %s %s\r\n" % (IrcKey.IRCHANNEL, IrcKey.IRCHANPASS),
                        "UTF-8",
                    )
                )
                time.sleep(Config.Time_Sleep)
                Irc.send(
                    bytes(
                        "PRIVMSG %s :<Knock Knock Neo ...>\r\n" % IrcKey.IRCHANNEL,
                        "UTF-8",
                    )
                )
                time.sleep(Config.Time_Sleep)
                Irc.send(
                    bytes(
                        "PRIVMSG %s :<The Matrix Has You.>\r\n" % IrcKey.IRCHANNEL,
                        "UTF-8",
                    )
                )
                time.sleep(Config.Time_Sleep)
                Irc.send(
                    bytes(
                        "PRIVMSG %s :<Follow The White Rabbit.>\r\n" % IrcKey.IRCHANNEL,
                        "UTF-8",
                    )
                )
                time.sleep(Config.Time_Sleep)
                Fig("digital", "\n--Joined--\n")
                Joined = True
            if (time.time() - last_ping) > threshold:
                Fig("digital", "\n--TimeOut--\n\n--Restablishing Connection--\n")
                return IrSweet()

            if Joined is True and Identified is True and Konnected is True:
                GOGOGO_Trigger = True

        except Exception as e:
            Betterror(e, inspect.stack()[0][3])


def RssFeeds(ttl):
    global RssSent
    global Extracted_Datas

    try:

        counter = 0

        for flux in Rss_Url_List:
            if counter <= ttl:
                try:
                    rss = feedparser.parse(flux)

                    for news in rss.entries:
                        time.sleep(Config.Time_Sleep)
                        counter = counter + 1
                        format = str(news.title) + " : " + str(news.link)
                        if format not in RssSent:
                            RssSent.append(format)
                            IrSend(format)
                            if Config.WEB_SERVER is True:
                                Rss_tuple = (
                                    news.link,
                                    "rss",
                                    str(datetime.datetime.now()),
                                    flux,
                                    "img/redqueen-profile.png",
                                    news.link,
                                    news.title,
                                    "",
                                    "",
                                    "9999",
                                    "9999",
                                    "",
                                    news.link,
                                )
                                Extracted_Datas.append(Rss_tuple)
                            with open(Pth_Data + "RssSave", "a") as f:
                                f.write("\n"+str(format) + "\n")
                except Exception as e:
                    Betterror(e, inspect.stack()[0][3])
                    time.sleep(Config.Time_Sleep)
                    counter = counter + 1
                    print("Rss Error %s : %s" % (flux, e))
                    IrSend("Rss Error " + str(flux) + " : " + str(e))
            else:
                return
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def IrSend(content, dontprint=None):
    global Irc
    global Broken_pipe_Trigger
    global MasterPause_Trigger

    if Config.IRC_CONNECT is False:
        return ()
    try:

        Fig("cybermedium", "IrSend()")

        if not dontprint:
            print("==")
            Fig("cybermedium", "Tweet Loaded!")
            print("==")
            Irc.send(
                bytes(
                    "PRIVMSG %s :==============================================================\r\n"
                    % IrcKey.IRCHANNEL,
                    "UTF-8",
                )
            )
        content = content.replace("\n", " ")
        time.sleep(Config.Time_Sleep)
        Fig("digital", "\n--Sending :" + str(content) + "--\n")
        Irc.send(
            bytes("PRIVMSG %s :** %s **\r\n" % (IrcKey.IRCHANNEL, content), "UTF-8")
        )
        Fig("digital", "\n--Done--\n")
        if Broken_pipe_Trigger is True:
                Broken_pipe_Trigger = False
                MasterPause_Trigger = False

        return
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])
        if "Broken pipe" in str(e):
            Broken_pipe_Trigger = True
            MasterPause_Trigger = True
            time.sleep(60)

def Stat2Irc(Time_To_Wait):

    try:

        #  Flood = randint(0,3)
        #  if Flood == 3:
        Api_Call_Nbrtxt = "Total RT Sent: " + str(Total_Sent_Nbr)
        IrSend(Api_Call_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Update_Call_Nbrtxt = "Current Update Calls: " + str(Update_Call_Nbr)
        IrSend(Update_Call_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Call_Nbrtxt = "Total Calls: " + str(Total_Call_Nbr)
        IrSend(Total_Call_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Update_Call_Nbrtxt = "Total Update Calls: " + str(Total_Update_Call_Nbr)
        IrSend(Total_Update_Call_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Banned_User_listtxt = "Banned Users in list: " + str(len(Banned_User_list))
        IrSend(Banned_User_listtxt)
        time.sleep(Config.Time_Sleep)
        Ban_Double_Listtxt = "Total Banned (Double): " + str(Total_Already_Send_Nbr)
        IrSend(Ban_Double_Listtxt)
        time.sleep(Config.Time_Sleep)
        Banned_Word_listtxt = "Banned Words in list: " + str(len(Banned_Word_list))
        IrSend(Banned_Word_listtxt)
        time.sleep(Config.Time_Sleep)
        Friendstxt = "Nbr of friends: " + str(len(Friends_List))
        IrSend(Friendstxt)
        time.sleep(Config.Time_Sleep)
        Followingtxt = "Users Followed: " + str(len(Following_List))
        IrSend(Followingtxt)
        time.sleep(Config.Time_Sleep)
        Keywordstxt = "Keywords in list: " + str(len(Keywords_List))
        IrSend(Keywordstxt)
        time.sleep(Config.Time_Sleep)
        Timelinestxt = "Timelines in list: " + str(len(Timelines_List))
        IrSend(Timelinestxt)
        time.sleep(Config.Time_Sleep)
        AvgScoreTxt = "Current Tweets collected: " + str(len(AvgScore))
        IrSend(AvgScoreTxt)
        time.sleep(Config.Time_Sleep)
        NbrRetweettxt = "Tweets sent:" + str(len(Retweet_List))
        IrSend(NbrRetweettxt)
        time.sleep(Config.Time_Sleep)
        Totale_Score_Nbrtxt = "Total Banned (Score): " + str(Totale_Score_Nbr)
        IrSend(Totale_Score_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_Lang_Nbrtxt = "Total Banned (Language): " + str(
            Total_Ban_By_Lang_Nbr
        )
        IrSend(Total_Ban_By_Lang_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_Date_Nbrtxt = "Total Banned (Too old): " + str(
            Total_Ban_By_Date_Nbr
        )
        IrSend(Total_Ban_By_Date_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_NoResult_Nbrtxt = "Total Banned (No Keywords): " + str(
            Total_Ban_By_NoResult_Nbr
        )
        IrSend(Total_Ban_By_NoResult_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_Keywords_Nbrtxt = "Total Banned (Words): " + str(
            Total_Ban_By_Keywords_Nbr
        )
        IrSend(Total_Ban_By_Keywords_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_FollowFriday_Nbrtxt = "Total Banned (FF): " + str(
            Total_Ban_By_FollowFriday_Nbr
        )
        IrSend(Total_Ban_By_FollowFriday_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_TooManyHashtags_Nbrtxt = "Total Banned (###):" + str(
            Total_Ban_By_TooManyHashtags_Nbr
        )
        IrSend(Total_Ban_By_TooManyHashtags_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        Total_Ban_By_BannedPeople_Nbrtxt = "Total Banned Users: " + str(
            Total_Ban_By_BannedPeople_Nbr
        )
        IrSend(Total_Ban_By_BannedPeople_Nbrtxt)
        time.sleep(Config.Time_Sleep)
        RssFeeds(Time_To_Wait)
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def limits():
    try:

        Fig("cybermedium", "Limits()")
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
            Fig("cybermedium", "CURRENT LIMITS ARE REACHED !!")
            print("")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")

            Fig("digital", "Login Out")
            Fig("digital", "Waiting 60 minutes")
            print("\n\n\n\n")

            Stat2Irc(3600)
            Update_Call_Nbr = 0
            Api_Call_Nbr = 0
            Search_Limit_Trigger = False
            RestABit_Trigger = False
            Wait_Hour_Trigger = False

            Fig("digital", "Waking up ..")
            print("")
            Twitter_Api = WakeApiUp()
            print("\n\n")

        if RestABit_Trigger == True:
            print("****************************************")
            print("****************************************")
            Fig("cybermedium", "Mysterious Error !!!", True)
            print("")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")

            Fig("digital", "Login Out")
            Fig("digital", "Waiting 5 minutes")
            Stat2Irc(3600)

            Update_Call_Nbr = 0
            Api_Call_Nbr = 0
            Search_Limit_Trigger = False
            RestABit_Trigger = False

            Fig("digital", "Waking up ..")
            print("")
            Twitter_Api = WakeApiUp()

        if Search_Limit_Trigger == True:

            # Request()
            print("****************************************")
            print("****************************************")

            Fig("cybermedium", "SEARCH LIMITS ALMOST REACHED")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")

            Fig("digital", "Login Out")

            Fig("digital", "Waiting 15 minutes")
            Stat2Irc(900)

            Update_Call_Nbr = 0
            Api_Call_Nbr = 0
            Search_Limit_Trigger = False

            Fig("digital", "Waking up ..")
            print("")
            Twitter_Api = WakeApiUp()
            print("****************************************")
            print("****************************************\n\n\n\n")

        if Api_Call_Nbr >= Config.Maximum_Api_Search_Call_By_15_Minutes:

            # Request()
            print("****************************************")
            print("****************************************")

            Fig("cybermedium", "CURRENT LIMITS ALMOST REACHED")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")

            Fig("digital", "Login Out")

            if Wait_Half_Hour_Trigger != 1:
                Fig("digital", "Waiting 15 minutes")

                Stat2Irc(900)
            else:
                Fig("digital", "Waiting 30 minutes")
                Stat2Irc(1800)

            Update_Call_Nbr = 0
            Api_Call_Nbr = 0
            Fig("digital", "Waking up ..")
            print("")
            Twitter_Api = WakeApiUp()
            print("****************************************")
            print("****************************************\n\n\n\n")

        if Total_Call_Nbr > Config.Maximum_Api_Search_Call_By_Day:

            # Request()
            print("****************************************")
            print("****************************************")

            Fig("cybermedium", "CURRENT LIMITS ALMOST REACHED (total)")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")
            All_Ok_Trigger = True
            Skip_Wait_Trigger = True

        if Total_Update_Call_Nbr > Config.Maximum_Api_Search_Update_Call_By_Day:
            # Request()

            print("****************************************")
            print("****************************************")
            Fig("cybermedium", "CURRENT LIMITS ALMOST REACHED (update)")
            Fig("digital", "Saving Total Calls to file")
            SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)
            Fig("digital", "Resetting current Api_Call_Nbrs")
            All_Ok_Trigger = True

        print("===================")
        Fig("digital", "Ok")
        print("===================")
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])

def IsKnown(coop):
   if "@" + str(coop) in Following_List:
       print("##")
       print("This tweet is from a known user:",coop)
       print("##")
       return(True)
   if "@" + str(coop) in Friends_List:
       print("##")
       print("This tweet is from a known friend:",coop)
       print("##")
       return(True)
   return(False)

def Ban(twitem):

    global Total_Ban_By_NoResult_Nbr
    global Total_Ban_By_Keywords_Nbr
    global Total_Already_Send_Nbr
    global Total_Ban_By_FollowFriday_Nbr
    global Total_Ban_By_TooManyHashtags_Nbr
    global Total_Ban_By_BannedPeople_Nbr
    global Total_Ban_By_Lang_Nbr
    global Total_Ban_By_Date_Nbr

    Fig("cybermedium", "Ban()")

    try:

        if "retweeted_status" in twitem:

            Tweet_Id = str(twitem["retweeted_status"]["id"])
            Tweet_Timestamp = twitem["retweeted_status"]["created_at"]
            Tweet_Author = twitem["retweeted_status"]["user"]["screen_name"]
            Tweet_Author_Bio = twitem["retweeted_status"]["user"]["description"]
            Tweet_Rt_Author = twitem["user"]["screen_name"]
            Tweet_Follower_Count = twitem["user"]["followers_count"]
            Tweet_Favorite_Counter = twitem["retweeted_status"]["favorite_count"]
            Tweet_Retweet_Counter = twitem["retweeted_status"]["retweet_count"]
        else:
            Tweet_Id = str(twitem["id"])
            Tweet_Timestamp = twitem["created_at"]
            Tweet_Author = twitem["user"]["screen_name"]
            Tweet_Author_Bio = twitem["user"]["description"]
            Tweet_Rt_Author = ""
            Tweet_Follower_Count = twitem["user"]["followers_count"]
            Tweet_Favorite_Counter = twitem["favorite_count"]
            Tweet_Retweet_Counter = twitem["retweet_count"]

        Tweet_Origin_Link = ("https://twitter.com/" + str(twitem["user"]["screen_name"]) + "/status/" + str(twitem["id"]))

        Tweet_Urls = []
        Tweet_Urls.append(Tweet_Origin_Link)

        if "urls" in twitem["entities"]:
           for url in twitem["entities"]["urls"]:
               Tweet_Urls.append(url["expanded_url"])
        if "retweeted_status" in twitem:
           if "urls" in twitem["retweeted_status"]["entities"]:
               for url in twitem["retweeted_status"]["entities"]["urls"]:
                     Tweet_Urls.append(url["expanded_url"])

        if twitem["lang"] not in Config.Allowed_Tweet_Lang:

                Saveid(Tweet_Id)
                Total_Ban_By_Lang_Nbr += 1
                time.sleep(Config.Time_Sleep)
                Fig("digital", "This tweet is written in a language not allowed")
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")


        if Idlist(Tweet_Id) is True:
                Total_Already_Send_Nbr += 1
                time.sleep(Config.Time_Sleep)
                Fig("digital", "This tweet has been already sent.")
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

        if Tweet_Retweet_Counter < Config.Minimum_Tweet_Retweet:
                    Fig("digital", "NOT ENOUGH RETWEET")
                    Fig("digital", "Going To Trash")
                    print("*=*=*=*=*=*=*=*=*=*")
                    time.sleep(Config.Time_Sleep)
                    return(True)

        if Tweet_Retweet_Counter > Config.Maximum_Tweet_Retweet:
            if "retweeted_status" in twitem:
                    if IsKnown(Tweet_Rt_Author) is False:
                        Fig("digital", "Too many retweets and not from a friend or follower")
                        Fig("digital", "Going To Trash")
                        print("*=*=*=*=*=*=*=*=*=*")
                        return(True)
            if IsKnown(Tweet_Author) is False:
                        Fig("digital", "Too many retweets and not from a friend or follower")
                        Fig("digital", "Going To Trash")
                        print("*=*=*=*=*=*=*=*=*=*")
                        return(True)
        if Tweet_Favorite_Counter  > Config.Maximum_Tweet_Fav:
            if "retweeted_status" in twitem:
                    if IsKnown(Tweet_Rt_Author) is False:
                        Fig("digital", "Too many fav and not from a friend or follower")
                        Fig("digital", "Going To Trash")
                        print("*=*=*=*=*=*=*=*=*=*")
                        return(True)
            if IsKnown(Tweet_Author) is False:
                        Fig("digital", "Not enough followers")
                        Fig("digital", "Going To Trash")
                        print("*=*=*=*=*=*=*=*=*=*")
                        return(True)


        if Tweet_Follower_Count < Config.Minimum_User_Following:
             if IsKnown(Tweet_Author) is False:
                        Fig("digital", "Too many fav and not from a friend or follower")
                        Fig("digital", "Going To Trash")
                        print("*=*=*=*=*=*=*=*=*=*")
                        return(True)


        Tweet_Timestamp = Tweet_Timestamp.replace(" +0000 ", " ")
        Timeformat = datetime.datetime.strptime(Tweet_Timestamp, "%a %b %d %H:%M:%S %Y").strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        Timestrip = datetime.datetime.strptime(Timeformat, "%Y-%m-%d %H:%M:%S")
        Tweet_Age = datetime.datetime.now() - Timestrip


        if "retweeted_status" in twitem:

            if Tweet_Age.days >= Config.Maximum_Retweet_DayOld:
                Fig("digital", "This tweet is too Old.")
                print("This tweet was send at : ", Tweet_Age)
                Saveid(Tweet_Id)
                Total_Ban_By_Date_Nbr += 1
                time.sleep(Config.Time_Sleep)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

        else:
            if Tweet_Age.days >= Config.Maximum_Tweet_DayOld:
                Fig("digital", "This retweet is too Old.")
                print("This tweet was send at : ", Tweet_Age)
                Saveid(Tweet_Id)
                Total_Ban_By_Date_Nbr += 1
                time.sleep(Config.Time_Sleep)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

        if "full_text" in twitem:
            Tweet_Txt = twitem["full_text"]
        else:
            Tweet_Txt = twitem["text"]


        if len(Tweet_Txt) < Config.Minimum_Tweet_Length:
            Fig("digital", "NOT ENOUGH TEXT")
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)


        UShallPass = 0
        Twist = re.sub(r"[^A-Za-z0-9 ]+", "", Tweet_Txt.lower())
        Tweet_Author_Bio = re.sub(r"[^A-Za-z0-9 ]+", "", Tweet_Author_Bio.lower())

        print("*=*=*=*=*=*=*=*=*=*")

        if Tweet_Txt in Ban_Double_List:
            Fig("digital", "This tweet is Identical to a Previous tweet :")
            Saveid(Tweet_Id)
            Total_Already_Send_Nbr = Total_Already_Send_Nbr + 1
            time.sleep(Config.Time_Sleep)
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)

        Banned = Checkdouble(Tweet_Txt,Tweet_Id,Tweet_Urls)

        if Banned is False:

            for item in Emoji_List:
                emotst = Tweet_Txt.count(item)
                if emotst > Config.Maximum_Tweet_Emoticon:
                    print("Found those emoji : ", item)
                    Fig(
                        "cybermedium",
                        "This tweet contains an Emoticon and must die for some reason. ",
                    )
                    return(True)
        else:

            print("Tweet: ", Tweet_Txt)
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)



        if Banned is False:
            for mustbe in Keywords_List:
                mustbe = re.sub(r"[^A-Za-z0-9 ]+", "", mustbe.lower())
                if mustbe in Twist:
                    Fig("digital", "Found Keywords :")
                    print("Sample : ", mustbe)
                    Fig("digital", "You shall Pass")
                    print("*=*=*=*=*=*=*=*=*=*")
                    UShallPass += 1

            if UShallPass < Config.Minimum_Keywords_In_Tweet:

                Fig("digital", "Did not found any Keyword in Tweet_Txt.")
                Total_Ban_By_NoResult_Nbr = Total_Ban_By_NoResult_Nbr + 1
                print("Tweet: ", Tweet_Txt)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)
            print("*=*=*=*=*=*=*=*=*=*")

        for forbid in Banned_Word_list:
            forbid = re.sub(r"[^A-Za-z0-9 ]+", "", forbid.lower())
            if forbid in Twist:
                Fig("digital", "This tweet contains banned words :")
                print("** %s **" % str(forbid))
                Total_Ban_By_Keywords_Nbr = Total_Ban_By_Keywords_Nbr + 1
                time.sleep(Config.Time_Sleep)
                print("Tweet: ", Tweet_Txt)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

            if forbid in Tweet_Author_Bio:
                Fig("digital", "This user profile contains banned words :")
                print(Tweet_Author_Bio)
                print("** %s **" % str(forbid))
                Total_Ban_By_Keywords_Nbr = Total_Ban_By_Keywords_Nbr + 1
                time.sleep(Config.Time_Sleep)
                print("Tweet: ", Tweet_Txt)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

        for forbid in Banned_User_list:
            if str(forbid.lower()) in str(Tweet_Author.lower()):

                Fig("digital", "This tweet is from a banned user :")
                print("** %s **" % forbid)
                Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
                time.sleep(Config.Time_Sleep)
                print("Tweet: ", Tweet_Txt)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)

        if len(Tweet_Rt_Author) > 0:
            for forbid in Banned_User_list:
                if str(forbid.lower()) in str(Tweet_Rt_Author.lower()):

                    Fig("digital", "This retweet is from a banned user :")
                    print("** %s **" % forbid)
                    Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
                    time.sleep(Config.Time_Sleep)
                    print("Tweet: ", Tweet_Txt)
                    Fig("digital", "Going To Trash")
                    print("*=*=*=*=*=*=*=*=*=*")
                    return(True)

        if Tweet_Txt.count("@") >= Config.Maximum_Mention_In_Tweet:
            Fig("digital", "Follow Friday")
            Total_Ban_By_FollowFriday_Nbr = Total_Ban_By_FollowFriday_Nbr + 1
            time.sleep(Config.Time_Sleep)
            print("Tweet: ", Tweet_Txt)
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)

        if Tweet_Txt.count("#") >= Config.Maximum_Hashtag_In_Tweet:

            Fig("digital", "HashTags Fever")
            Total_Ban_By_TooManyHashtags_Nbr = Total_Ban_By_TooManyHashtags_Nbr + 1
            time.sleep(Config.Time_Sleep)
            print("Tweet: ", Tweet_Txt)
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)

        if Tweets_By_Same_User.count(str(Tweet_Author)) >= Config.Maximum_Tweet_By_User:
            Fig("digital", "Too many Tweets From this user ")
            Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
            time.sleep(Config.Time_Sleep)
            print("Tweet: ", Tweet_Txt)
            Fig("digital", "Going To Trash")
            print("*=*=*=*=*=*=*=*=*=*")
            return(True)
#        else:
#            print("Nbr of tweets for this user : ", Tweets_By_Same_User.count(Tweet_Author))
#            print("*=*=*=*=*=*=*=*=*=*")
#            time.sleep(Config.Time_Sleep)

        if len(Tweet_Rt_Author) > 0:
            if Tweets_By_Same_User.count(str(Tweet_Rt_Author)) >= Config.Maximum_Tweet_By_User:
                Fig("digital", "Too many Tweets From this user ")
                Total_Ban_By_BannedPeople_Nbr = Total_Ban_By_BannedPeople_Nbr + 1
                time.sleep(Config.Time_Sleep)
                print("Tweet: ", Tweet_Txt)
                Fig("digital", "Going To Trash")
                print("*=*=*=*=*=*=*=*=*=*")
                return(True)
#            else:
#                print("Nbr of tweets for this user : ", Tweets_By_Same_User.count(Tweet_Rt_Author))
#                print("*=*=*=*=*=*=*=*=*=*")
#                time.sleep(Config.Time_Sleep)


        Fig("digital", "Good To Go !!")
        print("*=*=*=*=*=*=*=*=*=*")
        time.sleep(Config.Time_Sleep)
        return(False)
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Saveid(id):
    try:
        Fig("cybermedium", "Saveid()")
        time.sleep(Config.Time_Sleep)

        with open(Pth_Tweets_Id_Rq, "a") as file:
            file.write("\n"+ str(id) + "\n")
        print("*=*=*=*=*=*=*=*=*=*")
        print("Id :", id)
        Fig("digital", "Saved")
        print("*=*=*=*=*=*=*=*=*=*")
        time.sleep(Config.Time_Sleep)
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Idlist(id):
    global Banned
    global Total_Sent_Nbr
    global Id_Done_Trigger
    try:
        Fig("cybermedium", "Idlist()")
        time.sleep(Config.Time_Sleep)

        if Id_Done_Trigger == False:

            Total_Sent_Nbr = sum(1 for line in open(Pth_Tweets_Id_Rq))
            Id_Done_Trigger = True

        for saved in Cleanfile(Pth_Tweets_Id_Rq):

            if saved != "\n" or saved != "":
                if str(saved) in str(id):

                    print("*=*=*=*=*=*=*=*=*=*")
                    print("Id from file :", saved)
                    print("tweet id :", id)
                    print("*=*=*=*=*=*=*=*=*=*")
                    Banned = True
                    time.sleep(Config.Time_Sleep)
                    return True

        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        Fig("digital", "Unknown Tweet ID")
        print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
        return False
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Scoring(tweet, search):

    global Api_Call_Nbr
    global Total_Call_Nbr
    global Update_Call_Nbr
    global Total_Update_Call_Nbr
    global AvgScore
    global Tweet_Age
    global Totale_Score_Nbr
    global RestABit_Trigger
    global ERRORCNT
    global Wait_Hour_Trigger
    global Wait_Half_Hour_Trigger
    global RetweetSave
    try:

        if "retweeted_status" in tweet:

            Tweet_Timestamp = tweet["retweeted_status"]["created_at"]
        else:
            Tweet_Timestamp = tweet["created_at"]
        now = datetime.datetime.now()
        TwtTime = Tweet_Timestamp
        TwtTime = TwtTime.replace(" +0000 ", " ")
        Timed = datetime.datetime.strptime(TwtTime, "%a %b %d %H:%M:%S %Y").strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        TimeFinal = datetime.datetime.strptime(Timed, "%Y-%m-%d %H:%M:%S")
        Tweet_Age = now - TimeFinal

        Score = 0
        LuckyLuke = randint(0, Config.Luck_Factor)

        Fig("cybermedium", "Scoring()")

        if "full_text" in tweet:
            Tweext = tweet["full_text"]
        else:
            Tweext = tweet["text"]

        print(
            "*************************************************************************************"
        )
        Fig("digital", "Starting Scoring function")
        print("")


        if "retweet_count" in tweet:

                print("##")
                print(
                    "This tweet has been retweeted %i times " % tweet["retweet_count"]
                )
                print("##")

                if tweet["retweet_count"] >= 1 and tweet["retweet_count"] <= 23:
                    Score = Score + int(tweet["retweet_count"])
                    if tweet["retweet_count"] > 23 and tweet["retweet_count"] <= 30:
                        Score = Score + 23 + 3
                    if tweet["retweet_count"] > 30 and tweet["retweet_count"] <= 40:
                        Score = Score + 23 + 4
                    if tweet["retweet_count"] > 40 and tweet["retweet_count"] <= 50:
                        Score = Score + 23 + 5
                    if tweet["retweet_count"] > 50 and tweet["retweet_count"] <= 50:
                        Score = Score + 23 + 6
                    if tweet["retweet_count"] > 60 and tweet["retweet_count"] <= 70:
                        Score = Score + 23 + 7
                    if tweet["retweet_count"] > 70 and tweet["retweet_count"] <= 80:
                        Score = Score + 23 + 8
                    if tweet["retweet_count"] > 80 and tweet["retweet_count"] <= 90:
                        Score = Score + 23 + 9
                    if tweet["retweet_count"] > 90 and tweet["retweet_count"] <= 100:
                        Score = Score + 23 + 10
                    if tweet["retweet_count"] > 100 and tweet["retweet_count"] <= 110:
                        Score = Score + 23 + 11
                    if tweet["retweet_count"] > 110 and tweet["retweet_count"] <= 120:
                        Score = Score + 23 + 12
                    if tweet["retweet_count"] > 120 and tweet["retweet_count"] <= 130:
                        Score = Score + 23 + 13
                    if tweet["retweet_count"] > 130 and tweet["retweet_count"] <= 140:
                        Score = Score + 23 + 14
                    if tweet["retweet_count"] > 140 and tweet["retweet_count"] <= 150:
                        Score = Score + 23 + 15
                    if tweet["retweet_count"] > 150 and tweet["retweet_count"] <= 160:
                        Score = Score + 23 + 16
                    if tweet["retweet_count"] > 160 and tweet["retweet_count"] <= 170:
                        Score = Score + 23 + 17
                    if tweet["retweet_count"] > 170 and tweet["retweet_count"] <= 180:
                        Score = Score + 23 + 18
                    if tweet["retweet_count"] > 180 and tweet["retweet_count"] <= 190:
                        Score = Score + 23 + 19
                    if tweet["retweet_count"] > 190 and tweet["retweet_count"] <= 200:
                        Score = Score + 23 + 20
                    if tweet["retweet_count"] > 200 and tweet["retweet_count"] <= 210:
                        Score = Score + 23 + 21
                    if tweet["retweet_count"] > 210 and tweet["retweet_count"] <= 223:
                        Score = Score + 23 + 23

        if "entities" in tweet:
            nogo = 0
            if (
                    "urls" in tweet["entities"]
                    and len(tweet["entities"]["urls"]) > Config.Minimum_Link_In_Tweet
                ):
                    print("##")
                    print(
                        "This tweet contains a link : ",
                        tweet["entities"]["urls"][-1]["expanded_url"],
                    )
                    print("##")
                    Score = Score + 3
                    if (
                        "hashtags" in tweet["entities"]
                        and len(tweet["entities"]["hashtags"])
                        > Config.Minimum_Link_In_Tweet
                    ):
                        print("##")
                        print(
                            "This tweet contains Hashtag : ",
                            tweet["entities"]["hashtags"][-1]["text"],
                        )
                        print("##")
                        Score = Score + 1

                    if (
                        "media" in tweet["entities"]
                        and len(tweet["entities"]["media"])
                        > Config.Minimum_Media_In_Tweet
                    ):
                        print("##")
                        print(
                            "This tweet contains Media : ",
                            tweet["entities"]["media"][-1]["media_url"],
                        )
                        print("##")
                        Score = Score + 3

                    if tweet["favorite_count"] > Config.Minimum_Tweet_Fav:

                        print("##")
                        print("This tweet has been fav : ", tweet["favorite_count"])
                        print("##")
                        Score = Score + 1
                        fav = tweet["favorite_count"]
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

            if (
                    "followers_count" in tweet["user"]
                    and tweet["user"]["followers_count"] > Config.Minimum_User_Following
                ):
                    print("##")
                    print("Source followers count : ", tweet["user"]["followers_count"])
                    print("##")

                    if tweet["user"]["followers_count"] > Config.Minimum_User_Friend:
                        Score = Score + 2
                    if (
                        tweet["user"]["followers_count"] > 400
                        and tweet["user"]["followers_count"] < 500
                    ):
                        Score = Score + 4
                    if (
                        tweet["user"]["followers_count"] > 500
                        and tweet["user"]["followers_count"] < 600
                    ):
                        Score = Score + 5
                    if (
                        tweet["user"]["followers_count"] > 600
                        and tweet["user"]["followers_count"] < 700
                    ):
                        Score = Score + 6
                    if (
                        tweet["user"]["followers_count"] > 700
                        and tweet["user"]["followers_count"] < 800
                    ):
                        Score = Score + 7
                    if (
                        tweet["user"]["followers_count"] > 800
                        and tweet["user"]["followers_count"] < 900
                    ):
                        Score = Score + 8
                    if (
                        tweet["user"]["followers_count"] > 900
                        and tweet["user"]["followers_count"] < 1000
                    ):
                        Score = Score + 9
                    if (
                        tweet["user"]["followers_count"] > 1000
                        and tweet["user"]["followers_count"] < 1500
                    ):
                        Score = Score + 10
                    if (
                        tweet["user"]["followers_count"] > 1500
                        and tweet["user"]["followers_count"] < 2000
                    ):
                        Score = Score + 11
                    if (
                        tweet["user"]["followers_count"] > 2000
                        and tweet["user"]["followers_count"] < 2500
                    ):
                        Score = Score + 12
                    if (
                        tweet["user"]["followers_count"] > 2500
                        and tweet["user"]["followers_count"] < 3000
                    ):
                        Score = Score + 13
                    if (
                        tweet["user"]["followers_count"] > 3000
                        and tweet["user"]["followers_count"] < 3500
                    ):
                        Score = Score + 14
                    if (
                        tweet["user"]["followers_count"] > 3500
                        and tweet["user"]["followers_count"] < 4000
                    ):
                        Score = Score + 15
                    if (
                        tweet["user"]["followers_count"] > 4000
                        and tweet["user"]["followers_count"] < 4500
                    ):
                        Score = Score + 16
                    if (
                        tweet["user"]["followers_count"] > 4500
                        and tweet["user"]["followers_count"] < 5000
                    ):
                        Score = Score + 17
                    if (
                        tweet["user"]["followers_count"] > 5000
                        and tweet["user"]["followers_count"] < 6000
                    ):
                        Score = Score + 18
                    if (
                        tweet["user"]["followers_count"] > 6000
                        and tweet["user"]["followers_count"] < 7000
                    ):
                        Score = Score + 19
                    if (
                        tweet["user"]["followers_count"] > 7000
                        and tweet["user"]["followers_count"] < 8000
                    ):
                        Score = Score + 20
                    if (
                        tweet["user"]["followers_count"] > 8000
                        and tweet["user"]["followers_count"] < 9000
                    ):
                        Score = Score + 21
                    if (
                        tweet["user"]["followers_count"] > 9000
                        and tweet["user"]["followers_count"] < 10000
                    ):
                        Score = Score + 22
                    if tweet["user"]["followers_count"] > 10000:
                        Score = Score + 23

            if (
                    "user_mentions" in tweet["entities"]
                    and len(tweet["entities"]["user_mentions"])
                    > Config.Minimum_Tweet_Mention
                ):
                    print("##")
                    print(
                        "This tweet is mentioning someone : ",
                        tweet["entities"]["user_mentions"][-1]["screen_name"],
                    )
                    print("##")

                    Score = Score + 1

            if (
                    "verified" in tweet["entities"]
                    and len(tweet["entities"]["verified"]) == "True"
                ):
                    print("##")
                    print(
                        "This tweet has been sent by a verified user : ",
                        tweet["entities"]["verified"],
                    )
                    print("##")
                    Score = Score + 5

            if "screen_name" in tweet["user"]:
                    coop = tweet["user"]["screen_name"]
                    if IsKnown(coop) is True:
                       Score = Score + 5

            if Tweet_Age.seconds < 3600:
                Score = Score + 23
                print("Less than an hour ago .")
                print("Score = + 23")
                print("Score = ", Score)

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
                print("Score = ", Score)

            if Tweet_Age.seconds > 43200 and Tweet_Age.seconds <= 46800:
                print("Twelve hours ago .")
                Score = Score + 11
                print("Score = + 11")
                print("Score = ", Score)

            if Tweet_Age.seconds > 46800 and Tweet_Age.seconds <= 50400:
                Score = Score + 10
                print("Thirteen hours ago .")
                print("Score = + 10")
                print("Score = ", Score)

            if Tweet_Age.seconds > 50400 and Tweet_Age.seconds <= 54000:
                Score = Score + 9
                print("Fourteen hours ago .")
                print("Score = + 9")

            if Tweet_Age.seconds > 54000 and Tweet_Age.seconds <= 57600:
                Score = Score + 8
                print("Fiveteen hours ago .")
                print("Score = + 8")
                print("Score = ", Score)

            if Tweet_Age.seconds > 57600 and Tweet_Age.seconds <= 61200:
                Score = Score + 7
                print("Sixteen hours ago .")
                print("Score = + 7")
                print("Score = ", Score)

            if Tweet_Age.seconds > 61200 and Tweet_Age.seconds <= 64800:
                Score = Score + 6
                print("Seventeen hours ago .")
                print("Score = + 6")
                print("Score = ", Score)

            if Tweet_Age.seconds > 64800 and Tweet_Age.seconds <= 68400:
                Score = Score + 5
                print("Eighteen hours ago .")
                print("Score = + 5")
                print("Score = ", Score)

            if Tweet_Age.seconds > 68400 and Tweet_Age.seconds <= 72000:
                Score = Score + 4
                print("Nineteen hours ago .")
                print("Score = + 4")
                print("Score = ", Score)

            if Tweet_Age.seconds > 72000 and Tweet_Age.seconds <= 75600:
                Score = Score + 3
                print("twenty hours ago .")
                print("Score = + 3")
                print("Score = ", Score)

            if Tweet_Age.seconds > 75600 and Tweet_Age.seconds <= 79200:
                Score = Score + 2
                print("Twenty one hours ago .")
                print("Score = + 2")
                print("Score = ", Score)

            if Tweet_Age.seconds > 79200 and Tweet_Age.seconds <= 82800:
                Score = Score + 1
                print("Twenty two hours ago .")
                print("Score = + 1")
                print("Score = ", Score)

            if Tweet_Age.seconds > 82800 and Tweet_Age.seconds < 86400:
                print("Twenty three hours ago .")
                Score = Score + 0
                print("Score = + 0")
                print("Score = ", Score)

        AvgScore.append(Score)

        Tweet_Urls = []
        Tweet_Origin_Link = ("https://twitter.com/" + str(tweet["user"]["screen_name"]) + "/status/" + str(tweet["id"]))
        Tweet_Urls.append(Tweet_Origin_Link)

        if "urls" in tweet["entities"]:
            for url in tweet["entities"]["urls"]:
                Tweet_Urls.append(url["expanded_url"])
        if "media" in tweet["entities"]:
            for media in tweet["entities"]["media"]:
                Tweet_Urls.append(media["media_url"])
        if "retweeted_status" in tweet:
            if "urls" in tweet["retweeted_status"]["entities"]:
               for url in tweet["retweeted_status"]["entities"]["urls"]:
                   Tweet_Urls.append(url["expanded_url"])
            if "media" in tweet["retweeted_status"]["entities"]:
               for media in tweet["retweeted_status"]["entities"]["media"]:
                   Tweet_Urls.append(media["media_url"])

        if Tweext.startswith("RT"):
               origtweet = Tweext.find(":")
               twxt = Tweext[Tweext.find(":")+2:] 
               LastCheck = SaveDouble(twxt,Tweet_Urls)
        else:
               LastCheck = SaveDouble(Tweext,Tweet_Urls)

        if Score >= Config.Minimum_Tweet_Score and LastCheck is False:
                        Tweext = Tweext.replace("\n", " ")
                        print("######################################")
                        print("Adding to Retweet List")
                        print("Nbr of tweets sent :", len(Retweet_List))
                        print("Tweet Score : ", Score)
                        print("Tweet ID :", tweet["id"])
                        print("Current ApiCall Count :", Api_Call_Nbr)
                        print("Total Number Of Calls :", Total_Call_Nbr)
                        print("Current Update Status Count :", Update_Call_Nbr)
                        print("Total Number Of Update Calls :", Total_Update_Call_Nbr)
                        print("Search Call left :", search)
                        print("Tweet :", Tweext)
                        print("######################################")
                        print("")

                        time.sleep(Config.Time_Sleep)
                        Retweet_List.append(tweet)
                        Tweets_By_Same_User.append(tweet["user"]["screen_name"])
                        if "retweeted_status" in tweet:
                            Tweets_By_Same_User.append(tweet["retweeted_status"]["user"]["screen_name"])

                        clickme = (
                            "https://twitter.com/"
                            + str(tweet["user"]["screen_name"])
                            + "/status/"
                            + str(tweet["id"])
                        )
                        Format_To_Irc = "From:%s %s -> %s Hype:%s Date:%s" % (
                            tweet["user"]["screen_name"],
                            Tweext,
                            clickme,
                            Score,
                            TwtTime,
                        )
                        IrSend(Format_To_Irc)
                        time.sleep(Config.Time_Sleep)
                        if Config.WEB_SERVER is True:
                            Extract_Tweet_Data(tweet)

        else:
                        print("")
                        Fig("cybermedium", "But ..")
                        print(
                            "================================================================================"
                        )
                        figy = "Score = %i" % Score
                        Fig("digital", str(figy))
                        print(
                            "================================================================================"
                        )
                        print("Score = ", Score)
                        print(
                            "================================================================================"
                        )
                        print(Tweext)
                        print(
                            "================================================================================"
                        )
                        print(
                            ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :("
                        )
                        if LastCheck is False:
                            print(
                            "This tweet does not match the requirement to be retweeted. (Score)"
                            )
                        else:
                            print(
                            "This tweet does not match the requirement to be retweeted. (Already Sent)"
                            )
                        print(
                            ":( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :( :("
                        )
                        print(
                            "================================================================================"
                        )
                        print("")
                        Totale_Score_Nbr = Totale_Score_Nbr + 1
                        time.sleep(Config.Time_Sleep)

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


def Search_Keyword(word):
    global Api_Call_Nbr
    global Update_Call_Nbr
    global Twitter_Api
    global RestABit_Trigger
    global Search_Done_Trigger
    global Search_Limit_Trigger
    global Search_ApiCallLeft_Nbr
    try:

        Fig("cybermedium", "Searching()")
        time.sleep(Config.Time_Sleep)
        ratechk = 0

        if Search_Done_Trigger == False:

            try:
                Twitter_Api = WakeApiUp()
                ratechk = 1

            except Exception as e:
                Betterror(e, inspect.stack()[0][3])
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
                Fig("digital", "Starting search function")
                print("**")
                print("##########################################")

                print("=/\/\/\/\/\/\/\/\/\/\/\=")
                Fig("digital", "Calling Limit function")
                print("=/\/\/\/\/\/\/\/\/\/\/\=")

                limits()

                try:
                    print("==")
                    print("Loading tweets for " + word)
                    print("")

                    Twitter_Api = WakeApiUp()
                    if word.startswith("@"):
                        searchresults = Twitter_Api.get_user_timeline(screen_name=str(word).replace("@",""), count=100, tweet_mode="extended")
                        Search_nbr = len(searchresults)
                        Search_obj = searchresults
                    else:
                        searchresults = Twitter_Api.search(q=word, tweet_mode="extended", count=100)
                        Search_nbr = len(searchresults["statuses"])
                        Search_obj = searchresults["statuses"]

                    print("##########################################")

                    Fig("cybermedium", "%s Results Found !" % Search_nbr)
                    # print(searchresults)
                    # time.sleep(10)
                    print("##########################################")

                    Api_Call_Nbr = Api_Call_Nbr + 1
                    Search_ApiCallLeft_Nbr = Search_ApiCallLeft_Nbr - 1
                    time.sleep(Config.Time_Sleep)

                except Exception as e:
                    if "Twitter API returned a 404 (Not Found)" in str(e):
                        with open(Pth_NoResult_Rq, "a") as file:
                            file.write("\n"+str(word) + "\n")
                    if "Twitter API returned a 401 (Unauthorized)" in str(e):
                        with open(Pth_NoResult_Rq, "a") as file:
                            file.write("\n"+str(word) + "\n")
                    searchresults = []
                    Search_nbr = 0
                    Search_obj = []
                    Betterror(e, inspect.stack()[0][3])
                    Api_Call_Nbr = Api_Call_Nbr + 1
                try:
                    if Search_nbr > Config.Minimum_Search_Result:
                        for item in Search_obj:
                            time.sleep(Config.Time_Sleep)
                            if MasterPause_Trigger is False:
                                try:
                                   txt = "Loading tweets for " + str(word)
                                   Fig("digital", txt)
                                except Exception as e:
                                   Betterror(e, inspect.stack()[0][3])
                                if Ban(item) is False:
                                   Scoring(item, Search_ApiCallLeft_Nbr)
                            else:
                                while True:
                                    time.sleep(Config.Time_Sleep)
                                    if MasterPause_Trigger is False:
                                        break
                                if Ban(item) is False:
                                   Scoring(item, Search_ApiCallLeft_Nbr)

                    else:
                        print("****************************************")

                        Fig("digital", "No Result")

                        print("****************************************")
                        Fig("digital", "Saving unwanted search to no.result")
                        time.sleep(Config.Time_Sleep)
                        with open(Pth_NoResult_Rq, "a") as file:
                            file.write("\n"+str(word) + "\n")

                except Exception as e:
                    Betterror(e, inspect.stack()[0][3])

            else:

                Search_Limit_Trigger = True
                Search_Done_Trigger = False
                limits()
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


# Some Code
def RedQueen():

    global Keywords_List
    global Timelines_List
    global MasterPause_Trigger
    global MasterStart_Trigger
    try:

        while 1:
            if GOGOGO_Trigger == True:
                break

        Fig("digital", "GOGOGO!", True)
        time.sleep(Config.Time_Sleep)

        Load_Variables()
        time.sleep(Config.Time_Sleep)

        Fig("digital", "Calling Flush function", True)

        flushtmp()

        Fig("digital", "Calling Search function", True)

        time.sleep(Config.Time_Sleep)

        Fig("digital", "Removing Keywords and Users Timelines from No.Result.Rq", True)

        Keywords_List = [k for k in Keywords_List if k not in NoResult_List]
        Timelines_List = [t for t in Timelines_List if t not in NoResult_List]

        Fig("digital", "Removing Keywords and Users Timelines from Already_Searched_List", True)

        Keywords_List = [k for k in Keywords_List if k not in Already_Searched_List]
        Timelines_List = [t for t in Timelines_List if t not in Already_Searched_List]

        shuffle(Keywords_List)
        shuffle(Timelines_List)

        Minwords = int( (len(Keywords_List) + len(Timelines_List)) / 20)
        Maxwords = int( (len(Keywords_List) + len(Timelines_List)) / 10)
        rndwords = randint(Minwords, Maxwords)
        if rndwords < 100:
            rndwords = len(Keywords_List)

        TODAYS_MENU = Keywords_List + Timelines_List
        shuffle(TODAYS_MENU)
        TODAYS_MENU = TODAYS_MENU[:rndwords]

        print("**")
        Fig("cybermedium", "Today's Menu :")

        print(Keywords_List[:rndwords])
        
        print("Total search terms : ", rndwords)

        print("**")

        try:
            status = (
                "Redqueen started at "
                + str(CurrentDate)
                + " Searching "
                + str(rndwords)
                + " items ."
            )
            IrSend(status)
            print("")
            Fig("digital", 'Status sent !"')

        except Exception as e:
            Betterror(e, inspect.stack()[0][3])
        time.sleep(Config.Time_Sleep)

        Fig("digital", "Check Last Menu started", True)

        tmpcnt = 0
        if Config.IRC_CONNECT is True:
            if MasterStart_Trigger is False:
                print("**Waiting for !start command from Irc.**")
                IrSend("Idle mode..")
            else:
                IrSend("Redqueen is starting..")
        else:
            MasterStart_Trigger = True

        while True:
            time.sleep(Config.Time_Sleep)
            if MasterStart_Trigger is True:
                figy = "Starting Redqueen"
                Fig("digital", figy)
                break
        for key in TODAYS_MENU:
            time.sleep(Config.Time_Sleep)
            if MasterPause_Trigger is False and MasterStart_Trigger is True:
                if MasterStop_Trigger is True:
                    MasterStart_Trigger == False
                    return IrSend("Redqueen has been stopped")
                tmpcnt = tmpcnt + 1
                figy = "Searching : %s %i/%i" % (key, tmpcnt, rndwords)
                Fig("digital", figy)
                time.sleep(Config.Time_Sleep)
                Search_Keyword(key)
            else:
                while True:
                    time.sleep(Config.Time_Sleep)
                    if MasterStop_Trigger is True:
                        MasterStart_Trigger == False
                        return IrSend("Redqueen has been stopped")
                    if MasterPause_Trigger is False and MasterStart_Trigger is True:
                        break
                tmpcnt = tmpcnt + 1
                figy = "Searching : %s %i/%i" % (key, tmpcnt, rndwords)
                Fig("digital", figy)
                time.sleep(Config.Time_Sleep)
                Search_Keyword(key)

        Fig("digital", "All Done !", True)

        time.sleep(Config.Time_Sleep)

        Fig("digital", "Calling Save Search Terms Function", True)

        time.sleep(Config.Time_Sleep)
        Last_Session(TODAYS_MENU)

        if (len(AvgScore)) != 0:
            avgscore = sum(AvgScore) / float(len(AvgScore))
        else:
            avgscore = 0
        try:
            dbrief = (
                "*Redqueen Debrief* -Searchs: "
                + str(rndwords)
                + "-Twts:"
                + str(len(AvgScore))
                + "-Avg Score:"
                + str(avgscore)
                + "-Rtwts:"
                + str(RetweetSave)
                + "-Tcall:"
                + str(Total_Call_Nbr)
                + "-Ucall:"
                + str(Total_Update_Call_Nbr)
            )

            IrSend(dbrief)

            Fig("digital", "Status sent !")

        except Exception as e:
            Betterror(e, inspect.stack()[0][3])
            time.sleep(Config.Time_Sleep)

        Fig("digital", "Calling Saving call function", True)

        SaveTotalCall(Api_Call_Nbr, Update_Call_Nbr)

        print(
            "##############################################################################################################"
        )
        print(
            "##############################################################################################################"
        )
        Fig("digital", "The End")
        print(
            "##############################################################################################################"
        )
        print(
            "##############################################################################################################"
        )
        MasterPause_Trigger = True
    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


if __name__ == "__main__":

    try:
        title()

        if Config.WEB_SERVER is True:
            for lenchk in [
                len(TAK.oa1_app_key),
                len(TAK.oa1_app_secret),
                len(TAK.oa1_oauth_token),
                len(TAK.oa1_oauth_token_secret),
            ]:
                if lenchk < 25:
                    print(
                        "All TAK.OAUT_1 keys must be filled and correct in TwitterApiKeys.py"
                    )
                    sys.exit()

        for lenchk in [len(TAK.oa2_app_key), len(TAK.oa2_access_token)]:
            if lenchk < 25:
                print("ALL TAK.OAUT_2 must be filled and correct in TwitterApiKeys.py")
                sys.exit()

        WakeApiUp()

        Fig("digital", "Launching Blueking on IRC")
        time.sleep(Config.Time_Sleep)

        Fig("cybermedium", "IrSweet()")
        Fig("digital", "Waiting for idle mode")
        time.sleep(Config.Time_Sleep)

        if Config.IRC_CONNECT is True:
            Thread(target=IrSweet).start()

        Thread(target=RedQueen).start()

        if Config.WEB_SERVER is True:
            while 1:
                time.sleep(1)
                if GOGOGO_Trigger == True:
                    break
            cherrypy.quickstart(Redqueen_Server(), "/", Cherryconf)

    except Exception as e:
        Betterror(e, inspect.stack()[0][3])


#################################################TheEnd#############################################################
