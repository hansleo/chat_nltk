from __future__ import print_function

from nltk.chat.util import Chat
from nltk.chat.eliza import eliza_chat
from nltk.chat.iesha import iesha_chat
from nltk.chat.rude import rude_chat
from nltk.chat.suntsu import suntsu_chat
from nltk.chat.zen import zen_chat
import sys

bots = [
    (eliza_chat,  'Eliza (psycho-babble)'),
    (iesha_chat,  'Iesha (teen anime junky)'),
    (rude_chat,   'Rude (abusive bot)'),
    (suntsu_chat, 'Suntsu (Chinese sayings)'),
    (zen_chat,    'Zen (gems of wisdom)')]

print("test")

# def chatbots():
print('Which chatbot would you like to talk to?')
botcount = len(bots)
for i in range(botcount):
    print('  %d: %s' % (i+1, bots[i][1]))
while True:
    print('\nEnter a number in the range 1-%d: ' % botcount, end=' ')
    choice = input()
    if choice.isdigit() and (int(choice) - 1) in range(botcount):
        break
    else:
        print('   Error: bad chatbot number')


chatbot = bots[int(choice)-1][0]
chatbot()