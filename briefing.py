"""
Generate an HTML mission briefing from campaign state.
"""

from campaign import Campaign

MISSION_COLORS = {"SUCCESS": "#27ae60", "PARTIAL": "#f39c12", "FAILURE": "#e74c3c"}
COALITION_COLORS = {"blue": "#2980b9", "red": "#c0392b"}


def generate_briefing(campaign: Campaign, output_path: str = None):
    blue_bases = campaign.controlled_by("blue")
    red_bases  = campaign.controlled_by("red")
    output_path = output_path or f"{campaign.name.replace(' ', '_')}_briefing.html"

    mission_rows = ""
    for m in reversed(campaign.missions[-10:]):
        color = MISSION_COLORS.get(m["result"], "#888")
        pkg   = ", ".join(m["package"])
        mission_rows += f"""
        <tr>
          <td>Day {m['day']}</td><td><b>{m['type']}</b></td>
          <td>{m['target']}</td><td>{pkg}</td>
          <td style="color:{color};font-weight:bold">{m['result']}</td>
          <td>{m['losses']}</td>
        </tr>"""

    ab_rows = ""
    for ab, col in sorted(campaign.airbases.items()):
        color = COALITION_COLORS[col]
        ab_rows += f"<tr><td>{ab}</td><td style='color:{color};font-weight:bold'>{col.upper()}</td></tr>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{campaign.name} -- Day {campaign.day} Briefing</title>
  <style>
    body {{ font-family: 'Courier New', monospace; background: #0d1117; color: #c9d1d9; margin: 40px; }}
    h1 {{ color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 10px; }}
    h2 {{ color: #79c0ff; margin-top: 30px; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
    th {{ background: #161b22; color: #58a6ff; padding: 8px 12px; text-align: left; }}
    td {{ padding: 6px 12px; border-bottom: 1px solid #21262d; }}
    tr:hover {{ background: #161b22; }}
    .stat-box {{ display: inline-block; background: #161b22; border: 1px solid #30363d;
                 border-radius: 6px; padding: 12px 24px; margin: 8px; text-align: center; }}
    .stat-num {{ font-size: 2em; font-weight: bold; color: #58a6ff; }}
    .stat-label {{ font-size: 0.85em; color: #8b949e; }}
  </style>
</head>
<body>
  <h1>DCS -- {campaign.name}</h1>
  <p>Theater: <b>{campaign.theater_data['name']}</b> | Day: <b>{campaign.day}</b></p>
  <div>
    <div class="stat-box"><div class="stat-num" style="color:#2980b9">{len(blue_bases)}</div><div class="stat-label">BLUE Airbases</div></div>
    <div class="stat-box"><div class="stat-num" style="color:#c0392b">{len(red_bases)}</div><div class="stat-label">RED Airbases</div></div>
    <div class="stat-box"><div class="stat-num">{len(campaign.missions)}</div><div class="stat-label">Missions Flown</div></div>
    <div class="stat-box"><div class="stat-num" style="color:#e74c3c">{campaign.losses['blue']}</div><div class="stat-label">Blue A/C Lost</div></div>
  </div>
  <h2>Airbase Control</h2>
  <table><tr><th>Airbase</th><th>Coalition</th></tr>{ab_rows}</table>
  <h2>Mission Log (last 10)</h2>
  <table>
    <tr><th>Day</th><th>Type</th><th>Target</th><th>Package</th><th>Result</th><th>Losses</th></tr>
    {mission_rows if mission_rows else '<tr><td colspan="6" style="color:#8b949e">No missions logged yet.</td></tr>'}
  </table>
</body></html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Briefing saved to {output_path}")
    return output_path
