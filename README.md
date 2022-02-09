##RedQueen

My personal search bot crawling twitter for infoSec news made in ~2010..

Have to rewrite it but still working it seems.

##Description

It tries to sort all tweets from worst to best tweet by giving them a score
 
depending on their contents , nbr of followers , retweets , favorites , language , media 

, timestamp , emoticon , if already sent or not , if content or user bio contains banned words or is from a banned user ,

Check if there is enough text, check if Tweet is Follow Friday or if too much hashs,

check and act if tweet is from a verifed account or from a friend or follower , check if current tweet contains some part.

of tweet already sent to prevent retweeting the same info twice , do not retweet the same user more than 3 times ,

do not retweet if retweet count is not at least 1 (Roll a dice and if 1 give a chance to this tweet )

do not retweet if retweet count or Fav more than 323 (check if from friend or followers before), 

do not retweet if older than 2 days (Roll a dice if 1 give it a chance),Saves item already searched ,

do not retweet if the user is not followed by at least 400 ppl,

Such quote Th3j3st3r , MAny Replace his name by Th3Bouf0n , Very Hack, Much Wow ,  

saves items searched which returned no result and removes them from the search list,

provide some statistics about the current session during api resting time,

it does respect the limit of twitter api by saving the total nbr of calls and then

behave depending on how many call are left to be send (reset calls every 24 hours), etc ...


Then Sends a dm when done retweeting all the good stuff in its timeline .


Banned words/users/ can be update by sending cmd seperated by comma via dm to Redqueen .

ex: Banuser,bouffon,@thejester,Add:ZeroDay,dark web rocks!,@bfm,https://t.co/nFj083Iybr

Banuser will add the user from the quote https://t.co/nFj083Iybr to Banned Users list (./Data/Rq.Bannedpeople)

Then Will add @thejester and @bfm to Banned Users list too.

"bouffon" and "dark web rocks!" will be add to Banned words list (./Data/Rq.Bannedword)

And Add:ZeroDay will add ZeroDay to the keywords list .(./Data/Rq.Keywords)

## Installation

pip install asciimatics
pip install emoji
pip install twython
python 2.7


Edit TwitterApiKeys.py and Rq.Bannedpeople ,Rq.Bannedword ,Rq.Following ,Rq.Friends ,Rq.Keywords in ./Data to fit your needs .
Then Run the beast .
