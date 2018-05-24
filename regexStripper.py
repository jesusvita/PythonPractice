import re

def regexStripper(s, string):
    if s is None:
        s = '\s'
    x = re.compile(r'^[{0}]+|[{0}]+$'.format(s))
    return x.sub('', string)


string1 = 'ssssss Jesus sssssss'
string2 = 'sssssssssJesusssssss'
string3 = 'SpamSpamBaconSpamEggsSpamSpam'
string4 = '                Hello               '
x = ' '

print(len(regexStripper(x, string4)))
print(regexStripper(x, string4))
