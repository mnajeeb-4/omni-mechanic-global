import streamlit as st
from core_engine.webrtc_pipeline import render_live_stream
from ui_components.global_tools_db import get_tools_for_domain

def render():
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">🚗 Automotive & Heavy Machinery</h1>', unsafe_allow_html=True)
    st.markdown("Diagnose engine misfires, transmission whines, and belt slips in real-time.")
    
    render_live_stream("auto")
    
    st.markdown("---")
    st.subheader("🔧 Recommended Tools for Auto")
    tools = get_tools_for_domain("auto")
    cols = st.columns(3)
    for i, (name, data) in enumerate(tools.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="clay-card" style="text-align:center;">
                <img src="{data['icon_url']}" width="60" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));">
                <h4 style="color:#6C63FF;">{name}</h4>
                <p style="font-size:0.85rem;">{data['description']}</p>
                <span style="background:#2A2F38; padding:4px 12px; border-radius:20px; font-size:0.7rem;">{data['usage']}</span>
            </div>
            """, unsafe_allow_html=True)
