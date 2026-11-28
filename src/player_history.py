import requests
from heroes import fetch_hero_names
from datetime import datetime, timedelta, timezone

hero_names = fetch_hero_names()

def filter_recent_matches(matches, days=7):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    cutoff_timestamp = cutoff.timestamp()

    recent_matches = []

    for match in matches:
        # Checks whether match["start_time"]
        # is greater than or equal to cutoff_timestamp
        if match["start_time"] >= cutoff_timestamp:
            recent_matches.append(match)

    return recent_matches


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

def calculate_hero_stats(matches):
    hero_stats = {}

    for match in matches:
        hero_id = match["hero_id"]

        if hero_id not in hero_stats:
            hero_stats[hero_id] = {
                "matches": 0,
                "wins": 0
            }

        hero_stats[hero_id]["matches"] += 1

        if get_match_result(match) == "Win":
            hero_stats[hero_id]["wins"] += 1

    for hero_id, stats in hero_stats.items():
        stats["win_rate"] = (stats["wins"] / stats["matches"]) * 100

    return hero_stats

def print_hero_stats(hero_stats, hero_names):
    
    print("\n=== HERO PERFORMANCE ===")
    
    for hero_id, stats in hero_stats.items():
        hero_name = hero_names.get(hero_id, "Unknown Hero")

        matches = stats["matches"]
        wins = stats["wins"]
        win_rate = stats["win_rate"]
        
        print(f"{hero_name} | Matches: {matches} | Wins: {wins} | Win Rate: {win_rate:.2f}%")
        

def main():
    acc_id = 909467283
    
    matches = fetch_match_history(acc_id)
    
    hero_names = fetch_hero_names()
    
    print(f"Total matches: {len(matches)}")
    
    print_match_history(matches)
    
    win_rate = calculate_win_rate(matches)
    
    print(f"Win Rate: {win_rate:.2f}%")
    
    hero_stats = calculate_hero_stats(matches)
    
    print_hero_stats(hero_stats,hero_names)
    
    recent_matches = filter_recent_matches(matches)
    
    print(f"Matches in the last 7 days: {len(recent_matches)}")
    
    weekly_win_rate = calculate_win_rate(recent_matches)
    
    print(f"Weekly Win Rate: {weekly_win_rate:.2f}%")
    
if __name__ == "__main__":
    main()