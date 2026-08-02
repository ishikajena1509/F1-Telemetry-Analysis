import streamlit as st
import fastf1
from pathlib import Path
import plotly.graph_objects as go
import pandas as pd

def format_laptime(td):
    total_seconds = td.total_seconds()

    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60
    return f"{td.total_seconds():.3f}s"

st.set_page_config(
    page_title="Dashboard | F1 Telemetry Analytics Platform",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

.dashboard-title{
    font-size:42px;
    font-weight:700;
    color:#E10600;
}

.subtitle{
    font-size:18px;
    color:#D0D0D0;
}
.winner-card {
    background: linear-gradient(135deg,#0F5132,#198754);
    padding: 28px;
    border-radius: 18px;
    color: white;
    border-left: 8px solid gold;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.35);
    margin-bottom: 15px;
}

.winner-title{
    font-size:18px;
    color:#FFD700;
    font-weight:700;
}

.winner-name{
    font-size:36px;
    font-weight:800;
    margin-bottom:10px;
}

.winner-info{
    font-size:18px;
    line-height:1.9;
}

</style>
""", unsafe_allow_html=True)

st.markdown("#F1 Telemetry Dashboard :      "
"Case Study   -  "
"2026 Chinese Grand Prix – Qualifying")

st.divider()
unsafe_allow_html=True


st.markdown(
"""
<p class="subtitle">
Compare Formula 1 drivers using official FastF1 telemetry data.
</p>
""",
unsafe_allow_html=True
)

st.divider()

BASE_DIR = Path(__file__).resolve().parent.parent

CACHE_DIR = BASE_DIR / "cache"

CACHE_DIR.mkdir(exist_ok=True)

fastf1.Cache.enable_cache(str(CACHE_DIR))

YEAR = 2026
GRAND_PRIX = "China"
SESSION_TYPE = "Q"

with st.spinner("Loading Formula 1 telemetry..."):

    session = fastf1.get_session(
        YEAR,
        GRAND_PRIX,
        SESSION_TYPE
    )

    session.load()
event = session.event

st.title(f"{event['EventName']} {event['EventDate'].year}")
st.caption(f"Session: {session.name}")

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

TEAM_COLORS = {
    "Mercedes": "#00D2BE",
    "Ferrari": "#DC0000",
    "McLaren": "#FF8700",
    "Red Bull Racing": "#1E41FF",
    "Aston Martin": "#006F62",
    "Williams": "#005AFF",
    "Alpine": "#0090FF",
    "Kick Sauber": "#52E252",
    "RB": "#6692FF",
    "Haas F1 Team": "#B6BABD"
}

driver1_color = TEAM_COLORS.get(driver1_team, "#3B82F6")
driver2_color = TEAM_COLORS.get(driver2_team, "#EF4444")

driver1_fastest = session.laps.pick_drivers(driver1).pick_fastest()
driver2_fastest = session.laps.pick_drivers(driver2).pick_fastest()

driver1_time = driver1_fastest["LapTime"]
driver2_time = driver2_fastest["LapTime"]

if driver1_time < driver2_time:
    winner = driver1
    winner_lap = driver1_fastest
else:
    winner = driver2
    winner_lap = driver2_fastest
winner_name = (
    driver1_name
    if winner == driver1
    else driver2_name
)
st.markdown("## Session Winner")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
<div class="winner-card">

<div class="winner-title">
SESSION WINNER
</div>

<div class="winner-name">
{winner_name}
</div>

<div class="winner-info">

<b>Team:</b> {winner_lap['Team']}<br>

⏱<b>Fastest Lap:</b> {format_laptime(winner_lap['LapTime'])}<br>

<b>Top Speed:</b> {winner_lap.get_car_data()['Speed'].max():.1f} km/h

</div>

</div>
""", unsafe_allow_html=True)

with col2:

    st.metric(
        label="Winner",
        value=winner_name
    )

st.divider()

driver1_car = driver1_fastest.get_car_data().add_distance()
driver2_car = driver2_fastest.get_car_data().add_distance()

st.markdown("## Performance Overview")

comparison_data = {
    "Metric": [
        "Team",
        "Fastest Lap",
        "Top Speed (km/h)",
        "Average Speed (km/h)",
        "Maximum RPM"
    ],

    driver1_name: [
        driver1_team,
        format_laptime(driver1_fastest["LapTime"]),
        f"{driver1_car['Speed'].max():.1f}",
        f"{driver1_car['Speed'].mean():.1f}",
        f"{int(driver1_car['RPM'].max()):,}"
    ],

    driver2_name: [
        driver2_team,
        format_laptime(driver2_fastest["LapTime"]),
        f"{driver2_car['Speed'].max():.1f}",
        f"{driver2_car['Speed'].mean():.1f}",
        f"{int(driver2_car['RPM'].max()):,}"
    ]
}
comparison_df = pd.DataFrame(comparison_data)
st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.markdown("##Speed Comparison")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=driver1_car["Distance"],
        y=driver1_car["Speed"],
        mode="lines",
        name=driver1,
        line=dict(color=driver1_color, width=3)
    )
)

fig.add_trace(
    go.Scatter(
        x=driver2_car["Distance"],
        y=driver2_car["Speed"],
        mode="lines",
        name=driver2,
        line=dict(color=driver2_color, width=3)
    )
)

