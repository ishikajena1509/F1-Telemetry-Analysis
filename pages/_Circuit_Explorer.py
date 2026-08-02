import streamlit as st
import pandas as pd
from PIL import Image
sprite_sheet = Image.open("assets/circuits/circuits_sheet.png")
st.set_page_config(
    page_title="Circuit Explorer | F1 Telemetry Analytics Platform",
    page_icon="🏁",
    layout="wide"
)

st.markdown("""
#Circuit Explorer

Explore Formula 1 circuits before diving into telemetry analysis.
""")

st.divider()

st.info(
    "Select a circuit to view key information, track characteristics, and interesting facts."
)
circuits = pd.read_csv("data/circuits.csv")
selected_gp = st.selectbox(
    "Select a Grand Prix",
    circuits["Grand Prix"]
)
circuit = circuits[circuits["Grand Prix"] == selected_gp].iloc[0]

st.markdown("##Circuit Information")

col1, col2 = st.columns(2)

with col1:

    st.metric("Circuit", circuit["Circuit"])

    st.metric("Country", circuit["Country"])

    st.metric("Track Length", circuit["Track Length"])

with col2:

    st.metric("Corners", circuit["Corners"])

    st.metric("Race Distance", circuit["Race Distance"])

    st.metric("DRS Zones", circuit["DRS Zones"])

st.metric("Lap Record", circuit["Lap Record"])

st.divider()

track_characteristics = {
    "China GP": {
        "Top Speed": 4,
        "Overtaking": 4,
        "Braking": 4,
        "Tyre Wear": 3
    },

    "Belgium GP": {
        "Top Speed": 5,
        "Overtaking": 5,
        "Braking": 3,
        "Tyre Wear": 3
    },

    "Japan GP": {
        "Top Speed": 3,
        "Overtaking": 2,
        "Braking": 4,
        "Tyre Wear": 5
    }
}

ratings = {
    "Top Speed": int(circuit["Top Speed"]),
    "Overtaking": int(circuit["Overtaking"]),
    "Braking": int(circuit["Braking"]),
    "Tyre Wear": int(circuit["Tyre Wear"]),
}

st.markdown("##Track Characteristics")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Top Speed:** {'⭐' * ratings['Top Speed']}")
    st.write(f"**Overtaking:** {'⭐' * ratings['Overtaking']}")

with col2:
    st.write(f" **Braking:** {'⭐' * ratings['Braking']}")
    st.write(f" **Tyre Wear:** {'⭐' * ratings['Tyre Wear']}")

st.divider()

st.markdown("## Interesting Facts")
st.success(f"✅ {circuit['Fact 1']}")
st.success(f"✅ {circuit['Fact 2']}")
st.success(f"✅ {circuit['Fact 3']}")
st.divider()

