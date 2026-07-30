import streamlit as st
from core_engine.webrtc_pipeline import render_live_stream
from ui_components.global_tools_db import get_tools_for_domain

def render():
    st.markdown('<h1 style="text-shadow: 0 0 20px rgba(108,99,255,0.3);">🏠 Home Appliances</h1>', unsafe_allow_html=True)
    st.markdown("AC compressor hums, washing machine drum wobbles, fridge cooling faults.")
    
    render_live_stream("home")
    
    st.subheader("🔧 Appliance Tools")
    tools = get_tools_for_domain("home")
    cols = st.columns(2)
    for i, (name, data) in enumerate(tools.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="clay-card">
                <img src="{data['icon_url']}" width="40">
                <h4>{name}</h4>
                <p>{data['description']}</p>
            </div>
            """, unsafe_allow_html=True)
