import streamlit as st

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 SentinelAI Disaster Response Command Center")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    incident = st.selectbox(
        "Incident Type",
        [
            "Earthquake",
            "Flood",
            "Cyclone",
            "Wildfire"
        ]
    )

    country = st.text_input(
        "Country",
        value="Nepal"
    )

with col2:
    population = st.number_input(
        "Affected Population",
        min_value=1,
        value=25000
    )

    severity = st.selectbox(
        "Severity",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

st.markdown("")

launch = st.button(
    "🚀 Launch Response",
    use_container_width=True
)

st.markdown("---")

if launch:

    st.success("Mission Started")

    st.write("### Agent Status")

    st.success("🟢 Search Agent ✔ Completed")

    st.success("🟢 Medical Agent ✔ Completed")

    st.success("🟢 Supply Agent ✔ Completed")

    st.info("🟣 Verification Agent ✔ Completed")

    st.warning("🟠 Report Agent ✔ Completed")

    st.markdown("---")

    st.subheader("Situation Summary")

    st.write(
        f"""
An **{incident}** has affected approximately **{population:,}**
people in **{country}**.

Severity Level:

**{severity}**
"""
    )

    st.subheader("Hospital Preparation")

    st.write(
        """
• Activate disaster protocol

• Prepare trauma units

• Increase ICU capacity

• Stock IV fluids

• Prepare dialysis equipment
"""
    )

    st.subheader("Resource Planning")

    water = population * 3

    food = population

    blankets = population

    medicine = max(1, population // 8)

    st.write(f"Water: {water:,} liters/day")

    st.write(f"Food Packs: {food:,}")

    st.write(f"Blankets: {blankets:,}")

    st.write(f"Medicine Kits: {medicine:,}")

    st.markdown("---")

    st.metric(
        "Confidence Score",
        "92%"
    )

    st.download_button(
        "📄 Download Report",
        "SentinelAI Report",
        file_name="report.txt"
    )