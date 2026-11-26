import requests

match_id = 9105978646

url = f"https://api.opendota.com/api/matches/{match_id}"

response = requests.get(url, timeout=15)

response.raise_for_status()

match_data = response.json()

print(match_data["match_id"])

duration_minutes = match_data["duration"] / 60

print(f"Match Duration: {duration_minutes:.2f} minutes")