import requests
import json

result_api_url = 'https://ctftime.org/api/v1/results/'
event_info_api_url = 'https://ctftime.org/api/v1/events/'
rht_url = 'https://ctftime.org/api/v1/teams/186788/'


def rht_info() -> dict:
    with requests.Session() as s:
        header = {
            'Host': 'ctftime.org',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'close'
        }
        rht = s.get(rht_url, headers=header)
        rht = json.loads(rht.text)
    return rht


def results_from_ctftime() -> dict:
    with requests.Session() as s:
        header = {
            'Host': 'ctftime.org',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'close'
        }
        b = s.get(result_api_url, headers=header)
        b = json.loads(b.text)
    return b


def event_information(event_id: int) -> dict:
    with requests.Session() as s:
        header = {
            'Host': 'ctftime.org',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'close'
        }
        event_info = s.get(event_info_api_url + str(event_id) + '/', headers=header)
        event_info = json.loads(event_info.text)
    return event_info
