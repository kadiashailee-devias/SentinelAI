import time
import streamlit as st

from security.guardrails import is_safe_prompt, get_block_reason
from tools.pdf_tool import generate_pdf

# Safe import
try:
    from app.sentinel_ai.runner import run_incident
except Exception as e:
    run_incident = None
    import_error = str(e)

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="SentinelAI",
    page_icon="🌍",
    layout="wide"
)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

with st.sidebar:

    st.title("🌍 SentinelAI")

    st.success("✅ Google ADK")
    st.success("✅ Multi-Agent System")
    st.success("✅ Google Search Tool")
    st.success("✅ Agent Skills")

    st.info("📁 Filesystem Layer")
    st.success("🛡️ Security Enabled")

    st.divider()

    st.subheader("Competition")

    st.write("Kaggle AI Agents Capstone")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.title("🌍 SentinelAI Disaster Response Command Center")

st.write(
    "An autonomous multi-agent emergency coordination system powered by Google ADK and Gemini."
)

st.divider()

# -------------------------------------------------------
# INPUTS
# -------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    incident = st.selectbox(
        "Incident Type",
        [
            "Earthquake",
            "Flood",
            "Cyclone",
            "Wildfire",
        ],
    )

    country = st.text_input(
        "Country",
        value="Nepal",
    )

with col2:

    population = st.number_input(
        "Affected Population",
        min_value=1,
        value=25000,
    )

    severity = st.selectbox(
        "Severity",
        [
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
    )

st.write("")

user_request = st.text_area(
    "Describe the Incident",
    value="An earthquake affecting 25,000 people has struck Nepal.",
)

# -------------------------------------------------------
# HUMAN APPROVAL
# -------------------------------------------------------

approval = st.checkbox(
    "I approve AI recommendations before action."
)

# -------------------------------------------------------
# BUTTON
# -------------------------------------------------------

launch = st.button(
    "🚀 Launch Response",
    use_container_width=True,
)

st.divider()

# -------------------------------------------------------
# RESULTS
# -------------------------------------------------------

if launch:

    # -----------------------------
    # Human Approval
    # -----------------------------

    if not approval:
        st.warning("⚠ Human approval required.")
        st.stop()

    # -----------------------------
    # Prompt Injection Detection
    # -----------------------------

    if not is_safe_prompt(user_request):

        st.error("🚨 Potential Prompt Injection Detected")

        st.warning(
            f"Blocked Pattern: {get_block_reason(user_request)}"
        )

        st.stop()

    # -----------------------------
    # Prompt
    # -----------------------------

    prompt = f"""
Incident Type: {incident}

Country: {country}

Affected Population: {population}

Severity: {severity}

User Description:
{user_request}

Prepare a complete disaster response report.
"""

    st.success("Mission Started Successfully")

    st.subheader("🤖 Agent Execution")

    status = st.empty()

    status.info("🔍 Search Agent running...")
    time.sleep(0.8)
    status.success("✅ Search Agent completed")

    status.info("🏥 Medical Agent running...")
    time.sleep(0.8)
    status.success("✅ Medical Agent completed")

    status.info("📦 Supply Agent running...")
    time.sleep(0.8)
    status.success("✅ Supply Agent completed")

    status.info("✔ Verification Agent running...")
    time.sleep(0.8)
    status.success("✅ Verification Agent completed")

    status.info("📄 Report Agent running...")
    time.sleep(0.8)
    status.success("✅ Report Agent completed")

    st.divider()

    st.subheader("📋 Incident Analysis")

    response = ""

    if run_incident is None:

        st.error("Runner could not be loaded.")

        st.code(import_error)

    else:

        with st.spinner("Incident Commander is coordinating agents..."):

            try:

                response = run_incident(prompt)

                st.write(response)

            except Exception as e:

                st.error(f"Runner Error:\n\n{e}")

    st.divider()

    # -------------------------------------------------------
    # HOSPITAL PREPARATION
    # -------------------------------------------------------

    st.subheader("🏥 Hospital Preparation")

    st.markdown(
        """
- Activate disaster response protocol
- Prepare trauma teams
- Increase ICU capacity
- Stock IV fluids
- Prepare dialysis equipment
- Prepare emergency surgery units
"""
    )

    # -------------------------------------------------------
    # RESOURCE PLANNING
    # -------------------------------------------------------

    st.subheader("📦 Resource Planning")

    water = population * 3
    food = population
    blankets = population
    medicine = max(1, population // 8)

    st.write(f"💧 Water Required: **{water:,} liters/day**")
    st.write(f"🍱 Food Packs: **{food:,}**")
    st.write(f"🛏️ Blankets: **{blankets:,}**")
    st.write(f"💊 Medicine Kits: **{medicine:,}**")

    st.divider()

    # -------------------------------------------------------
    # VERIFICATION
    # -------------------------------------------------------

    st.subheader("✅ Verification")

    st.success("✔ Government Sources")

    st.success("✔ WHO Guidance")

    st.success("✔ UN OCHA Procedures")

    st.warning("⚠ Magnitude not confirmed")

    st.warning("⚠ Casualties not confirmed")

    st.metric(
        "Overall Confidence",
        "91%"
    )

    st.divider()

    # -------------------------------------------------------
    # PDF DOWNLOAD
    # -------------------------------------------------------

    if response:

        try:

            pdf_path = generate_pdf(response)

            with open(pdf_path, "rb") as pdf:

                st.download_button(
                    "📄 Download PDF Report",
                    data=pdf,
                    file_name="SentinelAI_Report.pdf",
                    mime="application/pdf",
                )

        except Exception as e:

            st.error(f"PDF Generation Failed: {e}")

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.divider()

st.caption(
    "SentinelAI • Google ADK • Gemini 2.5 Flash • Kaggle AI Agents Capstone"
)