import willie
import re

@willie.module.rule('.*(?:^| )/?r/([A-Za-z0-9][A-Za-z0-9_]{2,20})/?(?:$| ).*')
def sublink(bot, trigger):
    """Gives a subreddit url and title when the abreviation r/subreddit is posted to the channel"""

    url = 'https://www.reddit.com/r/' + trigger.group(1) + '/'
    data = willie.web.get(url, limit_bytes=1024)
    title = re.match('.*<title>(.+)</title>.*', data).group(1)
    
    if title == 'search results' : bot.reply('r/' + trigger.group(1) + ' doesn\'t seem to exist')
    else : bot.say('\x02r/' + trigger.group(1) + '\x02 [' + title + '] ' + url)
