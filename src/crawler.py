import json
import os
import requests

from bs4 import BeautifulSoup

from constants.bot import BOT_START_MESSAGE
from constants.kofa import KOFA_BASE_URL


def fetch():
    response = requests.get(f'{KOFA_BASE_URL}/cinematheque/screenings')
    response.encoding = 'utf-8'

    return response.text


def get_lies_from(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select('.cm-list-program-1 > li')


def get_title_from(li):
    return li.select('.txt-2')[0].contents[0].strip()


def get_url_path_from(li):
    return li.select('a')[0]['href']


def get_url_from(li):
    return KOFA_BASE_URL + get_url_path_from(li)


def get_kofa_id_from(li):
    return get_url_path_from(li).split('/')[-1]


def parse(html):
    return [
        {
            'title': get_title_from(li),
            'url': get_url_from(li),
            'kofa_id': get_kofa_id_from(li),
        }
        for li in get_lies_from(html)
    ]


def crawl():
    return parse(fetch())
