import requests

match_id = 9105978646

url = f"https://api.opendota.com/api/matches/{match_id}"

response = requests.get(url, timeout=15)

response.raise_for_status()

match_data = response.json()

print(match_data["match_id"])

duration_minutes = match_data["duration"] // 60
duration_seconds = match_data["duration"] % 60 

print(f"Match Duration: {duration_minutes} minutes and {duration_seconds} seconds")

players = match_data["players"]

def get_player_stats(player):
    hero_id = player["hero_id"]
    kills = player["kills"]
    deaths = player["deaths"]
    assists = player["assists"]
    
    return hero_id, kills, deaths, assists
    

radiant_players = []
dire_players = []

for player in players:
    if player["player_slot"] < 128:
        radiant_players.append(player)
    else:
        dire_players.append(player)
        

def print_team(team_name, team_players):
    print(f"\n== {team_name} ===")
    
    for num, player in enumerate(team_players, start = 1):
        name = player.get("personaname") or "Anonymous Player"
    
        hero_id, kills, deaths, assists = get_player_stats(player)
    
        print(f"{num}. {name} | Hero ID: {hero_id} | "
            f"K/D/A: {kills}/{deaths}/{assists} "
        )

print_team("RADIANT", radiant_players)
print_team("DIRE",dire_players)

