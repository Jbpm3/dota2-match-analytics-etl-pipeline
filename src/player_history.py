import requests

acc_id = 909467283

url = f"https://api.opendota.com/api/players/{acc_id}/matches"

limit = 20

params = {"limit":limit}

response = requests.get(url, params=params, timeout=15)
response.raise_for_status()

match_data = response.json()

print(f"Total matches retrieved: {len(match_data)}")

for num, match in enumerate(match_data, start=1):
    is_radiant = match["player_slot"] < 128
    radiant_win = match["radiant_win"]
    result = "Win" if is_radiant == radiant_win else "Loss"
    
    
    print(f"{num}. Match ID: {match['match_id']} | Hero ID: {match['hero_id']} | "
          f"Result: {result}")

