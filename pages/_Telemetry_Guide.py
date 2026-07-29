import streamlit as st

st.set_page_config(
    page_title="Telemetry Guide | F1 Telemetry Analytics Platform",
    page_icon="📖",
    layout="wide"
)

st.markdown("""
<div style='text-align:center;padding:20px;'>
    <h1>📖 Telemetry Guide</h1>
    <h4>Understand the key telemetry signals used by Formula 1 engineers to analyze driver performance.</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("## 🚀 Speed")

st.info("""
### What is Speed?

Speed telemetry shows how fast the Formula 1 car is travelling at every point on the circuit.

### Why is it important?

• Compare straight-line performance between drivers.

• Analyze corner entry and exit speed.

• Identify where a driver gains or loses time.

### Engineering Insight

Engineers compare speed traces to understand whether a driver is braking too early, accelerating too late, or carrying more speed through corners.
""")

st.divider()

st.markdown("## 🟢 Throttle")

st.info("""
### What is Throttle?

Throttle telemetry shows how much accelerator input the driver is applying. It is measured as a percentage from 0% to 100%.

### Why is it important?

• Compare acceleration between drivers.

• Understand traction out of corners.

• Identify smooth or aggressive throttle application.

### Engineering Insight

A driver who applies the throttle smoothly usually has better traction and tyre management. Sudden throttle inputs may lead to wheelspin and slower corner exits.
""")

st.divider()

st.markdown("## 🛑 Brake")

st.info("""
### What is Brake?

Brake telemetry indicates when and how strongly the driver applies the brakes before entering a corner.

### Why is it important?

• Compare braking points.

• Analyze braking consistency.

• Detect late or early braking.

### Engineering Insight

Efficient braking allows a driver to slow the car just enough before the corner while maximizing exit speed. Braking too late can compromise the entire corner.
""")

st.divider()

st.markdown("## ⚙️ Gear")

st.info("""
### What is Gear?

Gear telemetry shows which gear is engaged throughout the lap.

### Why is it important?

• Understand shifting strategy.

• Compare driving styles.

• Analyze acceleration and cornering behaviour.

### Engineering Insight

Different gear choices can reveal how drivers balance acceleration, stability, and traction through different sections of the circuit.
""")

st.divider()

st.markdown("## 🔁 RPM")

st.info("""
### What is RPM?

RPM (Revolutions Per Minute) measures how fast the engine is rotating.

### Why is it important?

• Optimize gear changes.

• Monitor engine performance.

• Compare acceleration phases.

### Engineering Insight

Maintaining the engine within its optimal RPM range ensures maximum performance and efficient power delivery.
""")

st.divider()

st.markdown("## 📡 DRS")

st.info("""
### What is DRS?

The Drag Reduction System (DRS) opens the rear wing to reduce aerodynamic drag, increasing straight-line speed.

### Why is it important?

• Improve overtaking opportunities.

• Increase top speed on straights.

• Reduce lap times.

### Engineering Insight

Engineers analyze DRS activation to evaluate overtaking performance and determine whether drivers are maximizing available DRS zones.
""")

st.divider()

st.caption(
    "📖 Understanding telemetry is the first step toward analyzing Formula 1 performance like a race engineer."
    "🏎️ F1 Telemetry Analytics Platform | Built using Python • FastF1 • Plotly • Streamlit"
)