import streamlit as st

st.set_page_config(
    page_title="About Project | F1 Telemetry Analytics Platform",
    page_icon="👨‍💻",
    layout="wide"
)

st.markdown("""
<div style='text-align:center;padding:20px;'>
    <h1>👨‍💻 About the Project</h1>
    <h4>Discover the motivation, technologies, and engineering concepts behind the F1 Telemetry Analytics Platform.</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("## 🏎️ Project Overview")

st.info("""
### F1 Telemetry Analytics Platform

The F1 Telemetry Analytics Platform is a multi-page interactive web application developed using Python, Streamlit, FastF1, Plotly, and Pandas.

The platform enables users to explore Formula 1 telemetry data, compare driver performance, analyze race engineering metrics, and understand the technical aspects of motorsport through interactive visualizations.

The primary objective of this project is to combine software engineering, data analytics, and motorsport into an educational and analytical platform that demonstrates practical data visualization techniques.
""")

st.divider()

st.markdown("## 🎯 Objectives")

st.success("""✅ Learn motorsport data analysis

✅ Build an interactive analytics dashboard

✅ Visualize Formula 1 telemetry

✅ Compare driver performance

✅ Strengthen Python, Streamlit, and Plotly skills

✅ Create a professional portfolio project
""")

st.divider()

st.markdown("## 🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Programming", "Python")

with col2:
    st.metric("Framework", "Streamlit")

with col3:
    st.metric("Telemetry", "FastF1")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Visualization", "Plotly")

with col5:
    st.metric("Data", "Pandas")

with col6:
    st.metric("Numerical", "NumPy")

st.divider()

st.markdown("## ✨ Key Features")

st.markdown("""
- 📊 Interactive Dashboard for telemetry analysis
- 🏎️ Driver performance comparison
- 🚀 Speed, Throttle, Brake, Gear, RPM & DRS visualizations
- 📈 Automated engineering insights
- 🏁 Circuit Explorer covering all current Formula 1 circuits
- 📖 Telemetry Guide for beginners
- 📑 Dedicated About Project documentation
- 🎨 Interactive and responsive Streamlit interface
""")

st.divider()

st.markdown("## 📈 Challenges & Learnings")

st.info("""
### Challenges Faced

• Understanding Formula 1 telemetry data structures.

• Working with FastF1 APIs and session data.

• Designing an interactive multi-page Streamlit application.

• Organizing project files for better maintainability.

### What I Learned

• Building interactive dashboards with Streamlit.

• Data visualization using Plotly.

• Processing motorsport telemetry using FastF1.

• Structuring a real-world analytics project.

• Improving UI/UX for technical applications.
""")

st.divider()

st.markdown("## 🚀 Future Enhancements")

st.success("""
✔ Support for multiple Formula 1 seasons

✔ Race pace and tyre strategy analysis

✔ Pit stop performance dashboard

✔ Driver consistency analysis

✔ Lap delta comparison

✔ Export engineering reports as PDF

✔ Live session support (where applicable)

✔ Additional interactive visualizations
""")

st.divider()

st.markdown("## 👩‍💻 Developer")

st.markdown("""
### Ms. Ishika Jena

Computer Science & Engineering Student

This project was developed as a personal portfolio project to combine software engineering, data analytics, and Formula 1 into an interactive learning and analysis platform.

The goal was not only to analyze telemetry data but also to build a scalable, user-friendly application that demonstrates problem-solving, data visualization, and software development skills.
""")

st.divider()

st.caption(
    "🏎️ Thank you for exploring the F1 Telemetry Analytics Platform!"
    "🏎️ F1 Telemetry Analytics Platform | Built using Python • FastF1 • Plotly • Streamlit"
)