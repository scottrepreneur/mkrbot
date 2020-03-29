import os
import re
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import praw


MAKER_FORUM_URL = 'https://forum.makerdao.com'
STAGING_FORUM_URL = 'https://staging-forum.makerfoundation.com'
ROCKETCHAT_URL = 'https://chat.makerdao.com'
governance_at_a_glance_topic = 84
test_gaag_topic = 15

REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_BOT_PW = os.getenv('REDDIT_BOT_PW')
BOT_USER_AGENT = 'mkrgov bot'
REDDIT_BOT_USER = os.getenv('REDDIT_BOT_USER')

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    password=REDDIT_BOT_PW,
    user_agent=BOT_USER_AGENT,
    username=REDDIT_BOT_USER
)

def forum_cross_post(post, test):
    
    response = requests.get(MAKER_FORUM_URL + f'/t/{governance_at_a_glance_topic}.json')
    print(response.json())

    topic_body = response.json()['post_stream']['posts'][0]['cooked']

    soup = BeautifulSoup(topic_body, 'html.parser')
    
    # header links
    header_links = soup.select('a strong')
    for link in header_links:
        link.parent.parent.replace_with(f"# [{link.contents[0]}]({link.parent['href']})")

    # mentions
    mentions_links = soup.find_all('a', class_='mention')
    for mention in mentions_links:
        mention.replace_with(f"[{mention.contents[0]}]({MAKER_FORUM_URL + mention['href']})")

    # remaining links
    links = soup.select('a')
    for link in links:
        link.replace_with(f"[{link.contents[0]}]({link['href']})")

    # list items
    list_items = soup.select('li')
    for item in list_items:
        item.replace_with(f"* {item.contents[0]}")
    
    # leftover list tags
    lists = soup.select('ul')
    for _list in lists:
        _list.unwrap()
    
    # superscripts
    superscripts = soup.select('small em')
    for s in superscripts:
        s.parent.replace_with(f"^({s.contents[0]})  ")

    # headers
    header_tags = soup.select('big strong')
    for header in header_tags:
        # print(header.parent)
        header.parent.replace_with(f'# {header.contents[0]}')

    # bolds
    bolds = soup.select('strong')
    for b in bolds:
        b.replace_with(f"**{b.contents[0]}**")

    # horizontal rules
    h_rules = soup.find_all('hr')
    for h in h_rules:
        h.decompose()

    # breaks
    breaks = soup.find_all('br')
    for b in breaks:
        b.decompose()

    soup.smooth()

    # paragraph tags
    p_tags = soup.select('p')
    for p in p_tags:
        p.unwrap()

    # move to string manipulation 
    # clear extra * LFW is using for emphasis
    soup = str(soup).replace('***','**')

    # break up link points a bit
    soup = soup.replace('\n[', '\n\n[')

    # add link to beginning
    soup = soup.replace(
        '**The one stop shop for finding out what’s being discussed by governance right now.**',
        f"**[The one stop shop for finding out what’s being discussed by governance right now.]({MAKER_FORUM_URL + '/t/governance-at-a-glance/' + str(governance_at_a_glance_topic)})**  ")
    
    # interject brought to you by
    soup = soup[:soup.find('# Three Point Summary')] + '\nBrought to you by u/LongForWisdom\n' + soup[soup.find('# Three Point Summary'):] 

    # append footer
    soup = soup + f'\n\n[Join us on the Forum for more discussion]({MAKER_FORUM_URL}) and in [RocketChat]({ROCKETCHAT_URL}).'

    #* post to reddit api in r/makerdao

    if not test:
        reddit.subreddit('makerdao').submit(f'Governance at a Glance - {datetime.now().strftime("%d/%m/%y")}', selftext=soup)
    else:
        reddit.subreddit('scottrepreneur').submit(f'Governance at a Glance - {datetime.now().strftime("%d/%m/%y")}', selftext=soup)
