# DCS Campaign Planner

A lightweight Python tool to manage and track dynamic campaigns in DCS World. Inspired by DCS Liberation, but designed to be simple, scriptable, and easy to extend.

Plan your campaign, log mission results, track frontline changes, and generate an HTML briefing from the terminal.

## Features

- Create campaigns on 3 theaters: Caucasus, Persian Gulf, Sinai
- Track airbase control (BLUE / RED)
- Log missions: CAP, CAS, SEAD, STRIKE, DEAD
- Advance the campaign day by day
- Generate a dark-themed HTML briefing with mission history
- Save/load campaign state as JSON

## Quick Start

```bash
git clone https://github.com/RisKyAyO/dcs-campaign-planner
cd dcs-campaign-planner
pip install -r requirements.txt

# Start a new campaign
python main.py new "Op. Desert Storm" persian_gulf

# Log a mission
python main.py mission "Op._Desert_Storm.json" STRIKE "Bandar Abbas SAM" "Viper 1-1,Viper 1-2" SUCCESS 0

# Capture an airbase
python main.py capture "Op._Desert_Storm.json" "Kish" blue

# Advance to next day
python main.py next-day "Op._Desert_Storm.json"

# Generate HTML briefing
python main.py briefing "Op._Desert_Storm.json"
```

## Commands

| Command | Description |
|---|---|
| `new <name> <theater>` | Start a new campaign |
| `status <save.json>` | Print campaign state |
| `mission <save.json> <TYPE> <target> <pkg> <RESULT> <losses>` | Log a mission |
| `capture <save.json> <airbase> <coalition>` | Change airbase control |
| `next-day <save.json>` | Advance one day |
| `briefing <save.json>` | Generate HTML briefing |

Mission types: CAP, CAS, SEAD, STRIKE, DEAD
Results: SUCCESS, PARTIAL, FAILURE

## Theaters

| Theater | Key airbases |
|---|---|
| caucasus | Batumi, Kutaisi, Senaki, Gudauta, Mozdok |
| persian_gulf | Al Dhafra, Al Minhad, Bandar Abbas, Kish |
| sinai | Ben Gurion, Ovda, Cairo Intl, El Arish |

## Structure

```
dcs-campaign-planner/
├── main.py          # CLI entry point
├── campaign.py      # Campaign class (state, save/load)
├── theaters.py      # Theater and airbase data
├── briefing.py      # HTML briefing generator
└── requirements.txt
```

## License

MIT
