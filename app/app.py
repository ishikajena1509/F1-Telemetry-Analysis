import streamlit as st
import fastf1
import plotly.graph_objects as go
from pathlib import Path
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Formula 1 Telemetry Dashboard",
    page_icon="🏎️",
    layout="wide"
)

st.title("🏎️ Formula 1 Telemetry Dashboard")

st.write(
    "Interactive telemetry comparison using FastF1 and Plotly."
)

BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "cache"

CACHE_DIR.mkdir(exist_ok=True)

fastf1.Cache.enable_cache(str(CACHE_DIR))

session = fastf1.get_session(2026, "China", "Q")
session.load()
available_drivers = sorted(
    session.laps["Driver"].dropna().unique()
)
st.sidebar.header("⚙️ Dashboard Controls")

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
    st.warning("Please select two different drivers.")
    st.stop()
driver1_lap = session.laps.pick_drivers(driver1).pick_fastest()
driver2_lap = session.laps.pick_drivers(driver2).pick_fastest()

driver1_car_data = driver1_lap.get_car_data().add_distance()
driver2_car_data = driver2_lap.get_car_data().add_distance()

driver1_data = driver1_car_data
driver2_data = driver2_car_data

fig = make_subplots(
    rows=4,
    cols=1,
    shared_xaxes=True,
    subplot_titles=(
        "🚀 Speed (km/h)",
        "🟢 Throttle (%)",
        "🔴 Brake",
        "⚙️ RPM"
    ),
    vertical_spacing=0.08
)

fig.add_trace(
    go.Scatter(
        x=driver1_data["Distance"],
        y=driver1_data["Speed"],
        mode="lines",
        name=driver1,
        line=dict(width=2)
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver2_data["Distance"],
        y=driver2_data["Speed"],
        mode="lines",
        name=driver2,
        line=dict(width=2)
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver1_data["Distance"],
        y=driver1_data["Throttle"],
        mode="lines",
        name=driver1,
        showlegend=False,
        line=dict(width=2)
    ),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver2_data["Distance"],
        y=driver2_data["Throttle"],
        mode="lines",
        name=driver2,
        showlegend=False,
        line=dict(width=2)
    ),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver1_data["Distance"],
        y=driver1_data["Brake"].astype(int),
        mode="lines",
        name=driver1,
        showlegend=False,
        line=dict(width=2)
    ),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver2_data["Distance"],
        y=driver2_data["Brake"].astype(int),
        mode="lines",
        name=driver2,
        showlegend=False,
        line=dict(width=2)
    ),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver1_data["Distance"],
        y=driver1_data["RPM"],
        mode="lines",
        name=driver1,
        showlegend=False,
        line=dict(width=2)
    ),
    row=4, col=1
)

fig.add_trace(
    go.Scatter(
        x=driver2_data["Distance"],
        y=driver2_data["RPM"],
        mode="lines",
        name=driver2,
        showlegend=False,
        line=dict(width=2)
    ),
    row=4, col=1
)

fig.update_yaxes(title_text="km/h", row=1, col=1)
fig.update_yaxes(title_text="%", row=2, col=1)
fig.update_yaxes(title_text="Brake", row=3, col=1)
fig.update_yaxes(title_text="RPM", row=4, col=1)

fig.update_xaxes(title_text="", row=1, col=1)
fig.update_xaxes(title_text="", row=2, col=1)
fig.update_xaxes(title_text="", row=3, col=1)
fig.update_xaxes(title_text="Distance (m)", row=4, col=1)

fig.update_layout(
    title={
        "text": "Formula 1 Telemetry Comparison",
        "x": 0.5,
        "xanchor": "center"
    },
    template="plotly_dark",
    hovermode="x unified",
    height=1250,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.03,
        xanchor="right",
        x=1
    ),
    margin=dict(
        l=70,
        r=40,
        t=100,
        b=70
    )
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

st.subheader("📈 Telemetry Comparison")
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.subheader("📝 Engineering Insights")

driver1_top = driver1_data["Speed"].max()
driver2_top = driver2_data["Speed"].max()

driver1_avg = driver1_data["Speed"].mean()
driver2_avg = driver2_data["Speed"].mean()

driver1_rpm = driver1_data["RPM"].max()
driver2_rpm = driver2_data["RPM"].max()

if driver1_top > driver2_top:
    faster = driver1
else:
    faster = driver2
if driver1_avg > driver2_avg:
    avg_faster = driver1
else:
    avg_faster = driver2
if driver1_rpm > driver2_rpm:
    rpm_driver = driver1
else:
    rpm_driver = driver2

st.success(f"🏁 {faster} recorded the highest top speed.")

st.info(f"📈 {avg_faster} maintained the higher average speed over the lap.")

st.warning(f"⚙️ {rpm_driver} reached the highest engine RPM.")

st.markdown("### Comparison Summary")

st.write(f"""
- **Top Speed Difference:** {abs(driver1_top-driver2_top):.2f} km/h
- **Average Speed Difference:** {abs(driver1_avg-driver2_avg):.2f} km/h
- **RPM Difference:** {abs(driver1_rpm-driver2_rpm):,.0f}

These insights are generated automatically from the selected drivers' telemetry data.
""")

st.subheader("ℹ️ About")

st.write("""
This dashboard was built using:

- Python
- FastF1
- Pandas
- Plotly
- Streamlit

The application enables interactive comparison of Formula 1 qualifying telemetry between two selected drivers.
Developed as part of a Formula 1 Telemetry Analysis portfolio project.
""")