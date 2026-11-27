# Dota 2 match analytics ETL pipeline

Python scripts that fetch Dota 2 match data from OpenDota and print match summaries and player history.

The project currently covers data extraction and console output. Data storage and a complete extract, transform, and load workflow are not implemented yet.

## Recent updates

- Added player match history with a default limit of 20 matches.
- Refactored player history into reusable functions for fetching matches, determining results, and printing history.
- Added Radiant and Dire rosters with player names, hero IDs, and kills, deaths, and assists.
- Changed match duration output to minutes and seconds.

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

The script prints the number of returned matches, followed by each match's ID, hero ID, and win or loss result from the player's perspective.

`fetch_match_history(acc_id, limit=20)` controls the number of matches requested. To request a different number, change the call in `main()`, for example:

```python
matches = fetch_match_history(acc_id, limit=50)
```

Both scripts read IDs from the source code. They do not accept command-line arguments.

## Project files

| File | Purpose |
| --- | --- |
| [`src/extract.py`](src/extract.py) | Fetches one match and prints its duration and team statistics. |
| [`src/player_history.py`](src/player_history.py) | Fetches a player's match history and prints results. |
| [`requirements.txt`](requirements.txt) | Lists the Python dependency. |

## Current limitations

- `calculate_win_rate()` is unfinished and returns an undefined variable. The player history script does not call it.
- Results are printed to the console. The scripts do not save data to files or a database.
- API requests use a 15-second timeout and raise errors for unsuccessful HTTP responses. There is no retry logic.
