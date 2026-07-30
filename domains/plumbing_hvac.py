import streamlit as st
from core_engine.webrtc_pipeline import render_live_stream
from ui_components.global_tools_db import get_tools_for_domain

def render():
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">💧 Plumbing & HVAC</h1>', unsafe_allow_html=True)
    st.markdown("Detect pipe leaks, pump cavitation, and boiler pressure issues.")
    
    render_live_stream("plumbing")
    
    st.subheader("🔧 Plumber's Arsenal")
    tools = get_tools_for_domain("plumbing")
    cols = st.columns(3)
    for i, (name, data) in enumerate(tools.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="clay-card" style="padding:12px;">
                <h4>{name}</h4>
                <img src="{data['icon_url']}" width="50">
            </div>
            """, unsafe_allow_html=True)
