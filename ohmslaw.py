# -*- coding: utf-8 -*-
import willie
import math
import re

@willie.module.commands('ohm', 'o')
@willie.module.example('.ohm 3.7V 1.8o')
def ohmcalc(bot, trigger):
    """Ohm's law calculator, takes two values and calculates the two others."""

    if not trigger.group(2) : return bot.reply('Usage example: .ohm 4.2v 1.8o')
    
    rawreq = trigger.group(2).replace(u'Ω', 'o').lower()
 
    request = re.match('^ *([0-9]*\.?[0-9]+) *([avwo]) +([0-9]*\.?[0-9]+) *([avwo]) *$', rawreq, re.I)
    
    if not request : return bot.reply('Error: Syntax error. Usage example: .ohm 4.2v 1.8o')
    if request.group(2) == request.group(4) : return bot.reply('Error: same unit used twice')
    
    units = [ request.group(2), request.group(4) ]
    value = 1
    for unit in units :
        if unit == 'a' : a = float(request.group(value))
        elif unit == 'v' : v = float(request.group(value))
        elif unit == 'w' : w = float(request.group(value))
        elif unit == 'o' : o = float(request.group(value))
        else : return bot.reply('Error: Unit error')
        value = 3

    known = '%s%s' % (request.group(2), request.group(4))
    
    if known == 'ao' or known == 'oa' :
        v = o * a
        w = pow(a, 2) * o
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sA & %sΩ ==> %sV & %sW' % (a, o, v, w))
        
    if known == 'av' or known == 'va' :
        w = v * a
        o = v / a
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sA & %sV ==> %sW & %sΩ' % (a, v, w, o))
        
    if known == 'aw' or known == 'wa' :
        v = w / a
        o = w / pow(a, 2)
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sA & %sW ==> %sV %sΩ' % (a, w, v, o))
        
    if known == 'vo' or known == 'ov' :
        a = v / o
        w = pow(v, 2) / o
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sV & %sΩ ==> %sW & %sA' % (v, o, w, a))
        
    if known == 'vw' or known == 'wv' :
        a = w / v
        o = pow(v, 2) / w
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sV & %sW ==> %sΩ & %sA' % (v, w, o, a))
        
    if known == 'wo' or known == 'ow' :
        a = math.sqrt(w / o)
        v = math.sqrt(w * o)
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        bot.reply('%sW & %sΩ ==> %sA & %sV' % (w, o, a, v))
        
def numtostr( n ):
    n = round(n, 2)
    if n.is_integer() : n = int(n)
    n = str(n)
    return n
