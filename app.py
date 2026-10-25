"""
SlothSurf Streamlit Web Dashboard.
Run with: streamlit run app.py
"""

import asyncio
import os
import streamlit as st
from slothsurf.config import Config
from slothsurf.presets import PRESET_TASKS
from slothsurf.agent import execute_task

st.set_page_config(
    page_title="SlothSurf — The Zero-Effort Web Agent",
    page_icon="🦥",
    layout="wide",
)

st.title("🦥 SlothSurf")
st.subheader("The Zero-Effort Autonomous Browser Agent for Lazy Humans")
st.caption("Theme: Slow & Steady (International Sloth Day) | Powered by open-source browser-use & xAI Grok")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Sloth Control Panel")
    api_key_input = st.text_input(
        "xAI API Key",
        value=Config.XAI_API_KEY if Config.XAI_API_KEY != "your_xai_api_key_here" else "",
        type="password",
        help="Get your key at https://console.x.ai/",
    )
    if api_key_input:
        Config.XAI_API_KEY = api_key_input

    model_option = st.selectbox(
        "Grok Model",
        options=["grok-2-vision-1212", "grok-2-1212", "grok-beta"],
        index=0,
        help="grok-2-vision-1212 is recommended for visual browser grounding.",
    )
    Config.GROK_MODEL = model_option

    headless = st.checkbox("Headless Mode (Hide Browser Window)", value=False)
    slow_mo = st.slider("Sloth Speed (Slow-Mo in ms)", min_value=200, max_value=3000, value=1000, step=200)

    st.markdown("---")
    st.markdown(
        "**Why Open Source?**\n"
        "Built on `browser-use` — an open-source agent harness giving you complete programmatic control over your browser with zero vendor lock-in."
    )

# Main task interface
st.write("### Choose a Lazy Mission")

tab1, tab2 = st.tabs(["⚡ One-Click Presets", "✍️ Custom Lazy Task"])

selected_task = ""

with tab1:
    preset_choice = st.radio(
        "Select a pre-configured sloth mission:",
        options=list(PRESET_TASKS.keys()),
        format_func=lambda k: f"{PRESET_TASKS[k]['title']} — {PRESET_TASKS[k]['description']}",
    )
    selected_task = PRESET_TASKS[preset_choice]["task"]
    st.info(f"**Task Prompt:**\n\n{selected_task}")

with tab2:
    custom_task_input = st.text_area(
        "Describe whatever web chore you're too lazy to do:",
        placeholder="e.g. Go to Reddit r/technology, find the top post today, and summarize why everyone is arguing about it.",
        height=120,
    )
    if custom_task_input.strip():
        selected_task = custom_task_input.strip()

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🏄 Surf For Me (Conserve My Energy)", type="primary", use_container_width=True):
    if not Config.XAI_API_KEY or Config.XAI_API_KEY == "your_xai_api_key_here":
        st.error("Please enter a valid xAI API Key in the sidebar to run the agent!")
    elif not selected_task:
        st.warning("Please select or enter a task first.")
    else:
        with st.status("🦥 Sloth is browsing the web... stay calm and do nothing...", expanded=True) as status:
            st.write("Initializing Chromium browser via Playwright...")
            st.write(f"Connecting to xAI Grok ({Config.GROK_MODEL})...")
            
            try:
                result = asyncio.run(execute_task(selected_task, headless=headless, slow_mo=slow_mo))
                status.update(label="✅ Sloth Mission Completed!", state="complete", expanded=False)
                
                st.success("Mission Accomplished! Here is your lazy briefing:")
                st.markdown(result)
            except Exception as e:
                status.update(label="❌ Something went wrong", state="error")
                st.error(f"Error during execution: {e}")