fig.update_layout(
    title="Speed Comparison",
    xaxis_title="Distance (m)",
    yaxis_title="Speed (km/h)",
    template="plotly_dark",
    hovermode="x unified",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.markdown("##Driver Inputs")

col1, col2 = st.columns(2)

with col1:

    throttle_fig = go.Figure()

    throttle_fig.add_trace(
        go.Scatter(
            x=driver1_car["Distance"],
            y=driver1_car["Throttle"],
            mode="lines",
            name=driver1,
            line=dict(color=driver1_color, width=3)
        )
    )

    throttle_fig.add_trace(
        go.Scatter(
            x=driver2_car["Distance"],
            y=driver2_car["Throttle"],
            mode="lines",
            name=driver2,
            line=dict(color=driver2_color, width=3)
        )
    )

    throttle_fig.update_layout(
        title="Throttle Comparison",
        xaxis_title="Distance (m)",
        yaxis_title="Throttle (%)",
        template="plotly_dark",
        hovermode="x unified",
        height=420
    )

    st.plotly_chart(throttle_fig, use_container_width=True)

with col2:

    brake_fig = go.Figure()

    brake_fig.add_trace(
        go.Scatter(
            x=driver1_car["Distance"],
            y=driver1_car["Brake"],
            mode="lines",
            name=driver1,
            line=dict(color=driver1_color, width=3)
        )
    )

    brake_fig.add_trace(
        go.Scatter(
            x=driver2_car["Distance"],
            y=driver2_car["Brake"],
            mode="lines",
            name=driver2,
            line=dict(color=driver2_color, width=3)
        )
    )

    brake_fig.update_layout(
        title="Brake Comparison",
        xaxis_title="Distance (m)",
        yaxis_title="Brake",
        template="plotly_dark",
        hovermode="x unified",
        height=420
    )

    st.plotly_chart(brake_fig, use_container_width=True)

st.divider()
st.markdown("##Car Performance")

col1, col2, col3 = st.columns(3)

with col1:

    gear_fig = go.Figure()

    gear_fig.add_trace(go.Scatter(
        x=driver1_car["Distance"],
        y=driver1_car["nGear"],
        mode="lines",
        name=driver1,
        line=dict(color=driver1_color, width=3)
    ))

    gear_fig.add_trace(go.Scatter(
        x=driver2_car["Distance"],
        y=driver2_car["nGear"],
        mode="lines",
        name=driver2,
        line=dict(color=driver2_color, width=3)
    ))

    gear_fig.update_layout(
        title="Gear Changes",
        xaxis_title="Distance (m)",
        yaxis_title="Gear",
        template="plotly_dark",
        hovermode="x unified",
        height=400
    )

    st.plotly_chart(gear_fig, use_container_width=True)

with col2:

    rpm_fig = go.Figure()

    rpm_fig.add_trace(go.Scatter(
        x=driver1_car["Distance"],
        y=driver1_car["RPM"],
        mode="lines",
        name=driver1,
        line=dict(color=driver1_color, width=3)
    ))

    rpm_fig.add_trace(go.Scatter(
        x=driver2_car["Distance"],
        y=driver2_car["RPM"],
        mode="lines",
        name=driver2,
        line=dict(color=driver2_color, width=3)
    ))

    rpm_fig.update_layout(
        title="Engine RPM",
        xaxis_title="Distance (m)",
        yaxis_title="RPM",
        template="plotly_dark",
        hovermode="x unified",
        height=400
    )

    st.plotly_chart(rpm_fig, use_container_width=True)

with col3:

    drs_fig = go.Figure()

    drs_fig.add_trace(go.Scatter(
        x=driver1_car["Distance"],
        y=driver1_car["DRS"],
        mode="lines",
        name=driver1,
        line=dict(color=driver1_color, width=3)
    ))

    drs_fig.add_trace(go.Scatter(
        x=driver2_car["Distance"],
        y=driver2_car["DRS"],
        mode="lines",
        name=driver2,
        line=dict(color=driver2_color, width=3)
    ))

    drs_fig.update_layout(
        title="DRS Usage",
        xaxis_title="Distance (m)",
        yaxis_title="DRS",
        template="plotly_dark",
        hovermode="x unified",
        height=400
    )

    st.plotly_chart(drs_fig, use_container_width=True)

st.divider()

st.markdown("##Race Engineer Insights")

winner_speed = winner_lap.get_car_data()["Speed"].max()

loser_lap = driver2_fastest if winner == driver1 else driver1_fastest
loser_speed = loser_lap.get_car_data()["Speed"].max()

speed_diff = abs(winner_speed - loser_speed)

st.info(
    f"""
###Lap Summary

**Fastest Driver:** {winner_name}

**Fastest Lap:** {format_laptime(winner_lap['LapTime'])}

**Top Speed:** {winner_speed:.1f} km/h

**Top Speed Difference:** {speed_diff:.1f} km/h

The selected drivers have been compared using official FastF1 telemetry.
The graphs above illustrate differences in speed, throttle application,
braking behavior, gear changes, RPM, and DRS usage across the lap.
"""
)

st.divider()
st.caption(
    "F1 Telemetry Analytics Platform | Built using Python • FastF1 • Plotly • Streamlit"
)