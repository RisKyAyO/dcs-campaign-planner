"""
DCS World theater definitions -- airbases, coordinates, coalitions.
"""

THEATERS = {
    "caucasus": {
        "name": "Caucasus",
        "airbases": {
            "Batumi":          {"coalition": "blue", "lat": 41.6, "lon": 41.6},
            "Kobuleti":        {"coalition": "blue", "lat": 41.9, "lon": 41.9},
            "Kutaisi":         {"coalition": "blue", "lat": 42.2, "lon": 42.7},
            "Tbilisi-Lochini": {"coalition": "blue", "lat": 41.7, "lon": 44.9},
            "Senaki":          {"coalition": "blue", "lat": 42.2, "lon": 42.0},
            "Gudauta":         {"coalition": "red",  "lat": 43.1, "lon": 40.6},
            "Sukhumi":         {"coalition": "red",  "lat": 43.0, "lon": 41.0},
            "Mozdok":          {"coalition": "red",  "lat": 43.8, "lon": 44.6},
            "Mineralnye Vody": {"coalition": "red",  "lat": 44.2, "lon": 43.1},
        },
        "frontline_default": ["Senaki", "Gudauta"],
    },
    "persian_gulf": {
        "name": "Persian Gulf",
        "airbases": {
            "Al Dhafra":    {"coalition": "blue", "lat": 24.2, "lon": 54.5},
            "Al Minhad":    {"coalition": "blue", "lat": 25.0, "lon": 55.4},
            "Dubai Intl":   {"coalition": "blue", "lat": 25.3, "lon": 55.4},
            "Bandar Abbas": {"coalition": "red",  "lat": 27.2, "lon": 56.4},
            "Havadarya":    {"coalition": "red",  "lat": 27.2, "lon": 56.2},
            "Kish":         {"coalition": "red",  "lat": 26.5, "lon": 54.0},
        },
        "frontline_default": ["Al Dhafra", "Bandar Abbas"],
    },
    "sinai": {
        "name": "Sinai",
        "airbases": {
            "Ben Gurion":  {"coalition": "blue", "lat": 32.0, "lon": 34.9},
            "Ramat David": {"coalition": "blue", "lat": 32.7, "lon": 35.2},
            "Ovda":        {"coalition": "blue", "lat": 29.9, "lon": 34.9},
            "Cairo Intl":  {"coalition": "red",  "lat": 30.1, "lon": 31.4},
            "Cairo West":  {"coalition": "red",  "lat": 30.1, "lon": 31.0},
            "El Arish":    {"coalition": "red",  "lat": 31.1, "lon": 33.8},
        },
        "frontline_default": ["Ovda", "El Arish"],
    },
}
