import requests
import json
import logging

result_api_url = 'https://ctftime.org/api/v1/results/'
event_info_api_url = 'https://ctftime.org/api/v1/events/'
rht_url = 'https://ctftime.org/api/v1/teams/186788/'
# rht_results = "https://ctftime.org/team/186788"

header = {'Host': 'ctftime.org',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36',
          'Referer': 'https://ctftime.org/'}

RHT = 186788


def rht_best_res() -> list:
    try:
        with requests.Session() as s:
            response = s.get(result_api_url, headers=header)
            response_text = response.json()
            results = []
            results_for_menu = []
            for key, value in response_text.items():
                for i in value['scores']:
                    if i.get('team_id') == RHT:
                        results.append(
                            {value.get('title'): {'Place': int(i.get('place')), 'CTF points': float(i.get('points'))}})
                        sorted_data = sorted(results, key=lambda x: x[list(x.keys())[0]]['Place'])
            for i in sorted_data[:10]:
                for j in i:
                    place = i[j].get("Place")
                    if i[j].get("Place") == 1:
                        results_for_menu.append(f'🥇 {j} - <b>{place}</b>')
                    elif i[j].get("Place") == 2:
                        results_for_menu.append(f'🥈 {j} - <b>{place}</b>')
                    elif i[j].get("Place") == 3:
                        results_for_menu.append(f'🥉 {j} - <b>{place}</b>')
                    else:
                        results_for_menu.append(f'🪣 {j} - <b>{place}</b>')
            return [sorted_data, results_for_menu]
    except Exception as e:
        logging.error(e)
        pass


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
