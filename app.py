import streamlit as st

st.set_page_config(
    page_title="F1 Telemetry Analytics Platform",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main-title{
    font-size:82px;
    font-weight:900;
    color:#E10600;
    line-height:1.05;
    margin-bottom:0px;
}

.tagline{
    font-size:34px;
    color:#ECECEC;
    font-weight:600;
    margin-top:-8px;
    line-height:1.4;
}
.section-title{
    font-size:30px;
    font-weight:700;
    color:white;
    margin-top:20px;
}

.card{
    background:#181818;
    padding:25px;
    border-radius:18px;
    border:1px solid #333333;
    box-shadow:0px 6px 18px rgba(0,0,0,0.35);
}

.card:hover{
    border:1px solid #E10600;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}
hr{
    border-color:#2b2b2b;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <p class="main-title">
    🏎️<br>
    F1 Telemetry<br>
    Analytics Platform
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="tagline">

    Analyze. Compare. Understand.<br><br>

    Formula 1 performance
    like a race engineer.

    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
"""
Welcome to the **F1 Telemetry Analytics Platform**.

This application allows you to compare Formula 1 drivers using real telemetry data
from the FastF1 library. Explore speed, throttle, braking, RPM, and performance
metrics through interactive visualizations and engineering-style insights.
"""
)

st.divider()

st.markdown(
    """
    <p class="section-title">
    🚀 Explore the Platform
    </p>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        <div class="card">

        <h3>📊 Dashboard</h3>

        Compare two Formula 1 drivers using
        telemetry data including speed,
        throttle, brake and RPM.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="card">

        <h3>📈 Insights</h3>

        View engineering summaries,
        performance statistics,
        and race engineer reports.

        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class="card">

        <h3>🌍 Circuit Explorer</h3>

        Learn about Formula 1 circuits,
        track layouts,
        and race information.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="card">

        <h3>📖 Telemetry Guide</h3>

        Understand every telemetry metric
        used throughout the platform.

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown(
    """
    <p class="section-title">
    🛠 Technology Stack
    </p>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🐍 Language", "Python")

with col2:
    st.metric("🏎 Data", "FastF1")

with col3:
    st.metric("📊 Charts", "Plotly")

with col4:
    st.metric("📈 Analysis", "Pandas")

with col5:
    st.metric("💻 Framework", "Streamlit")

st.divider()

st.markdown(
    """
    <p class="section-title">
    ⚙️ Analytics Workflow
    </p>
    """,
    unsafe_allow_html=True
)

workflow = """
📥 Race Data

⬇️

🏎 FastF1 API

⬇️

🐍 Python Processing

⬇️

📊 Interactive Visualizations

⬇️

🧠 Engineering Insights
"""

st.code(workflow, language="text")

st.divider()

st.markdown(
    """
    <p class="section-title">
    💼 Why This Project?
    </p>
    """,
    unsafe_allow_html=True
)

st.info(
    """
Formula 1 generates millions of telemetry data points throughout a race weekend.

This platform transforms raw telemetry into interactive visualizations and engineering-style insights, demonstrating practical skills in:

• Python Programming

• Data Analysis

• Data Visualization

• Software Development

• Motorsport Analytics

The project has been built as a portfolio application to showcase real-world engineering and analytical skills.
"""
)
st.divider()

st.markdown(
"""
<div class="footer">

Built with ❤️ using Python • FastF1 • Pandas • Plotly • Streamlit

</div>
""",
unsafe_allow_html=True
)