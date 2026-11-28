import requests
from heroes import fetch_hero_names

hero_names = fetch_hero_names()

def fetch_match_history(acc_id,limit = 20):
    url = f"https://api.opendota.com/api/players/{acc_id}/matches"
    
    params = {"limit":limit}
    
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    
    return response.json()

def get_match_result(match):
    is_radiant = match["player_slot"] < 128
    radiant_win = match["radiant_win"]
    
    return "Win" if is_radiant == radiant_win else "loss"

def print_match_history(matches):
    for num, match in enumerate(matches, start=1):
        is_radiant = match["player_slot"] < 128
        radiant_win = match["radiant_win"]
        result = get_match_result(match)
    
        hero_id = match["hero_id"]
        hero_name = hero_names.get(hero_id, "Unknown Hero")
    
        print(f"{num}. Match ID: {match['match_id']} | Hero : {hero_name} | "
          f"Result: {result}")
        
def calculate_win_rate(matches):
    wins = 0
    
    if not matches:
        return 0.0
    
    for match in matches:
        results = get_match_result(match)
        if results == "Win":
            wins += 1

    win_rate = (wins / len(matches)) * 100
    
    return win_rate


def main():
    acc_id = 909467283
    
    matches = fetch_match_history(acc_id)
    
    hero_names = fetch_hero_names()
    
    print(f"Total matches: {len(matches)}")
    
    print_match_history(matches)
    
    win_rate = calculate_win_rate(matches)
    
    print(f"Win Rate: {win_rate:.2f}%")
    
    
if __name__ == "__main__":
    main()