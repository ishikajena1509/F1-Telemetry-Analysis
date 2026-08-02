import streamlit as st
import fastf1
from pathlib import Path

def format_laptime(td):
    total_seconds = td.total_seconds()

    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    return f"{minutes}:{seconds:06.3f}"

st.set_page_config(
    page_title="Insights | F1 Telemetry Analytics Platform",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
#Race Insights

Transform telemetry into engineering insights.
""")

st.divider()

BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "cache"
CACHE_DIR.mkdir(exist_ok=True)

fastf1.Cache.enable_cache(str(CACHE_DIR))

YEAR = 2026
GRAND_PRIX = "China"
SESSION_TYPE = "Q"

with st.spinner("Loading telemetry..."):
    session = fastf1.get_session(
        YEAR,
        GRAND_PRIX,
        SESSION_TYPE
    )
    session.load()

st.sidebar.header("Session Configuration")

available_drivers = sorted(
    session.laps["Driver"].dropna().unique()
)

driver1 = st.sidebar.selectbox(
    "Driver 1",
    available_drivers,
    index=0
)

driver2 = st.sidebar.selectbox(
    "Driver 2",
    available_drivers,
    index=1
)

if driver1 == driver2:
    st.error("Please select two different drivers.")
    st.stop()

results = session.results.set_index("Abbreviation")

driver1_name = results.loc[driver1]["FullName"]
driver2_name = results.loc[driver2]["FullName"]

driver1_team = results.loc[driver1]["TeamName"]
driver2_team = results.loc[driver2]["TeamName"]

driver1_fastest = session.laps.pick_drivers(driver1).pick_fastest()
driver2_fastest = session.laps.pick_drivers(driver2).pick_fastest()

driver1_time = driver1_fastest["LapTime"]
driver2_time = driver2_fastest["LapTime"]

if driver1_time < driver2_time:
    winner_name = driver1_name
    winner_team = driver1_team
    winner_lap = driver1_fastest
    lap_gap = (driver2_time - driver1_time).total_seconds()
else:
    winner_name = driver2_name
    winner_team = driver2_team
    winner_lap = driver2_fastest
    lap_gap = (driver1_time - driver2_time).total_seconds()

driver1_speed = driver1_fastest.get_car_data()["Speed"].max()
driver2_speed = driver2_fastest.get_car_data()["Speed"].max()

speed_diff = abs(driver1_speed - driver2_speed)

st.markdown("##Session Summary")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
###Winner

**{winner_name}**

Team: **{winner_team}**

Fastest Lap: **{format_laptime(winner_lap['LapTime'])}**
""")

with col2:

    st.metric(
        "Gap to Other Driver",
        f"{lap_gap:.3f} s"
    )

    st.metric(
        "Top Speed Difference",
        f"{speed_diff:.1f} km/h"
    )

st.divider()

st.markdown("##Sector Analysis")

sector1 = {
    driver1_name: driver1_fastest["Sector1Time"],
    driver2_name: driver2_fastest["Sector1Time"]
}

sector2 = {
    driver1_name: driver1_fastest["Sector2Time"],
    driver2_name: driver2_fastest["Sector2Time"]
}

sector3 = {
    driver1_name: driver1_fastest["Sector3Time"],
    driver2_name: driver2_fastest["Sector3Time"]
}

col1, col2, col3 = st.columns(3)

with col1:

    winner_s1 = min(sector1, key=sector1.get)

    st.success(f"""
### Sector 1

**{winner_s1}**

{sector1[winner_s1].total_seconds():.3f}s
""")

with col2:

    winner_s2 = min(sector2, key=sector2.get)

    st.success(f"""
### Sector 2

**{winner_s2}**

{sector2[winner_s2].total_seconds():.3f}s
""")

with col3:

    winner_s3 = min(sector3, key=sector3.get)

    st.success(f"""
### Sector 3

**{winner_s3}**

{sector3[winner_s3].total_seconds():.3f}s
""")
st.divider()

st.markdown("##Engineer Analysis")

observations = []

observations.append(
    f"**{winner_name}** recorded the fastest lap of the session in **{format_laptime(winner_lap['LapTime'])}**."
)

if driver1_speed > driver2_speed:
    observations.append(
        f"**{driver1_name}** achieved the higher top speed by **{driver1_speed-driver2_speed:.1f} km/h**."
    )
else:
    observations.append(
        f"**{driver2_name}** achieved the higher top speed by **{driver2_speed-driver1_speed:.1f} km/h**."
    )

sector_wins = {
    driver1_name: 0,
    driver2_name: 0
}

if winner_s1 == driver1_name:
    sector_wins[driver1_name] += 1
else:
    sector_wins[driver2_name] += 1

if winner_s2 == driver1_name:
    sector_wins[driver1_name] += 1
else:
    sector_wins[driver2_name] += 1

if winner_s3 == driver1_name:
    sector_wins[driver1_name] += 1
else:
    sector_wins[driver2_name] += 1

overall_sector_winner = max(sector_wins, key=sector_wins.get)

observations.append(
    f"**{overall_sector_winner}** was quicker in **{sector_wins[overall_sector_winner]} out of 3 sectors**."
)

observations.append(
    f"The overall lap difference between the selected drivers was **{lap_gap:.3f} seconds**."
)

for obs in observations:
    st.info(obs)

st.divider()

st.markdown("##Key Takeaways")

takeaways = []

takeaways.append(f"Faster Driver: **{winner_name}**")

if driver1_speed > driver2_speed:
    takeaways.append(
        f"Higher Top Speed: **{driver1_name}** ({driver1_speed:.1f} km/h)"
    )
else:
    takeaways.append(
        f"Higher Top Speed: **{driver2_name}** ({driver2_speed:.1f} km/h)"
    )

takeaways.append(
    f"Sector Advantage: **{overall_sector_winner}** won **{sector_wins[overall_sector_winner]} of 3 sectors**."
)

if lap_gap < 0.2:
    gap_comment = "Extremely close battle."
elif lap_gap < 0.5:
    gap_comment = "Competitive qualifying pace."
else:
    gap_comment = "Clear pace advantage."

takeaways.append(f"{gap_comment}")

for takeaway in takeaways:
    st.success(takeaway)

st.divider()
st.caption(
    " F1 Telemetry Analytics Platform | Built using Python • FastF1 • Plotly • Streamlit"
)