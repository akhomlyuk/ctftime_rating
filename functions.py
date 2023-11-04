import requests
import json
from bs4 import BeautifulSoup

result_api_url = 'https://ctftime.org/api/v1/results/'
event_info_api_url = 'https://ctftime.org/api/v1/events/'
rht_url = 'https://ctftime.org/api/v1/teams/186788/'
rht_results = "https://ctftime.org/team/186788"


def rht_best_res() -> list:
    with requests.Session() as s:
        header = {
            'Host': 'ctftime.org',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'close'
        }
        response = s.get(rht_results, headers=header)
        soup = BeautifulSoup(response.content, "html.parser")
        table_div = soup.find("div", {"id": "rating_2023"})
        table = table_div.find("table")
        results = []
        total_rating = 0.0
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            place = cols[1].text.strip()
            event = cols[2].text.strip()
            ctf_points = cols[3].text.strip()
            rating_points = cols[4].text.replace('*', '').strip()
            results.append(
                {event: {'Place': int(place), 'CTF points': float(ctf_points), 'Rating': float(rating_points)}})
            sorted_data = sorted(results, key=lambda x: x[list(x.keys())[0]]['Rating'], reverse=True)
        for i in sorted_data[:9]:
            for j in i:
                total_rating += i[j].get('Rating')
        return [sorted_data[:9], total_rating]


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
