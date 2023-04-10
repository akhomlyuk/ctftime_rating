from typing import Tuple, Any

import requests
import json

result_api_url = 'https://ctftime.org/api/v1/results/'
event_info_api_url = 'https://ctftime.org/api/v1/events/'


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


def event_information(event_id: int) -> list:
    with requests.Session() as s:
        header = {
            'Host': 'ctftime.org',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'close'
        }
        event_info = s.get(event_info_api_url + str(event_id) + '/', headers=header)
        event_info = json.loads(event_info.text)
    return event_info
