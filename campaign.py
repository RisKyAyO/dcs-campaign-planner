"""
Campaign state -- tracks airbases, units, missions and frontline.
"""

import json
from theaters import THEATERS


class Campaign:
    def __init__(self, name: str, theater: str, day: int = 1):
        if theater not in THEATERS:
            raise ValueError(f"Unknown theater '{theater}'. Available: {list(THEATERS)}")
        self.name = name
        self.theater = theater
        self.day = day
        self.theater_data = THEATERS[theater]

        self.airbases = {
            ab: data["coalition"]
            for ab, data in self.theater_data["airbases"].items()
        }
        self.missions: list[dict] = []
        self.losses = {"blue": 0, "red": 0}

    def capture(self, airbase: str, coalition: str):
        if airbase not in self.airbases:
            raise ValueError(f"Airbase '{airbase}' not found.")
        if coalition not in ("blue", "red"):
            raise ValueError("Coalition must be 'blue' or 'red'.")
        old = self.airbases[airbase]
        self.airbases[airbase] = coalition
        print(f"[Day {self.day}] {airbase} captured by {coalition.upper()} (was {old.upper()}).")

    def controlled_by(self, coalition: str) -> list[str]:
        return [ab for ab, col in self.airbases.items() if col == coalition]

    def add_mission(self, mission_type: str, package: list[str],
                    target: str, result: str, losses: int = 0):
        mission = {
            "day": self.day, "type": mission_type.upper(),
            "package": package, "target": target,
            "result": result.upper(), "losses": losses,
        }
        self.missions.append(mission)
        self.losses["blue"] += losses
        print(f"[Day {self.day}] Mission logged: {mission_type} vs '{target}' -- {result}")
        return mission

    def next_day(self):
        self.day += 1
        print(f"\n--- Advancing to Day {self.day} ---")

    def status(self):
        blue = self.controlled_by("blue")
        red  = self.controlled_by("red")
        sep  = "=" * 50
        print(f"\n{sep}")
        print(f"  Campaign : {self.name}  |  Theater : {self.theater_data['name']}  |  Day {self.day}")
        print(sep)
        print(f"  BLUE airbases ({len(blue)}): {', '.join(blue) or 'none'}")
        print(f"  RED  airbases ({len(red)}):  {', '.join(red) or 'none'}")
        print(f"  Missions flown : {len(self.missions)}")
        print(f"  Blue losses    : {self.losses['blue']} a/c")
        if self.missions:
            last = self.missions[-1]
            print(f"  Last mission   : [Day {last['day']}] {last['type']} -- {last['result']}")
        print(f"{sep}\n")

    def save(self, path: str = None):
        path = path or f"{self.name.replace(' ', '_')}.json"
        data = {
            "name": self.name, "theater": self.theater, "day": self.day,
            "airbases": self.airbases, "missions": self.missions, "losses": self.losses,
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"Campaign saved to {path}")

    @classmethod
    def load(cls, path: str) -> "Campaign":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        c = cls(data["name"], data["theater"], data["day"])
        c.airbases = data["airbases"]
        c.missions = data["missions"]
        c.losses   = data["losses"]
        print(f"Campaign '{c.name}' loaded (Day {c.day}).")
        return c
