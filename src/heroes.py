import requests

def fetch_hero_names():
    url = "https://api.opendota.com/api/heroes"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    heroes = response.json()

    hero_names = {}

    for hero in heroes:
        hero_id = hero["id"]
        hero_name = hero["localized_name"]

        hero_names[hero_id] = hero_name

    return hero_names
