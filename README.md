# Dota 2 match analytics ETL pipeline

Python scripts that fetch Dota 2 match data from OpenDota and print match summaries, player history, and hero performance.

The current workflow fetches data, calculates match statistics, and prints the results. Data storage and loading are planned.

## Recent updates

- Player history now resolves hero IDs to localized names from OpenDota.
- The script calculates the player's overall win rate and reports match counts, wins, and win rates for each hero played.

## Setup

Install Python 3, then run these commands from the repository root. The scripts depend on `requests`, listed in `requirements.txt`.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS and Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

The commands below use the Windows virtual environment. On macOS and Linux, replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`.

## View a match

Set `match_id` in [`src/extract.py`](src/extract.py) to the match you want to inspect. The current example is `9105978646`.

```powershell
.\.venv\Scripts\python.exe src/extract.py
```

The script prints:

- The match ID and duration in minutes and seconds.
- Separate Radiant and Dire rosters.
- Each player's name, hero ID, and kills/deaths/assists. Missing names appear as `Anonymous Player`.

## View player match history

Set `acc_id` inside `main()` in [`src/player_history.py`](src/player_history.py) to the OpenDota account ID you want to inspect. The current example is `909467283`.

```powershell
.\.venv\Scripts\python.exe src/player_history.py
```

The script prints the number of returned matches and lists each match ID, hero name, and win or loss from the player's perspective. It displays `Unknown Hero` when an ID has no name in the OpenDota lookup.

The overall win rate is the percentage of returned matches the player won. The hero performance summary lists the matches played, wins, and win rate for each hero in that same set of matches.

`fetch_match_history(acc_id, limit=20)` controls the number of matches requested. To request a different number, change the call in `main()`, for example:

```python
matches = fetch_match_history(acc_id, limit=50)
```

Both scripts read IDs from the source code. They do not accept command-line arguments.

## Project files

| File | Purpose |
| --- | --- |
| [`src/extract.py`](src/extract.py) | Fetches one match and prints its duration and team statistics. |
| [`src/player_history.py`](src/player_history.py) | Prints player match history, overall win rate, and per-hero statistics. |
| [`src/heroes.py`](src/heroes.py) | Maps OpenDota hero IDs to localized names. |
| [`requirements.txt`](requirements.txt) | Lists the Python dependency. |

## Current limitations

- Results are printed to the console. The scripts do not save data to files or a database.
- API requests use a 15-second timeout and raise errors for unsuccessful HTTP responses. There is no retry logic.
