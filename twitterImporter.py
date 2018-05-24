import requests
import re
from bs4 import BeautifulSoup


url = 'https://twitter.com/paulavalb'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')
print(soup)


comment_box = soup.find_all(class_='FullNameGroup')
print(comment_box)
name_box = soup.find_all('span', attrs={'class': 'FullNameGroup'})
print(name_box)
nameTag_box = soup.find_all('span', attrs={'class': 'FullNameGroup'})
time_box = soup.find_all('a', attrs={'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})

#if not comment_box:
#    print("This account is private")
#    quit()


x = 0
for i in comment_box:
    comment = comment_box[x].text
    name = name_box[x].text
    tag = nameTag_box[x].next_sibling.text
    time = str(time_box[x])
    print(name, end='')
    print('  ', tag)
    print(comment)
    timeRegex = re.compile(r'\d+(:)\d+\s\w+\s(-)\s\d+\s\w+\s\d+')
    time = timeRegex.search(time)
    print(time.group())
    print('\n\n')
    x += 1
