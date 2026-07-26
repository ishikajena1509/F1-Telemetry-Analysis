import streamlit as st
import fastf1
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="Formula 1 Telemetry Dashboard",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏎️ Formula 1 Telemetry Dashboard")

st.write(
    "Interactive telemetry comparison using FastF1 and Plotly."
)
st.sidebar.header("⚙️ Dashboard Controls")
driver1 = st.sidebar.selectbox(
    "Driver 1",
    ["ANT", "RUS"]
)

driver2 = st.sidebar.selectbox(
    "Driver 2",
    ["RUS", "ANT"],
    index=0
)
if driver1 == driver2:
    st.warning("Please select two different drivers.")
    st.stop()
BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "cache"

CACHE_DIR.mkdir(exist_ok=True)

fastf1.Cache.enable_cache(str(CACHE_DIR))

session = fastf1.get_session(2026, "China", "Q")
session.load()

driver1_lap = session.laps.pick_drivers(driver1).pick_fastest()
driver2_lap = session.laps.pick_drivers(driver2).pick_fastest()

driver1_car_data = driver1_lap.get_car_data().add_distance()
driver2_car_data = driver2_lap.get_car_data().add_distance()
fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=driver1_car_data["Distance"],
        y=driver1_car_data["Speed"],
        mode="lines",
        name=driver1
    )
)

fig.add_trace(
    go.Scatter(
        x=driver2_car_data["Distance"],
        y=driver2_car_data["Speed"],
        mode="lines",
        name=driver2
    )
)

fig.update_layout(
    title="Speed Comparison",
    xaxis_title="Distance (m)",
    yaxis_title="Speed (km/h)",
    hovermode="x unified"
)
st.subheader("📊 Driver Performance Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Top Speed (" + driver1 + ")",
        f"{driver1_car_data['Speed'].max():.1f} km/h"
    )

    st.metric(
        "Average Speed",
        f"{driver1_car_data['Speed'].mean():.1f} km/h"
    )

    st.metric(
        "Maximum RPM",
        f"{driver1_car_data['RPM'].max():,.0f}"
    )

with col2:
    st.metric(
        "Top Speed (" + driver2 + ")",
        f"{driver2_car_data['Speed'].max():.1f} km/h"
    )

    st.metric(
        "Average Speed",
        f"{driver2_car_data['Speed'].mean():.1f} km/h"
    )

    st.metric(
        "Maximum RPM",
        f"{driver2_car_data['RPM'].max():,.0f}"
    )
st.divider()
st.subheader("📈 Interactive Speed Comparison")
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.subheader("📝 Engineering Insights")

st.write(f"""
### Driver Comparison

- **{driver1}** Top Speed: **{driver1_car_data['Speed'].max():.1f} km/h**
- **{driver2}** Top Speed: **{driver2_car_data['Speed'].max():.1f} km/h**

Both drivers reached competitive qualifying speeds.

Use the interactive chart to inspect braking zones,
corner exits, and acceleration throughout the lap.
""")
st.divider()

st.subheader("ℹ️ About")

st.write("""
This dashboard was built using:

- Python
- FastF1
- Pandas
- Plotly
- Streamlit

Developed as part of a Formula 1 Telemetry Analysis portfolio project.
""")