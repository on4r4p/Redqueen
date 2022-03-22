                                                  ,╓▄▄▄▄▄▄▄╓,
                                          ╓▄████████████████████████▄▄▄,
                                    ,▄▄█████████████████████████████████▄
                               ,▄▄████████████████████████████████████████▄
                            ,▄█████████████████████████████████████████████▌
                          ▄██████████████████████████████████████████████████▄
                       ,▄█████████████████████████████████████████████████████▌
                     ▄██████████████████████████████████████████████████████████▄
                   ▄█████████████████████████████████████████████████████████████⌐
                  ████████████████████████████████████████████████████████████████
                 █████████████████████████████████████████████▀▀▀█████████████████▌
                ║████████████████████████████████████████▀"       `╙▀██████████████
                ███████████████████████████████████████▀`            `▀████████████▌
               ║██████████████████████████████████████▌`               ╙███████████⌐
               ███████████████████████████████▓╫▓███▓▓"                 ╙█████████▌
             ,███████████████████████████████████▓▀╨`.                   "████████
            ╓█████████████████████████████████████████▄*          ,     , ▓██████⌐
           ╓███████████████████████████████████▄▓▀▓████░         ▄██████████████▌
           ▐████████████████████████████████████████████▀▀¥▄▄#Φ████▓▓▌██████████
            ████████████████████████████████████████████▌    ▄█████████████████M
            █████████████████████████▓▀▀███▓▓▓▓▓▓▓▓▓▓▓█▀     ╙█████████████████
            ║███████████████████████▌"   ╙▀▓▓▓▓▓▓▓▓▓▓▀        ╙▓▓▓▓▓▓▓▓▓██████▌
            ▐██████████████████████Ñ`        `╙'''             `▀▓▓▓▓▓▓▓██████
             █████████████████████▀                               '╙""╙ ║████▌
             █████████████████████                                     ╓█████
             ████████████████████▌                                    ╓█████▌
             ████████████████████⌐                 ╔╗▄▄╦  ,╓,       ╔╬█▓██▀█
             ████████████████████                  `╣▓▓▓▓▓▓▓▌`    ╔╣▓▓▓██▀ ║
            ▐████████████████████╫                  "╣▓▓▓▓▓▓▓w,╔╬▓▓▓▓▓██▌
            █████████████████████▓▌                  `╬▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▀
           ▐█████▀███████████████▓▓▓⌂          ,╓╗Φ╩▀▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█^
           ███▀└   ▀█████████████▓▓▓▓▄,            ,╗▄▄▄▄▄▓█▓▓▓▓▓▓▀
          ▐▀-        ▀█████████▓█▓▓▓▓▓▓▓µ        ╦╣▓▓▓▓▓▓▓▓▓▓▓▓█▀
                      `████████▓▓▓▓▓▓▓▓█▓▓╦      `╙▀▀▀╫▓▓▓▓▓▓█╨
                        ▀████▓█▓▓▓▓▓█▓▓▓▓▓▓▓╗,        ╫▓▓▓▓▓▓
                          ▀████████▓▓▓▓▓▓▓▓▓▓▓▓╗,. .╓╗▓▓▓▓▓▓▌
                          ║█ ╟████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▄
                          █▌ ╫████████████████████████████████▌
                         ╓█▌,▓████████████████▓████████████████
                       ,4████████████████████▓▓████████████████
                     `      └▀▀██████████████▓████████▓███████▌,
                                █████████████▓████████▓████████▓▓▓▄,
                               ║█████████████████████████████████▓▓▓▓▓▄,
                               ███████████████████████████████████▓▓▓▓▓▓▓▓▄,
                              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀╙╙╙╙╙"╙""╙^


## Redqueen

Search twitter for infoSec news made in ~2010 Still working somehow..

-Post results in Irc and create a twitter clone server to fav and retweet results- 

![](https://i.ibb.co/264n4TS/Screenshot-from-2022-02-23-01-40-27.png)

## Description

-It tries to sort all tweets from worst to best tweets by giving them a score 
depending on their content.

-Check if there is enough text,if Follow Friday or if there are too many hashstags

-Check if tweet is from a verifed account or from a friend or follower 

-Prevent retweeting the same info twice 

-Do not post the same user more than X times

-Do not post if retweet count is not at least X

-Do not post if retweet count or Fav more than X 

-Do not post if older than X days

-Saves item already searched 

-Do not post if the user is not followed by at least X ppl

-Behave may change if the tweet is from a friend or follower or with LuckFactor

-Such quote Th3j3st3r , MAny Replace his name by Th3Bouf0n , Very Hack, Much Wow

-Removes keywords which returns no result from the search list

-Provide some statistics about the current session during api resting time

-It does respect the limit of twitter api by saving the total nbr of calls and then
behave depending on how many call are left to be send (reset calls every 24 hours)etc ...


Then send a shot debrief when done posting all the good stuff in its timeline .
Some cmds can be send via private message in Irc : /msg botname !help


## Installation

pip3 install feedparser==6.0.8

pip3 install CherryPy==18.6.1

pip3 install pyfiglet==0.8.post1

pip3 install pbwrap==1.3.1

pip3 install emoji==0.5.0

pip3 install twython==3.3.0

pip3 install dateparser==1.1.0

pip3 uninstall regex

pip3 install regex==2022.1.18


Need: Twitter OA1/OA2 with read/write access


Edit:TwitterApiKeys.py,PastebinApiKey.py,IrcKey.py and Config.py

Fill:Data/Bannedpeople.Rq ,Bannedword.Rq ,Following.Rq ,Friends.Rq ,To.Search.Rq,Keywords.Rq etc..

Then Run the beast .


##Cmd Irc:
> ######*can be used without irc*
`< Commands starting with '!' can't be chained or must be placed at the end.>
< !help [Print this help] >
< !start [Launch Crawling.] >
< !stop [Stop Crawling.] >
< !pause [Start and Stop Pause mode] >
< !quit [Exit.] >
< !users [Print Following.Rq content] >
< !tosearch [print User.Timeline.Rq] >
< !searchs [print Current Search List] >
< !keywords [Print Keywords.Rq content] >
< !rss [Print Rss.Rq content] >
< !requests [Print Request.log content] >
< !badresult [Print No.Result content] >
< !flushrequest [Clear Request.log content] >
< !flushserver [Clear Results from Cherrypy server] >
< !flushbadresult [Remove No.Result content from Keywords.Rq] >
< !badkeys [Print Bannedword.Rq content] >
< !badppl [Print Bannedpeople.Rq content] >
< adduser:@user1,@user2 [Add user1 and user2 to Following.Rq] >
< deluser:@user1,@user2 [Delete user1 and user2 in Following.Rq] >
< banuser:@user1,@user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from Keywords.Rq] >
< addfriend:@user1,@user2 [Add user1 and user2 to Friends.Rq] >
< delfriend:@user1,@user2 [Delete user1 and user2 in Friends.Rq] >
< banfriend:@user1,@user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from Friend.Rq] >
< addkeyword:Key,word1,Key word2 [Add 'Key word1' and 'Key word2' to Keywords.Rq] >
< delkeyword:Key,word1,Key word2 [Delete 'Key word1' and 'Key word2' in Keywords.Rq] >
< bankeyword:Key,word1,Key word2 [Add Key word1 and Key word2 to Bannedword.Rq and remove it from Keywords.Rq] >
< addtosearch:@user1,@user2 [Add keyword and user2 (timelines/keywords) to To_Search.Rq] >
< deltosearch:@user1,@user2 [Delete user1 and user (timelines/keywords) in To_Search.Rq] >
< bantosearch:@user1,@user2 [Add user1 and user2 to Bannedpeople.Rq and remove it from To_Search.Rq] >
< addrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Add rss feeds to Rss.Rq] >
< delrss:https://www.url1.com/fluxrss.xml,http://url2.com/rss [Delete rss feeds in Rss.Rq]>`
