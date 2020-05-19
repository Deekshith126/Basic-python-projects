import requests
from bs4 import BeautifulSoup
import pprint


page = requests.get('https://news.ycombinator.com/news')
page2 = requests.get('https://news.ycombinator.com/news?p=2')
page3 = requests.get('https://news.ycombinator.com/news?p=3')
page4 = requests.get('https://news.ycombinator.com/news?p=4')
page5 = requests.get('https://news.ycombinator.com/news?p=5')



soup = BeautifulSoup(page.text,'html.parser')
soup2 = BeautifulSoup(page2.text,'html.parser')
soup3 = BeautifulSoup(page3.text,'html.parser')
soup4 = BeautifulSoup(page4.text,'html.parser')
soup5 = BeautifulSoup(page5.text,'html.parser')



links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

links3 = soup3.select('.storylink')
subtext3 = soup3.select('.subtext')

links4 = soup4.select('.storylink')
subtext4 = soup4.select('.subtext')

links5 = soup5.select('.storylink')
subtext5 = soup5.select('.subtext')



mega_links = links + links2 + links3 + links4 + links5
mega_subtext = subtext + subtext2 + subtext3 + subtext4 + subtext5


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['votes'],reverse = True)
	


def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points',''))
            if points > 50:   #---> use this to filter the stories based on votes
                hn.append({'title':title, 'links':href,'votes':points})
            
    return sort_stories_by_votes(hn)
	

pprint.pprint(create_custom_hn(mega_links,mega_subtext))