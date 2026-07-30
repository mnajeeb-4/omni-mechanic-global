import streamlit as st
from core_engine.webrtc_pipeline import render_live_stream
from ui_components.global_tools_db import get_tools_for_domain

def render():
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">⚡ Electrical Hub & PCB</h1>', unsafe_allow_html=True)
    st.markdown("Detect burnt resistors, broken traces, and live wire shorts.")
    
    render_live_stream("electrical")
    
    st.subheader("🔧 Tools for Electricians")
    tools = get_tools_for_domain("electrical")
    for name, data in tools.items():
        with st.expander(f"🔧 {name}"):
            st.markdown(f"**Usage:** {data['usage']}")
            st.image(data['icon_url'], width=80)
