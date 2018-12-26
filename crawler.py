import json
import os
import requests

from bs4 import BeautifulSoup

from constants import KOFA_BASE_URL, BOT_START_MESSAGE


def fetch():
    response = requests.get(f'{KOFA_BASE_URL}/cinematheque/screenings')
    response.encoding = 'utf-8'

    return response.text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')

    return [
        {
            'title': li.select('.txt-2')[0].contents[0].strip(),
            'link': KOFA_BASE_URL + li.select('a')[0]['href'],
            'kofa_id': li.select('a')[0]['href'].split('/')[-1]
        }
        for li in soup.select('.cm-list-program-1 > li')
    ]


def crawl():
    return parse(fetch())
