from curl_cffi import requests


def get_soup(url: str) -> dict:
    response = requests.get(url, impersonate="chrome")
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")
    return response.json()
