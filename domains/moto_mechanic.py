import streamlit as st
from core_engine.webrtc_pipeline import render_live_stream
from ui_components.global_tools_db import get_tools_for_domain

def render():
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">🏍️ Motorcycle & Scooter Diagnostics</h1>', unsafe_allow_html=True)
    st.markdown("Analyze chain slack, exhaust pops, and frame stress fractures.")
    
    render_live_stream("moto")
    
    st.subheader("🔧 Recommended Tools for Bikes")
    tools = get_tools_for_domain("moto")
    cols = st.columns(2)
    for i, (name, data) in enumerate(tools.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="clay-card" style="text-align:center;">
                <img src="{data['icon_url']}" width="60">
                <h4 style="color:#6C63FF;">{name}</h4>
                <p style="font-size:0.85rem;">{data['description']}</p>
            </div>
            """, unsafe_allow_html=True)
